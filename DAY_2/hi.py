import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is ML?"
        }
    ]
)
print(response["message"]["content"])
