
import os
from langchain_openai import ChatOpenAI

# Read the API key securely from an environment variable
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError(
        "OPENAI_API_KEY is missing. Set it before running the script."
    )

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = """
Generate exactly 5 healthy, vegetarian South Indian breakfast ideas.

Requirements:

Include a variety of dishes using fruits, millets, lentils, whole grains, and fresh vegetables.

Ensure each idea includes at least one nutritious source of protein or fiber.

Prefer steaming, boiling, fermenting, or cooking with minimal oil.

Avoid deep-fried dishes, excessive salt, and added sugar.

Choose affordable ingredients that are readily available in Tamil Nadu, India.

Avoid repeating the same main ingredient or preparation style across all five ideas.

Format the response as a numbered list from 1 to 5, with one concise breakfast idea per line.

Do not include recipes, nutritional explanations, an introduction, or a conclusion.

Return exactly 5 distinct ideas and nothing else.
"""

# Invoke the model
reply = llm.invoke(prompt)

# Print only the message text
print(reply.content)
