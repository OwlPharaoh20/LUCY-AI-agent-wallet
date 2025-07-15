#Mai entry Point 
#CLI interface sing FASTapi and langchain to communicate Lucy

from fastapi import FastAPI
from agent import run_agent
import uvicorn

app = FastAPI()

@app.get("/wallet")
def run_wallet_agent(prompt: str):
    """
    Accepts a prompt from the user and sends it to the agent
    Example:  http://localhost:8000/wallet?prompt=Check my balance

    
    """

    response = run_agent(prompt)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

