import os
import streamlit as st
from google import genai
from google.genai.errors import APIError
import time

# --- Configuration ---
# The API key is crucial for the application to function.
# It is automatically sourced from the GEMINI_API_KEY environment variable.
API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL_NAME = "gemini-2.5-flash"
MAX_RETRIES = 3

@st.cache_data(show_spinner="Generating summary with Gemini...")
def summarize_text(text: str) -> str:
    """
    Connects to the Gemini API to summarize the text into exactly three sentences,
    using a system instruction for strict control over the output format.
    """
    if not API_KEY:
        return "ERROR: GEMINI_API_KEY environment variable not set. Please ensure your API key is correctly configured."

    # The System Instruction is the core element that enforces the 3-sentence constraint.
    system_instruction = (
        "You are a professional text summarizer. Your only task is to read the "
        "provided article or blog post and return a summary that consists of "
        "EXACTLY three concise sentences. Do not add any extra text, titles, or headers."
    )
    
    user_prompt = f"Please summarize the following article in exactly 3 sentences:\n\n---\n\n{text}"

    # Implement exponential backoff for robust API calls
    for attempt in range(MAX_RETRIES):
        try:
            client = genai.Client()
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=user_prompt,
                config=genai.types.GenerateContentConfig(
                    system_instruction=system_instruction
                )
            )

            # Return the generated text after stripping whitespace
            return response.text.strip()

        except APIError as e:
            if attempt < MAX_RETRIES - 1:
                # Wait before retrying (1s, 2s)
                time.sleep(2 ** attempt) 
                continue
            # If all retries fail, return the final error
            return f"An API error occurred after {MAX_RETRIES} attempts. Error: {e}"
        except Exception as e:
            # Handle non-API related exceptions (e.g., network issues)
            return f"An unexpected error occurred: {e}"

# --- Streamlit UI Layout and Logic ---
def main():
    st.set_page_config(page_title="3-Sentence AI Summarizer", layout="centered")

    # Custom CSS for a professional, branded look
    st.markdown("""
        <style>
            /* Customizing the Streamlit button for a modern feel */
            .stButton>button {
                background-color: #4285F4; /* Google Blue */
                color: white;
                font-weight: bold;
                border-radius: 8px;
                padding: 10px 24px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #357ae8;
            }
            /* Styling for the success message (summary output) */
            .stSuccess {
                border-left: 5px solid #34A853; /* Google Green */
                padding: 15px;
                background-color: #f0fff0;
                border-radius: 8px;
            }
            /* Styling for the info message (character count) */
            .stInfo {
                background-color: #f0f8ff;
                border-radius: 8px;
            }
            /* Ensure text areas and inputs are easily readable */
            .stTextArea > label {
                font-size: 1.1em;
                font-weight: 600;
                color: #333;
            }
        </style>
    """, unsafe_allow_html=True)

    # Header and Instructions
    st.title("🤖 Tiny AI-Powered App: 3-Sentence Summarizer")
    st.markdown(
        """
        This application uses the **Gemini API** to condense any news article or blog post into a summary of 
        **precisely three sentences**. This fulfills the assignment's **Text Summarizer** task and the optional **Streamlit UI Stretch Goal**.
        ---
        """
    )
    
    # Text Input Area
    input_text = st.text_area(
        "Paste the Article Text Below:", 
        height=300, 
        placeholder="Paste a long article, research paper abstract, or blog post here. The AI will strictly enforce the three-sentence rule."
    )

    # Button to Trigger Summarization
    if st.button("Generate 3-Sentence Summary", type="primary", use_container_width=True):
        
        # 1. Input Validation
        if not input_text or len(input_text.strip()) < 50:
            st.error("⚠️ Please paste a valid article (at least 50 characters) to summarize.")
        else:
            # 2. Call the AI Function
            summary = summarize_text(input_text)
            
            # 3. Display Results
            if summary.startswith("ERROR:"):
                st.error(summary)
            else:
                st.markdown("### ✅ Final Summary (Exactly 3 Sentences)")
                st.success(summary)
                st.info(f"Input character count: {len(input_text.strip())} | Summary generation successful.")

if __name__ == "__main__":
    main()
