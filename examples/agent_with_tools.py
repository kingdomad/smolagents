from agents import load_tool, CodeAgent, HfApiEngine
from agents.search import DuckDuckGoSearchTool

# Import tool from Hub
image_generation_tool = load_tool("m-ric/text-to-image", cache=False)

# Import tool from LangChain

search_tool = DuckDuckGoSearchTool()

llm_engine = HfApiEngine("Qwen/Qwen2.5-72B-Instruct")
# Initialize the agent with both tools
agent = CodeAgent(tools=[image_generation_tool, search_tool], llm_engine=llm_engine)

# Run it!
result = agent.run(
    "Return me a photo of the car that James bond drove in the latest movie.",
)

print(result)