from dotenv import load_dotenv

load_dotenv()

# initialize a LangChain chat model with just a string
# ensure provider package is installed for models that we will be using

import ollama
from langsmith import traceable
# Tool message - contains tool results
# System message - general information about the LLM
# Human message - user input

MAX_ITERATIONS=10
MODEL="qwen2.5"
#

@traceable(run_type="tool")
def get_product_price(name: str) -> float:
    """Look up the price of a product in the catalog"""
    print(f"    >> Executing get_product_price(name='{name}')")
    prices = {"laptop": 1299.99, "headphones": 149.95, "keyboard": 89.50}
    return prices.get(name, 0)

@traceable(run_type="tool")
def apply_discount(price: float, discount_tier: str) -> float:
    """Apply a discount tier to a price and return the final price"""
    print(f"    >> Executing apply_discount(price={price}, discount_tier='{discount_tier}')")
    discount_percentages = {"bronze": 5, "silver": 12, "gold": 23}
    discount = discount_percentages.get(discount_tier, 0)
    return round(price * (1 - (discount/100)), 2)

# --- Agent Loop ---
@traceable(name="LangChain Agent Loop")
def run_agent(question:str):
    tools = [get_product_price, apply_discount]
    tools_dict = {t.name: t for t in tools}

    llm = init_chat_model(f"ollama:{MODEL}", temperature=0)
    llm_with_tools = llm.bind_tools(tools)

    print(f"Question: {question}")
    print("=" * 60)

    messages=[
        SystemMessage(content=(
            "You're a helpful shopping assistant"
            "You have access to a product catalog tool"
            "and a discount tool.\n\n"
            "STRICT RULES - you must follow these exactly:\n"
            "1. NEVER guess or assume any product price. "
            "You MUST call get_product_price first to get a real price.\n"
            "2. Only call apply_discount AFTER you have received "
            "a price from get_product_price. Pass the exact price "
            "returned by get_product_price - do NOT pass a made-up number.\n"
            "3. NEVER calculate discounts yourself using math. "
            "Always use the apply_discount tool.\n"
            "4. If the user does not specificy a discount tier, "
            "ask them which tier to use - do NOT assume one.\n"
            "5. If the user enters an invalid discount tier, " \
            "please inform them to provide the valid values only"

        )),
        HumanMessage(content=question)
    ]

    for iteration in range(1, MAX_ITERATIONS + 1):
        print(f"\n--- Iteration {iteration} ---")

        """
            ai_message is either going to return tool call or final answer
            if there's no tool call, we can access its content as the final answer
        """
        ai_message = llm_with_tools.invoke(messages)
        tool_calls = ai_message.tool_calls

        if not tool_calls:
            print(f"\nFinal Answer: {ai_message.content}")
            return ai_message.content

        # Run tool
        tool_call = tool_calls[0]
        tool_name = tool_call.get("name", "")
        tool_args = tool_call.get("args", {})
        tool_call_id = tool_call.get("id", "")

        tool_func = tools_dict[tool_name]

        if tool_func is None:
            raise ValueError("Tool '{tool_name}' not found")

        observation = tool_func.invoke(tool_args)

        print(f"   [Tool Result] {observation}")

        messages.append(ai_message)
        messages.append(ToolMessage(content=observation, tool_call_id=tool_call_id))
if __name__ == "__main__":
    print("Hello LangChain Agent (.bind_tools)!")
    print()
    result = run_agent(question="What is the price of a laptop after applying a platinum discount?")