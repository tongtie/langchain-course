from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=(Path(__file__).parent.parent / ".env").absolute())

# 导入langchain封装的OpenAI接口
from langchain.llms import OpenAI
# 初始化大模型实例
llm = OpenAI(temperature=0.9)
# 询问大模型
question = "蔡徐坤现在情况如何，适合代言吗"
print(f'Q: {question}')
print(f'A: {llm.predict(question)}')
