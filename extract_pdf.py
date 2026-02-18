from pdfminer.high_level import extract_text
import sys

try:
    text = extract_text("My resume.pdf")
    with open("resume_text_utf8.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extraction complete to resume_text_utf8.txt")
except Exception as e:
    print(f"Error extracting text: {e}")
