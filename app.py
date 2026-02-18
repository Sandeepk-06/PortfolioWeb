import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize Groq Client
# WARNING: In production, use environment variables for API keys.
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable not set")
client = Groq(api_key=GROQ_API_KEY)

# Load Resume Data for Context
def get_resume_context():
    try:
        with open('resume_text_utf8.txt', 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading resume file: {e}")
        return "Resume data not available."

RESUME_CONTEXT = get_resume_context()

@app.route('/')
def home():
    resume_data = {
        "name": "SANDEEP KUMAR PRADHAN",
        "role": "Graphic Designer",
        "contact": {
            "email": "sandeep.otaku@gmail.com",
            "phone": "9451953321",
            "location": "Gosaninuagaoan, Berhampur, Ganjam, Odisha"
        },
        "summary": "I’m a graphic designer who loves turning ideas into visual stories. My passion is creating clean, creative, and meaningful designs that connect brands with people.",
        "skills": [
            "Illustration Design",
            "Social Media Optimization",
            "Coding"
        ],
        "education": [
            {
                "degree": "B.Tech",
                "institution": "N.I.S.T University",
                "year": "Current"
            },
            {
                "degree": "12th",
                "institution": "K.C. Public School",
                "year": "Completed"
            },
            {
                "degree": "10th",
                "institution": "K.C. Public School",
                "year": "Completed"
            }
        ],
        "experience": [
            {
                "role": "Graphic Designer",
                "description": "I have hands-on experience in graphic design and visual content creation, focusing on creating clean, modern designs that communicate ideas clearly and effectively. My work includes designing social media creatives, posters, and branding materials that help pages and small brands improve their online presence. I also have experience with content layout, typography, and visual hierarchy, ensuring designs are visually appealing and functional. Through these projects, I’ve developed a strong understanding of audience-focused design and how visuals can drive engagement."
            }
        ]
    }
    return render_template('index.html', resume=resume_data)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    system_prompt = f"""
    You are an AI assistant for Sandeep Kumar Pradhan's portfolio website.
    Your goal is to answer questions about Sandeep based strictly on his resume data provided below.
    
    RESUME DATA:
    {RESUME_CONTEXT}
    
    INSTRUCTIONS:
    - Answer politely and professionally.
    - If the answer is not in the resume, say "I don't have that information in the resume."
    - Keep answers concise.
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            model="llama-3.1-8b-instant",
        )
        bot_response = chat_completion.choices[0].message.content
        return jsonify({"response": bot_response})
    except Exception as e:
        print(f"Groq API Error: {e}")
        return jsonify({"error": "Failed to process request"}), 500

if __name__ == '__main__':
    app.run(debug=True)
