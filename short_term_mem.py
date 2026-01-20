from langchain.agents import create_agent
from langgraph.checkpoint.postgres import PostgresSaver

def short_term_memory():
    DB_URI = "postgresql://postgres:postgres@localhost:5442/postgres?sslmode=disable"
    with PostgresSaver.from_conn_string(DB_URI) as checkpointer:
        checkpointer.setup() # auto create tables in PostgresSql
        agent = create_agent(
            "gpt-5",
            tools=[get_user_info],
            checkpointer=checkpointer,
        )

from langchain.agents import create_agent, AgentState
from langgraph.checkpoint.memory import InMemorySaver


class CustomAgentState(AgentState):
    user_id: str
    preferences: dict

agent = create_agent(
    "gpt-5",
    tools=[get_user_info],
    state_schema=CustomAgentState,
    checkpointer=InMemorySaver(),
)

# Custom state can be passed in invoke
result = agent.invoke(
    {
        "messages": [{"role": "user", "content": "Hello"}],
        "user_id": "user_123",
        "preferences": {"theme": "dark"}
    },
    {"configurable": {"thread_id": "1"}})