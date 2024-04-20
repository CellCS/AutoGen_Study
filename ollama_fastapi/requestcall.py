import json
import requests
urls =["http://localhost:11434/api/generate"]
headers = {
    "Content-Type": "application/json"
}
url = urls[0]
payload = {
    "model": "llama3",
    "prompt": "Why is the sky blue?",
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
if response.status_code == 200:
    print(response.text)
else:
    print("error:", response.status_code, response.text)
