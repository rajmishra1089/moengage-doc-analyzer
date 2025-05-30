"""
MoEngage Documentation Analyzer and Rewriter using Gemini LLM

This script fetches a documentation article from MoEngage Help Center, analyzes it using Gemini
to suggest improvements (Agent 1), and then applies those suggestions to revise the article (Agent 2).

Outputs are saved as:
  - [slug]__original.md
  - [slug]__suggestions.md
  - [slug]__revised.md
"""



import urllib.request
from bs4 import BeautifulSoup
import html2text
import re
from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize Gemini client with your API key
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def fetch_article_html(url):
    """
    Fetch the HTML content of the MoEngage documentation article.

    Args:
        url (str): The full URL of the MoEngage Help Center article.

    Returns:
        tuple: (HTML string of content div, error message if any)
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
    }

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            soup = BeautifulSoup(html, 'html.parser')
            content_div = soup.find("div", class_="article__body")
            if not content_div:
                return None, "❌ Could not find article content."
            for tag in content_div(["script", "style"]):
                tag.decompose()
            return str(content_div), None
    except Exception as e:
        return None, f"❌ Error fetching article: {e}"

def html_to_markdown(html):
    """
    Convert cleaned HTML into Markdown format.

    Replaces all image tags with a standard inline placeholder.
    Uses html2text for HTML to Markdown conversion.

    Args:
        html (str): HTML string of article content.

    Returns:
        str: Markdown version of the article.
    """
    soup = BeautifulSoup(html, 'html.parser')
    for img in soup.find_all("img"):
        img.replace_with(
            "(Screenshot was present in the original article and has been replaced with a description inline. Please do not suggest adding screenshots.)"
        )
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0
    return h.handle(str(soup))

def replace_image_markdown(text):
    """
    Replace Markdown image syntax with explicit placeholder text to indicate image removal.

    Args:
        text (str): Markdown content that may contain image syntax.

    Returns:
        str: Markdown with image placeholders.
    """
    return re.sub(
        r"!\[.*?\]\(.*?\)",
        "(INTENTIONALLY REMOVED IMAGE: Original article contained a screenshot at this point)",
        text
    )

def build_analysis_prompt(url, article_text):
    """
    Build the prompt string for the Gemini Analyzer agent.

    Args:
        url (str): Article URL.
        article_text (str): Markdown text of the article.

    Returns:
        str: Formatted prompt for the LLM to analyze documentation quality.
    """
    return f"""
You are a Documentation Analyzer Agent. Analyze the following documentation article from MoEngage: {url}

IMPORTANT INSTRUCTIONS:
1. IMAGE HANDLING:
   - The original article contained screenshots that have been replaced with inline descriptions.
   - Please do NOT suggest adding, describing, or improving images/screenshots.

2. STEP TRANSITIONS:
   - Do not critique transitions between steps unless they are completely missing.
   - Assume transitions are adequately shown in the original article.

3. FOCUS ON:
   - Conceptual clarity of instructions
   - Missing information that would prevent task completion
   - Terminology explanations
   - Overall logical flow (not visual layout)

Here is the extracted article text:
\"\"\"
{article_text}
\"\"\"

Please format your response in **Markdown** using the structure below:

## URL
`{url}`

## 1. Readability for Marketers
**Assessment:**  
#    - Can non-technical users understand core concepts?
#    - Are technical terms explained?
#    - Is the tone appropriate?
#    - Highlight any confusing phrases or sections.
#    - Optionally, infer and comment on the document's approximate readability level (e.g., beginner-friendly or expert-level).

**Suggestions:**  
- List suggestions to improve readability, clarity, or tone.

## 2. Structural Quality
**Assessment:**  
#    - Are headings clear and hierarchical?
#    - Is information properly grouped?
#    - Can users easily scan the content?

**Suggestions:**  
- List improvements for structure, organization, or flow of content.

## 3. Textual Completeness
**Assessment:**  
#    - Could the text standalone without images?
#    - Are all necessary steps/textual explanations present?
#    - Are there conceptual gaps in the instructions?

