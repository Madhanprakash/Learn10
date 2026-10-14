
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini",)

print("Model is ready!")

response = llm.invoke("What is Python in one sentence?")

print(response.content)

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0   # 0 = focused and predictable
)

response = llm.invoke("Give me 3 fun facts about space.")
print(response.content)

messages = [
    SystemMessage(content="You are a friendly teacher. Keep answers very short."),
    HumanMessage(content="What is a variable in Python?")
]

response = llm.invoke(messages)
print(response.content)