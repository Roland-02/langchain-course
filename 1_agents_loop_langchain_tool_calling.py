from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage

MAX_ITERATIONS = 10
MODEL = "qwen3:1.7b"

# --- Tools ----

@tool
def get_product_price(product: str) -> float:
    """Get the price of a product."""
    prices = {"laptop": 999.99, "smartphone": 499.99, "tablet": 299.99}
    return prices.get(product, 0)

