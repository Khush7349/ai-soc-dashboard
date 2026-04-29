import os
import requests
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
def explain(log, model=DEFAULT_MODEL, temperature=0.2, timeout=30):
    prompt = f"""
You are a cybersecurity analyst.
Task:
1) Explain why the following network activity is suspicious (if it is).
2) Identify likely attack type (if applicable).
3) Suggest 2-4 concrete mitigation steps.
Be concise. Reference fields like IP, bytes, protocol when relevant.
Log:
{log}
Answer:
"""
    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": temperature
                }
            },
            timeout=timeout
        )
        res.raise_for_status()
        data = res.json()
        if "response" not in data:
            return "LLM Error: Invalid response format"
        return data["response"].strip()
    except requests.exceptions.Timeout:
        return "LLM Error: Request timed out"
    except requests.exceptions.ConnectionError:
        return "LLM Error: Cannot connect to Ollama"
    except requests.exceptions.HTTPError as e:
        code = e.response.status_code if e.response else "Unknown"
        return f"LLM Error: HTTP {code}"
    except Exception as e:
        return f"LLM Error: {str(e)}"