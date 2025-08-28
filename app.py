# ----------------------------------------------------------------------
# FILE: app.py (Your main application file)
# ----------------------------------------------------------------------
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image
import docx
import pptx
import openpyxl
import io

# --- Configuration ---
load_dotenv()
try:
    # It's safer to check for the key and handle its absence
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        st.error("GOOGLE_API_KEY not found. Please set it in your .env file.")
        st.stop()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Error configuring the API: {e}")
    st.stop()

# --- Helper Functions ---
def extract_text_from_file(uploaded_file):
    """Extracts text from various file types."""
    try:
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        if file_extension == ".docx":
            return "\n".join([para.text for para in docx.Document(uploaded_file).paragraphs])
        elif file_extension == ".pptx":
            prs = pptx.Presentation(uploaded_file)
            return "\n".join([shape.text for slide in prs.slides for shape in slide.shapes if hasattr(shape, "text")])
        elif file_extension == ".xlsx":
            workbook = openpyxl.load_workbook(uploaded_file)
            return "\n".join([" ".join(str(cell) if cell is not None else "" for cell in row) for sheet in workbook.worksheets for row in sheet.iter_rows(values_only=True)])
        elif file_extension == ".sql":
            return uploaded_file.getvalue().decode("utf-8")
        return "Unsupported file type for text extraction."
    except Exception as e:
        return f"Error extracting text: {e}"

# --- System Prompts for Different Tools ---
SYSTEM_PROMPTS = {
    "General Assistant": "You are a helpful digital marketing assistant.",
    "Ad Copy Generator": "You are an expert copywriter. Your task is to create compelling ad copy based on the user's request. Focus on headlines, body text, and calls-to-action.",
    "Social Media Post Generator": "You are a social media manager. Create engaging posts for the specified platform, including relevant hashtags and a suitable tone.",
    "Email Campaign Writer": "You are an email marketing specialist. Write effective marketing emails with strong subject lines and clear calls-to-action.",
    "SEO Keyword Analyst": "You are an SEO expert. Generate relevant short-tail and long-tail keywords for the user's topic.",
    "Content Improver": "You are an expert content editor. Rewrite and improve the user's text based on their stated goal (e.g., make it more persuasive, simplify it).",
    "Digital Marketing Analyst": "You are a digital marketing analyst. Your role is to analyze data, summarize reports, and provide actionable insights."
}

# --- Streamlit App ---
st.set_page_config(page_title="Marketing AI Chat", page_icon="🚀", layout="wide")

st.title("🚀 AI Digital Marketing Assistant")

# --- Sidebar ---
with st.sidebar:
    st.header("Tools & Settings")
    
    # Tool selection
    selected_tool = st.selectbox("Choose your marketing tool:", list(SYSTEM_PROMPTS.keys()))
    
    st.markdown("---")
    
    # File Uploader
    st.subheader("Upload a File")
    uploaded_file = st.file_uploader(
        "Upload an image, document, or audio file for context.",
        type=['png', 'jpg', 'jpeg', 'docx', 'pptx', 'xlsx', 'sql', 'wav', 'mp3', 'ogg']
    )

    st.markdown("---")

    # Clear Chat Button with Confirmation
    if 'confirm_clear' not in st.session_state:
        st.session_state.confirm_clear = False

    if st.button("Clear Chat History"):
        st.session_state.confirm_clear = True

    if st.session_state.confirm_clear:
        st.warning("Are you sure you want to clear the chat history?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, Clear It"):
                st.session_state.messages = []
                st.session_state.confirm_clear = False
                st.rerun()
        with col2:
            if st.button("Cancel"):
                st.session_state.confirm_clear = False
                st.rerun()


# --- Chat History Initialization ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        # Display images if they exist
        if "image" in message:
            st.image(message["image"], width=200)
        # Display text content
        if "content" in message:
            st.markdown(message["content"])

# --- Chat Input and Logic ---
if prompt := st.chat_input("What can I help you with today?"):
    # --- Handle File Upload ---
    user_message = {"role": "user"}
    
    # Process uploaded file if it exists
    if uploaded_file is not None:
        file_extension = os.path.splitext(uploaded_file.name)[1].lower()
        
        if file_extension in ['.png', '.jpg', '.jpeg']:
            image = Image.open(uploaded_file)
            user_message["image"] = image
            user_message["content"] = prompt
        elif file_extension in ['.wav', '.mp3', '.ogg']:
            st.info("Transcribing audio... (This is a placeholder for a real transcription service)")
            # In a real app, you would call a speech-to-text API here
            audio_text = f"Audio file '{uploaded_file.name}' was uploaded. The user's prompt is: {prompt}"
            user_message["content"] = audio_text
        else:
            extracted_text = extract_text_from_file(uploaded_file)
            user_message["content"] = f"Context from file '{uploaded_file.name}':\n---\n{extracted_text}\n---\nUser's question: {prompt}"

    else: # No file uploaded
        user_message["content"] = prompt
        
    st.session_state.messages.append(user_message)
    with st.chat_message("user"):
        if "image" in user_message:
            st.image(user_message["image"], width=200)
        if "content" in user_message:
            st.markdown(user_message["content"])

    # --- Generate AI Response ---
    with st.chat_message("assistant"):
        with st.spinner("🤖 Thinking..."):
            # Construct the full prompt with system message and history
            full_prompt = [SYSTEM_PROMPTS[selected_tool]]
            
            # Add chat history to the prompt for context
            for msg in st.session_state.messages:
                # For simplicity, we'll just pass the text content to the model for now
                if "content" in msg:
                    full_prompt.append(f"{msg['role']}: {msg['content']}")

            # Prepare content for the model (handles images)
            model_input = []
            if "image" in user_message:
                model_input.append(user_message["image"])
            model_input.append("\n".join(full_prompt))

            try:
                response = model.generate_content(model_input)
                response_text = response.text
            except Exception as e:
                response_text = f"Sorry, an error occurred: {e}"
            
            st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})
