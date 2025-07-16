# Custom tools (send money, check balance etc)
# Simulated tool functions to represent MCP banking APIs

# banking_tools.py
from logger import logger
from database import SessionLocal, Transaction

def check_balance(_input: str = "") -> str:
    """
    Calculates real balance by subtracting all sent transaction amounts
    from the starting balance (₦1,000,000).
    """
    from logger import logger
    from database import SessionLocal, Transaction

    STARTING_BALANCE = 1_000_000  # ₦1,000,000

    try:
        logger.info("🔎 Calculating dynamic balance...")

        session = SessionLocal()
        txns = session.query(Transaction).all()
        session.close()

        # Sum all transaction amounts (convert ₦ values to integers safely)
        total_spent = 0
        for txn in txns:
            amount = txn.amount.replace("₦", "").replace(",", "").strip()
            try:
                total_spent += int(float(amount))
            except ValueError:
                logger.warning(f"❌ Invalid amount skipped: {txn.amount}")

        balance = STARTING_BALANCE - total_spent
        logger.info(f"🧮 Total spent: ₦{total_spent}, Balance: ₦{balance}")

        return f"Final Answer: Your current balance is ₦{balance:,}.00"

    except Exception as e:
        logger.error(f"💥 Failed to calculate balance: {str(e)}")
        return "Final Answer: ❌ Could not retrieve your balance."


def send_money(input_str: str) -> str:
    """
    Parses input like 'Send ₦1000 to Aisha' and saves it to DB.
    """
    from logger import logger
    from database import SessionLocal, Transaction

    logger.info(f"🟡 Starting send_money tool with input: {input_str}")

    try:
        # Parse input
        parts = input_str.replace("Send", "").split("to")
        if len(parts) != 2:
            raise ValueError("❌ Invalid format. Use: Send ₦amount to name")

        amount = parts[0].strip()
        recipient = parts[1].strip()

        logger.info(f"Parsed amount: {amount}, recipient: {recipient}")

        # DB Transaction
        session = SessionLocal()
        txn = Transaction(action="send", amount=amount, recipient=recipient)
        session.add(txn)
        session.commit()
        session.close()

        logger.info("✅ Transaction saved successfully to DB")

        return f"Final Answer: ✅ Sent {amount} to {recipient}"

    except Exception as e:
        logger.error(f"🚨 send_money failed: {str(e)}")
        return "Final Answer: ❌ Could not complete the transfer."


def get_transaction_history(_input: str = "") -> str:
    logger.info("Fetching transaction history")

    session = SessionLocal()
    txns = session.query(Transaction).order_by(Transaction.timestamp.desc()).limit(5).all()
    session.close()

    if not txns:
        return "Final Answer: 📋 No recent transactions found."

    history = "\n".join([f"- Sent {txn.amount} to {txn.recipient}" for txn in txns])
    return f"Final Answer: 📋 Recent Transactions:\n{history}"
