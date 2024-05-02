# Open WebUI

Step 1: ollama is installed, and run a model
```
ollama run llama3
```

Step 2-localmodel: If Ollama is on your computer, install open-webui in a docker
```
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

Step 2-openAI: If Ollama is on your computer, install open-webui in a docker
```
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  -e OPENAI_API_BASE_URLS="https://api.openai.com/v1" \
  -e OPENAI_API_KEYS="<OPENAI_API_KEY_1>" \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

for multiple api service

```
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  -e OPENAI_API_BASE_URLS="https://api.openai.com/v1;https://api.mistral.ai/v1" \
  -e OPENAI_API_KEYS="<OPENAI_API_KEY_1>;<OPENAI_API_KEY_2>" \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Step 3:

```
http://localhost:3000
```

# Ollam webui

## Ollama in docker 

docker exec -it ollama ollama pull llama3
docker exec -it ollama ollama list

```
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
```


Reference:
[open-webui on github](https://github.com/open-webui/open-webui)