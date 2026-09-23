import ollama
response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":"your answer should be for 5 year old kid."
        },
        {
            "role": "user",
            "content": "What is AI?"
        }
    ]
)
print(response["message"]["content"])
