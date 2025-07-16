# main.py
from agent import run_agent
from fastapi import FastAPI
import uvicorn
import sys

app = FastAPI()

@app.get("/wallet")
def run_wallet_agent(prompt: str):
    """Handles HTTP prompt."""
    return {"response": run_agent(prompt)}

# 🔥 CLI fallback logic
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run in CLI mode
        prompt = " ".join(sys.argv[1:])
        print("🧠 Lucy's Response:")
        print(run_agent(prompt))
    else:
        # Start API server normally
        uvicorn.run("main:app", port=8000, reload=True)