**Suggestions:**  
- List what information might be missing or unclear.
  
**Disclaimers:**  
- Original contains supporting images  
- Step transitions assumed adequate in original

## 4. Style Adherence
**Assessment:**  
#    - Is the style clear and consistent?
#    - Are instructions action-oriented?
#    - Is the tone professional yet approachable?

**Suggestions:**  
- List changes to improve clarity, tone, and action-oriented language.
"""

def build_revision_prompt(original_md, suggestions_md):
    """Generate a prompt to revise the documentation according to provided suggestions."""
    return f"""
You are a Documentation Revision Agent.

Your task is to revise the following documentation article **by fully and accurately incorporating every suggestion listed below**. 

Guidelines:
- Apply **all** provided suggestions without skipping any.
- If a suggestion is unclear, make the best possible revision based on context.
- Preserve the structure unless a structural change is explicitly suggested.
- Do **not** add or remove images, or add new content outside the suggestions.

Here is the original documentation (Markdown format):

\"\"\"
{original_md}
\"\"\"

Here are the suggestions you must apply (Markdown format):

\"\"\"
{suggestions_md}
\"\"\"

🔴 Important: Your output **must reflect every suggestion** above. Do not omit or ignore any suggestion.  
✅ Output ONLY the final, fully revised Markdown document. Do NOT include explanations, notes, or commentary.
"""



def analyze_document(url):
    """Main driver function to analyze and revise a MoEngage documentation article."""

    # Step 1: Fetch and extract main content from article
    html_content, error = fetch_article_html(url)
    if error:
        print(error)
        return

    # Step 2: Convert to markdown and remove images
    markdown_text = html_to_markdown(html_content)
    markdown_text = replace_image_markdown(markdown_text)

    # print("✅ Extracted Markdown (Preview):\n")
    # print(markdown_text)

     # Step 3: Run Gemini Analyzer (Agent 1)
    prompt = build_analysis_prompt(url, markdown_text)
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[prompt]
    )
    suggestions_markdown = response.text

    # print("\n📄 Gemini Suggestions (Markdown):\n")
    # print(suggestions_markdown)


     # Step 4: Run Gemini Revision Agent (Agent 2)
    revision_prompt = build_revision_prompt(markdown_text, suggestions_markdown)
    revised_response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=[revision_prompt]
    )

    revised_markdown = revised_response.text
    # print("\n📄 Final Revised Markdown Article:\n")
    # print(revised_markdown)



     # Step 5: Save all versions to output folder
    slug = url.split("/")[-1]  # get slug from URL
    folder = "output"
    os.makedirs(folder, exist_ok=True)

    with open(f"{folder}/{slug}__original.md", "w", encoding="utf-8") as f:
        f.write(markdown_text)

    with open(f"{folder}/{slug}__suggestions.md", "w", encoding="utf-8") as f:
        f.write(suggestions_markdown)

    with open(f"{folder}/{slug}__revised.md", "w", encoding="utf-8") as f:
        f.write(revised_markdown)

    print(f"\n✅ Files saved to `./{folder}/` as:")
    print(f"   - {slug}__original.md")
    print(f"   - {slug}__suggestions.md")
    print(f"   - {slug}__revised.md")


def is_valid_moengage_url(url):
    """
    Validate that the given URL matches MoEngage Help Center article format.

    Args:
        url (str): Input URL.

    Returns:
        bool: True if URL is valid, False otherwise.
    """
    pattern = r"^https:\/\/help\.moengage\.com\/hc\/en-us\/articles\/[\d]+-.*"
    return re.match(pattern, url)

if __name__ == "__main__":
    print("🔗 Enter a MoEngage documentation article URL to analyze and revise:")
    input_url = input("URL: ").strip()

    if not is_valid_moengage_url(input_url):
        print("❌ Invalid URL. Please enter a URL in the format:")
        print("   https://help.moengage.com/hc/en-us/articles/[article-id]-[slug]")
    else:
        analyze_document(input_url)
