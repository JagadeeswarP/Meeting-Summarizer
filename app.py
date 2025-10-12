import os
import tempfile
import streamlit as st
import whisper
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GEMINI_API_KEY:
    st.error("Gemini API key not found. Set GOOGLE_API_KEY in your .env.")
    st.stop()
try:
    genai.configure(api_key=GEMINI_API_KEY)
except Exception as e:
    st.error(f"Error configuring Gemini: {e}")
    st.stop()

@st.cache_resource
def load_whisper_model():
    loading_container = st.empty()
    loading_container.info("Loading Whisper model... This may take a moment.")
    model = whisper.load_model("base")
    loading_container.empty()
    return model

def transcribe_audio(audio_path):
    model = load_whisper_model()
    info_container = st.empty()
    info_container.info(f"Transcribing {os.path.basename(audio_path)}...")
    try:
        result = model.transcribe(audio_path)
        info_container.empty()
        st.success("Transcription complete ✅")
        return result['text']
    except Exception as e:
        info_container.empty()
        st.error(f"Error during transcription: {e}")
        return None

def summarize_transcript(transcript):
    summary_container = st.empty()
    summary_container.info("Generating AI summary...")
    prompt = f"""
    Summarize the following meeting transcript into key decisions and action items.
    Structure your response with a "Summary" section and an "Action Items" section using bullet points.

    Transcript:
    ---
    {transcript}
    ---
    """
    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        summary_container.empty()
        st.success("Summary generated ✅")
        return response.text
    except Exception as e:
        summary_container.empty()
        st.error(f"Error during summarization: {e}")
        return "Error: Could not generate summary."

st.set_page_config(page_title="Modern Meeting Summarizer", layout="wide", page_icon="🎙️")
st.markdown(
    """
    <h1 style='text-align: center; color: #4B8BBE;'>🎙️ Modern Meeting Summarizer</h1>
    <p style='text-align: center; font-size: 16px; color: #555;'>Upload your meeting audio to generate a clean transcript and AI-powered summary</p>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.markdown("### 📂 Upload Audio File")
    uploaded_file = st.file_uploader("Supported formats: MP3, WAV, M4A, FLAC", type=['mp3', 'wav', 'm4a', 'flac'])
    
    if uploaded_file:
        st.audio(uploaded_file, format='audio/mpeg')
        generate_btn = st.button("✨ Generate Transcript & Summary")

        if generate_btn:
            with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{uploaded_file.name}") as tmp_file:
                tmp_file.write(uploaded_file.read())
                audio_path = tmp_file.name
            
            with st.spinner("Processing audio... ⏳"):
                transcript = transcribe_audio(audio_path)
                summary = summarize_transcript(transcript) if transcript else None
            
            os.remove(audio_path)


            if transcript:
                st.session_state['transcript'] = transcript
            if summary:
                st.session_state['summary'] = summary


if 'transcript' in st.session_state and 'summary' in st.session_state:
    st.markdown("### 💡 Summary & Action Items")
    

    st.markdown(
        f"<div style='font-size: 21px; font-weight: 500;'>{st.session_state['summary']}</div>", 
        unsafe_allow_html=True
    )
    
    st.download_button(
        "⬇️ Download Summary", 
        st.session_state['summary'], 
        file_name="meeting_summary.txt"
    )

    st.markdown("---")

    st.markdown("### 📝 Full Transcript")
    
    st.markdown("""
        <style>
        /* Target the textarea widget specifically by its generated class if possible, 
           or globally for textareas for simplicity */
        .stTextArea textarea {
            font-size: 21px !important; 
            font-weight: 350 !important; /* Standard weight for readability in a large block of text */
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.text_area("Transcript", st.session_state['transcript'], height=500)
    
    st.download_button(
        "⬇️ Download Transcript", 
        st.session_state['transcript'], 
        file_name="meeting_transcript.txt"
    )

# --- Sidebar ---
st.sidebar.header("About")
st.sidebar.info(
    """
    This application uses:
    - **OpenAI Whisper** for high-quality audio transcription
    - **Google Gemini** for AI summarization

    Upload your meeting audio to instantly get a clean transcript and actionable summary.
    """
)