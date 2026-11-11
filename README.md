# Gemini LLM API Integration

## Overview
A Python application that integrates Google's Gemini API to send a prompt to a Large Language Model (LLM) and display its generated response. The API key is securely managed using environment variables.

## Technologies Used
- Python
- Google Gemini API
- Google Gen AI SDK
- python-dotenv
- Git and GitHub

## Project Structure
```text
llm-hello-integration/
├── hello.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## Setup Instructions

**1. Clone the repository**
```bash
git clone YOUR_REPOSITORY_URL
cd llm-hello-integration
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure API key**

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key
```

Generate your API key through [Google AI Studio](https://aistudio.google.com/).

**5. Run the application**
```bash
python hello.py
```

## Application Workflow
1. Load environment variables using python-dotenv.
2. Retrieve the Gemini API key.
3. Initialize the Gemini client.
4. Send a prompt through the Gemini API.
5. Display the generated response.

## Security
- Store API keys in `.env`.
- Exclude `.env` and `venv/` using `.gitignore`.
- Never commit API credentials to GitHub.

## Testing
Successfully executed the Python script and verified that the Gemini API generates and returns a response.

## Git Workflow
Created a feature branch, committed and pushed changes, raised a Pull Request for review, and merged the approved changes into the main branch.

## Author
Developed as part of an internship task on Python tooling, GitHub collaboration, and LLM API integration.
