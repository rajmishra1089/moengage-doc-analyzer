# MoEngage Documentation Analyzer (Agent System)

This repository contains an intelligent agent-based system that analyzes and optionally revises MoEngage documentation articles. It uses Google's Gemini API to analyze clarity, structure, and completeness of documentation.

---


## 🔍 What It Does

1. **Takes a MoEngage Help Center URL** as input  
   (e.g., `https://help.moengage.com/hc/en-us/articles/12345678901234-Getting-Started-with-Flows`)

2. **Extracts and cleans article content**  
   - Removes scripts, styles, and images
   - Converts HTML to Markdown
   - Replaces screenshots with inline placeholders
  
- **Agent 1 (Documentation Analyzer)**: 
  - Fetches MoEngage help center articles
  - Converts HTML to Markdown (with image placeholders)
  - Analyzes clarity, structure, and completeness
  - Outputs actionable suggestions in Markdown format

- **Agent 2 (Optional: Documentation Rewriter)**: 
  - Uses suggestions from Agent 1
  - Automatically revises the original article
  - Outputs a revised Markdown version

## 📁 Output File Structure

For an article like `.../articles/123456-Using-Rich-Push`, the following files are generated in the `output/` folder:<br/>
output/<br/>
├── Using-Rich-Push__original.md<br/>
├── Using-Rich-Push__suggestions.md<br/>
├── Using-Rich-Push__revised.md



## 📦 Setup Instructions

1. **Clone the repository**<br/>
git clone https://github.com/rajmishra1089/moengage-doc-analyzer <br/>
cd moengage-doc-analyzer

2. **Install the dependencies**
pip install -r requirements.txt

3. **Set up your Gemini API key**
Create a .env file in the root directory with your Gemini API key:<br/>
GEMINI_API_KEY=your_google_gemini_api_key


🚀 **Running the Script**<br/>
**Start the program:**<br/>
python main.py<br/>

You'll be prompted to enter a MoEngage documentation article URL.<br/>
The system will:<br/>
Fetch and analyze the article<br/>
Apply the suggestions <br/>
Save all outputs to the output/ folder


📝 **Example Output**<br/>
Here's a preview of what's included in each generated file:<br/>
__original.md: Cleaned Markdown from the MoEngage article<br/>
__suggestions.md: Structured feedback on readability, structure, and clarity<br/>
__revised.md: Fully revised article incorporating all suggestions<br/>


👨‍💻 **Author**<br/>
Created by Raj Mishra as part of an LLM-based documentation analysis project.

