# Lucy – AI Fintech Wallet CLI

Lucy is a command-line AI wallet assistant built using Python, LangChain, OpenAI, and FastAPI.
It interacts with simulated Nigerian banking APIs using MCP servers to perform balance checks, send/receive money, and view transaction history.

## Features
- Check balance
- Send and receive money
- Transaction history (via MySQL)
- Uses MCP tool calling and LLM logic


#Commands
To Run server = uvicorn main:app --reload

#Prompts 
sample send money url/prompt
http://localhost:8000/wallet?prompt=Send ₦1000 to Aisha

to prompt via cli, use this command : python main.py + prompt ( send money, check balance, transaction history)

