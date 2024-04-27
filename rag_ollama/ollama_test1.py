import ollama

# need install ollama, download llama3 "ollama pull llama3" run one model like "ollama run llama3"
# so ollama server is running at http://localhost:11434

response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'how many standards for clinical trials?',
  },
])
print(response['message']['content'])