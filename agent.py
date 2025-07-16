 # LangChain agent logic

# Core AI agent that uses OpenAI + LangChain + Tool calling

from langchain.agents import initialize_agent, Tool
from langchain_community.chat_models import ChatOpenAI
from banking_tools import check_balance, send_money, get_transaction_history
from dotenv import load_dotenv
import os 
import time
from logger import logger

# Load secrets from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


# Initialize the LLM
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2, openai_api_key=openai_api_key)

# Define the tools available to the agent
tools = [
    Tool(
        name="CheckBalance",
        func=check_balance,
        description="Get current bank account balance"
    ),
    Tool(
        name="SendMoney",
        func=send_money,
        description="Send money to someone. Expected input format: 'Send ₦2000 to Tolu'"
    ),
    Tool(
        name="TransactionHistory",
        func=get_transaction_history,
        description="View recent transactions"
    )
]

# Build the agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="chat-zero-shot-react-description",  # ReAct framework
    verbose=True,
    handle_parsing_errors=True
)

def run_agent(prompt: str) -> str:
    max_retries = 2
    for attempt in range(max_retries + 1):
        try:
            logger.info(f"Running agent with prompt: {prompt}")
            return agent.run(prompt)
        except Exception as e:
            logger.error(f"Attempt {attempt+1} failed: {str(e)}")
            time.sleep(1)
    return "Final Answer: Agent failed after multiple attempts."
    


    
