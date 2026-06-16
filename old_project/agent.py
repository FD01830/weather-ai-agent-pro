
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
from config import XAI_API_KEY,XAI_BASE_URL,MODEL_NAME
from tools import get_weather

llm=ChatOpenAI(api_key=XAI_API_KEY,base_url=XAI_BASE_URL,model=MODEL_NAME,temperature=0)
prompt=hub.pull("hwchase17/react")
tools=[DuckDuckGoSearchRun(),get_weather]
agent=create_react_agent(llm,tools,prompt)
agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True,handle_parsing_errors=True)
