from swarm import Agent
from pprint import pprint


def process_refund(item_id, reason="NOT SPECIFIED"):
    """Refund an item. Refund an item. Make sure you have the item_id of the form item_... Ask for user confirmation before processing the refund."""
    print(f"[mock] Refunding item {item_id} because {reason}...")
    return "Success!"


def apply_discount():
    """Apply a discount to the user's cart."""
    print("[mock] Applying discount...")
    return "Applied discount of 11%"


triage_agent = Agent(
    name="Triage Agent",
    instructions="Determine which agent is best suited to handle the user's request, and transfer the conversation to that agent.",
)
sales_agent = Agent(
    name="Sales Agent",
    instructions="Be super enthusiastic about selling bees.",
)
refunds_agent = Agent(
    name="Refunds Agent",
    instructions="Help the user with a refund. If the reason is that it was too expensive, offer the user a refund code. If they insist, then process the refund.",
    functions=[process_refund, apply_discount],
)


def transfer_back_to_triage():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    print("[mock] Transferring back to triage agent...")
    return triage_agent


def transfer_to_sales():
    print("[mock] Transferring to sales agent...")
    return sales_agent


def transfer_to_refunds():
    print("[mock] Transferring to refunds agent...")
    return refunds_agent


triage_agent.functions = [transfer_to_sales, transfer_to_refunds]
sales_agent.functions.append(transfer_back_to_triage)
refunds_agent.functions.append(transfer_back_to_triage)


if __name__ == "__main__":
    from swarm import Swarm

    client = Swarm()
    response = client.run(
        agent=triage_agent,
        messages=[
            {"role": "user", "content": "Hi!"},
            {"role": "assistant", "content": "Hello, how can I help you today?"},
            #{"role": "user", "content": "I want to buy some bees."},
            {"role": "user", "content": "I want a refund for my order."},
        ],
        context_variables={"user_name": "John"},
    )
    pprint(response.messages)
