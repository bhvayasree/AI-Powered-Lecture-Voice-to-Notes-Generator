from google import genai
import os

def generate_notes_summary(transcript, tone, length):

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not set. Add it inside Streamlit Secrets."
        )

    try:
        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an AI Lecture Notes Generator.

Analyze the lecture transcript and create well-structured academic notes useful for students.

--------------- LECTURE TRANSCRIPT ---------------
{transcript}
--------------- END TRANSCRIPT -------------------

Instructions:

Create notes using this structure:

LECTURE NOTES:

1. Topic Overview
2. Key Concepts
3. Definitions / Terminologies
4. Important Explanations
5. Examples / Case Studies
6. Formulas / Data (if any)
7. Exam Important Points
8. Quick Revision Points

SUMMARY:

Write a {tone} summary in {length} length suitable for last-minute revision.

Rules:
- Use bullet points
- Use simple student-friendly language
- Highlight exam-important content
- Do NOT add extra headings
- Respond ONLY in the given format
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        full_text = response.text

        # Parsing output
        if "LECTURE NOTES:" in full_text and "SUMMARY:" in full_text:
            notes = full_text.split("LECTURE NOTES:")[1].split("SUMMARY:")[0].strip()
            summary = full_text.split("SUMMARY:")[1].strip()
        else:
            notes = full_text
            summary = "Summary could not be generated."

        return notes, summary

    except Exception as e:
        raise RuntimeError(f"Gemini API failed: {e}")
