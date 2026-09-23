import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "Give Definition of AI.3 Types of AI with examples."
        }
    ]

)
