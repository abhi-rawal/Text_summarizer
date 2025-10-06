AI Text Summarizer (Intern Assignment Submission)
This project is a web application built with Streamlit and Python that uses the Google Gemini API to summarize any provided text into exactly three sentences, fulfilling Task 2 (Text Summarizer) and the Stretch Goal (Simple UI) of the intern assignment.

Part 1: Setup and Documentation Log (Required)
Technologies Used
Language: Python 3.10

AI API: Google Gemini API (gemini-2.5-flash model)

SDK: google-genai Python library

UI Framework (Stretch Goal): Streamlit

Detailed Development Log
Step

Action Taken

Result / Outcome

1. Project Setup

Installed Python, created GitHub repository, initialized requirements.txt, and created command-line script (summarizer.py).

Success. Environment ready.

2. Command-Line Fix

Troubleshooting ImportError: cannot import name 'genai' from 'google'. Uninstalled conflicting google packages (pip uninstall google -y, etc.) and reinstalled the correct google-genai SDK.

Success. Import error resolved (Demonstrated resourcefulness).

3. Command-Line Refinement

Refined the API call to use a strict System Instruction (enforcing "EXACTLY three concise sentences") to ensure compliance with the core constraint.

Success. The summarization logic was robust.

4. Stretch Goal: UI Integration

Added streamlit to requirements.txt and converted the project to a single-file web application, streamlit_app.py. Added UI components and custom CSS for a professional look.

Success. The application now features a simple, modern web GUI, completing the optional stretch goal.

5. File Name Troubleshooting

Encountered Error: File does not exist: streamlit_app.py in the terminal. The issue was a hidden .txt extension. Renamed the file correctly.

Success. File name issue resolved, demonstrating crucial troubleshooting skills.

Phase 2: Installation
Open Command Prompt/Terminal: Navigate to your project folder (C:\Users\hp\Desktop\text_summarizer\) using the cd command:

cd C:\Users\hp\Desktop\text_summarizer

Install Dependencies: Run the following command to install the required libraries:

pip install -r requirements.txt

Phase 3: Run the Application (Part 3 Stretch Goal)
Execution Command: Run the Streamlit application using this command:

streamlit run streamlit_app.py
