# 🎓 AI Powered Lecture Voice → Notes Generator

An AI-powered web application that converts lecture audio into structured academic notes and summaries using **Speech Recognition + Generative AI**.

This tool helps students automatically transform classroom recordings, seminars, and online lectures into well-organized study notes.

---

# 📌 Project Overview

Students often struggle to write notes while listening to lectures. Important points may be missed, especially during fast-paced teaching sessions.

This project solves that problem by combining:

* 🎤 Speech-to-Text (Whisper AI)
* 🧠 AI Notes Generation (Gemini API)
* 📝 Structured Academic Formatting
* 📚 Exam-Focused Summaries

Users can upload or record lecture audio and instantly receive clean, revision-ready notes.

---

# 🚀 Features

✅ Upload lecture recordings
✅ Live voice recording
✅ Automatic transcription
✅ Timestamped transcripts
✅ AI-generated lecture notes
✅ Key concepts & definitions extraction
✅ Exam important points
✅ Quick revision bullets
✅ Custom summary tone & length
✅ Download notes & summary

---

# 🧠 How It Works

1. User uploads or records lecture audio
2. Audio converts to WAV format
3. Whisper AI transcribes speech → text
4. Transcript sent to Gemini AI
5. AI generates structured lecture notes
6. Notes + summary displayed & downloadable

---

# 🏗️ System Architecture

```
Audio Input
   ↓
Audio Conversion (FFmpeg / Pydub)
   ↓
Speech-to-Text (Whisper)
   ↓
Transcript Processing
   ↓
Gemini AI Prompting
   ↓
Lecture Notes + Summary
   ↓
Download / View
```

---

# 📂 Project Structure

```
ai-lecture-notes-generator/
│
├── app.py              # Streamlit UI
├── ai_notes.py         # Gemini Notes Generator
├── stt.py              # Whisper Transcription
├── utils.py            # File + Audio Utilities
├── requirements.txt   # Python Dependencies
├── packages.txt       # System Packages (FFmpeg)
├── uploads/           # Temporary Audio Storage
└── README.md
```

---

# ⚙️ Technologies Used

| Technology | Purpose            |
| ---------- | ------------------ |
| Streamlit  | Web App UI         |
| Whisper AI | Speech Recognition |
| Gemini API | Notes Generation   |
| Python     | Backend Logic      |
| Pydub      | Audio Conversion   |
| FFmpeg     | Audio Processing   |

---

# 🖥️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/ai-lecture-notes-generator.git
cd ai-lecture-notes-generator
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Install FFmpeg

### Ubuntu / Colab

```bash
apt install ffmpeg
```

### Windows

1. Download FFmpeg
2. Extract
3. Add to PATH

---

## 4️⃣ Add Gemini API Key

### Linux / Mac

```bash
export GEMINI_API_KEY=your_api_key
```

### Windows

```bash
set GEMINI_API_KEY=your_api_key
```

---

LECTURE NOTES

1. Topic Overview
2. Key Concepts
3. Definitions
4. Important Explanations
5. Examples
6. Exam Points
7. Revision Points
# 🎯 Use Cases

* College lectures
* Online classes
* YouTube study videos
* Seminars & workshops
* Research discussions
* Exam revision
# 🌐 Deployment

You can deploy using:

* Streamlit Cloud
* Render
* Railway
* Hugging Face Spaces

Make sure to add:

```
packages.txt → ffmpeg
```

And set environment variable:

```
GEMINI_API_KEY
```

