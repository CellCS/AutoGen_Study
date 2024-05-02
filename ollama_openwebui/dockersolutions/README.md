# Ollam webui

## Ollama in docker 

docker exec -it ollama ollama pull llama3
docker exec -it ollama ollama list



curl http://localhost:11434/api/generate -d '{
"model": "llama3",
"prompt": "why the sky is blue?",
"stream": false,
"options": {
"seed": 123,
"top_k": 20,
"top_p": 0.9,
"temperature": 0.1
}
}
