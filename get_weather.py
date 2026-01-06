# my_agent.py
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

# 1. Load the API Key
# This looks for a .env file, or expects you to export the variable in your terminal
load_dotenv()

# Verification check (Optional but recommended)
if not os.getenv("OPENAI_API_KEY"):
    print("❌ Error: OPENAI_API_KEY is missing!")
    exit(1)

# 2. Define the Tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

# 3. Initialize Model
# We use temperature=0 for more deterministic tool usage
model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 4. Create the Agent
agent = create_react_agent(model, tools=[get_weather])

# 5. Run the Agent
print("🤖 Agent is thinking...")
inputs = {"messages": [HumanMessage(content="what is the weather in sf")]}
response = agent.invoke(inputs)

# 6. Extract and Print the Final Answer
# LangGraph returns a list of messages; the last one is the AI's final answer
print(f"✅ Answer: {response['messages'][-1].content}")