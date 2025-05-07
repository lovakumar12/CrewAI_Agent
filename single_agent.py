import os
from dotenv import load_dotenv
from crewai import Agent,Task,Crew
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI

search_tool = SerperDevTool()

load_dotenv()
SERPER_API_KEY=os.getenv("SERPER_API_KEY")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

search_tool = SerperDevTool()
llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0)

def create_research_agents():
    # Create a research agent with the search tool
    
    return  Agent(
            role="Research specialist",
            goal="conduct through research on given topics",
            backstory="You are an experienced researcher with expertise in finding and synthesizing information from various sources." ,
            verbose=True,
            allow_delgation=False,
            tools=[search_tool],
            llm=llm
        )
       
    
def create_research_task(agent,topic):
    # Create a research task with the agent
    return Task(
        description="Research the following topic and provide a comprehensive summary.",
        agent=agent ,
        expected_output="A detailed summary of the research findings ,including key points and insights.",
        
    )
       
def run_research(topic):
    agent= create_research_agents()
    task= create_research_task(agent,topic)
    crew=Crew(
        agents=[agent],
        tasks=[task],
       
    )
    results=crew.kickoff()
    return results

if __name__=="__main__":
    print("Welcome to the Research Agent!")
    topic=input("Please enter the topic you want to research: ")
    result=run_research(topic)
    print("Research Results:",result)