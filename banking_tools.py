# Custom tools (send money, check balance etc)
# Simulated tool functions to represent MCP banking APIs

# banking_tools.py
from logger import logger
from database import SessionLocal, Transaction

def check_balance(_input: str = "") -> str:
    logger.info("Checking account balance")
    return "Final Answer: Your account balance is ₦13,500.00"

def send_money(input_str: str) -> str:
    logger.info(f"Sending money: {input_str}")

    # Simulate parsing amount and recipient
    try:
        parts = input_str.split(" to ")
        amount = parts[0].replace("Send ", "").strip()
        recipient = parts[1].strip()

        # Save to DB
        session = SessionLocal()
        txn = Transaction(action="send", amount=amount, recipient=recipient)
        session.add(txn)
        session.commit()
        session.close()

        return f"Final Answer: ✅ Sent {amount} to {recipient}"
    except Exception as e:
        logger.error(f"Failed to process send_money: {str(e)}")
        return "Final Answer: ❌ Could not process transaction"

def get_transaction_history(_input: str = "") -> str:
    logger.info("Fetching transaction history")

    session = SessionLocal()
    txns = session.query(Transaction).order_by(Transaction.timestamp.desc()).limit(5).all()
    session.close()

    if not txns:
        return "Final Answer: 📋 No recent transactions found."

    history = "\n".join([f"- Sent {txn.amount} to {txn.recipient}" for txn in txns])
    return f"Final Answer: 📋 Recent Transactions:\n{history}"
