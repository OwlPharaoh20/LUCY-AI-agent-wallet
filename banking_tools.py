# Custom tools (send money, check balance etc)
# Simulated tool functions to represent MCP banking APIs

# banking_tools.py

def check_balance(_input: str = "") -> str:
    """
    Simulates a balance check.
    Returns result in a format that's easier for LLM to parse.
    """
    return "Final Answer: Your account balance is ₦13,500.00"

def send_money(input_str: str) -> str:
    """
    Simulates sending money.
    Expected input: 'Send ₦2000 to John'
    """
    return f"✅ Successfully sent money: {input_str}"

def get_transaction_history(_input: str = "") -> str:
    """Simulates recent transaction history. Accepts dummy input."""
    return (
        "Final Answer: 📋 Recent Transactions:\n"
        "- Sent ₦2000 to John\n"
        "- Received ₦500 from Alice"
    )