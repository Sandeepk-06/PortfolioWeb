from groq import Groq

API_KEY = "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"

try:
    client = Groq(api_key=API_KEY)
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello"}],
        model="llama-3.1-8b-instant",
    )
    print("API Key is VALID. Response:", chat_completion.choices[0].message.content)
except Exception as e:
    print("API Key verification FAILED. Error:", e)
