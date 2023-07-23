from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=(Path(__file__).parent.parent / ".env").absolute())

from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import OpenAI


# The language model we're going to use to control the agent.
llm = OpenAI(temperature=0.9)

# The tools we'll give the Agent access to. Note that the 'llm-math' tool uses an LLM, so we need to pass that in.
# 使用了langchain的tools功能，tools提供了大模型一些可用工具，在大模型推理时，可以选择合适的工具和外界进行交互，补充信息
tools = load_tools(["serpapi"], llm=llm)


# Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
# agent封装了一套完整的交互逻辑，帮助大模型一步步推理，到最终解决问题
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Let's test it out!
question = "蔡徐坤现在情况如何，适合代言吗"
print(f'Q: {question}')
print(f'A: {agent.run(question)}')
