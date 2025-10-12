
<h1>🎙️ AI Meeting Summarizer</h1>
<p>A modern web application that transforms meeting audio into <strong>accurate transcripts</strong> and <strong>intelligent, action-oriented summaries</strong> using a dual-AI model architecture.</p>

<div class="badges" align="center">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=for-the-badge&logo=python" />
    <img src="https://img.shields.io/badge/Streamlit-1.29.0-FF4B4B.svg?style=for-the-badge&logo=streamlit" />
    <img src="https://img.shields.io/badge/OpenAI_Whisper-orange?style=for-the-badge&logo=openai" />
    <img src="https://img.shields.io/badge/Google_Gemini-1473E6?style=for-the-badge&logo=google&logoColor=white" />
</div>


<h2>✨ Key Features</h2>
<ul>
    <li><strong>Dual AI Integration:</strong> OpenAI Whisper for accurate speech-to-text, Google Gemini for intelligent summarization.</li>
    <li><strong>Action-Oriented Output:</strong> Extracts key decisions and actionable tasks.</li>
    <li><strong>Comparative Side-by-Side View:</strong> Displays full transcript and AI summary for easy review.</li>
    <li><strong>Downloadable Artifacts:</strong> Download transcripts and summaries as text files.</li>
    <li><strong>Simple UI/UX:</strong> Single-page professional experience built with Streamlit.</li>
</ul>

<h2>⚙️ Tech Stack</h2>
<table>
    <tr>
        <th>Category</th>
        <th>Technology & Details</th>
    </tr>
    <tr>
        <td>Backend</td>
        <td>Python, Streamlit</td>
    </tr>
    <tr>
        <td>ASR Model</td>
        <td>OpenAI Whisper (whisper library)</td>
    </tr>
    <tr>
        <td>LLM Model</td>
        <td>Google Gemini (gemini-2.5-flash)</td>
    </tr>
    <tr>
        <td>Dependencies</td>
        <td>numpy, ffmpeg-python, python-dotenv</td>
    </tr>
    <tr>
        <td>Environment</td>
        <td>.env for API keys (Google Gemini)</td>
    </tr>
</table>

<h2>📖 Setup & Installation</h2>
<h3>1. Prerequisites</h3>
<p>Python 3.8+ and ffmpeg command-line tool installed.</p>

<h3>2. Get Your API Key</h3>
<p>Obtain a <strong>Google Gemini API key</strong> from <a href="https://ai.google/">Google AI Studio</a>.</p>

<h3>3. Environment Setup</h3>
<p>Create a <code>.env</code> file in the root directory:</p>
<pre>
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY_HERE"
</pre>

<h3>4. Install Dependencies</h3>
<pre>pip install -r requirements.txt</pre>

<h3>5. Run the App</h3>
<pre>streamlit run app.py</pre>

<p>Upload your meeting audio, click <strong>Generate Transcript & Summary</strong>, and download the transcript and summary.</p>

<h2>💡 Usage Tips</h2>
<ul>
    <li>Clear audio improves transcription accuracy.</li>
    <li>Longer meetings may take more time to process.</li>
    <li>Minimize background noise for best results.</li>
</ul>

<h2>🛠️ Future Improvements</h2>
<ul>
    <li>Real-time meeting transcription</li>
    <li>Multi-language support</li>
    <li>Integration with Google Calendar & Microsoft Teams</li>
    <li>Export summaries as PDF or Markdown</li>
</ul>


</div>
</body>

