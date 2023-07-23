from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=(Path(__file__).parent.parent / ".env").absolute())

# 导入langchain封装的OpenAI接口
from langchain.llms import OpenAI

prompt = """上下文信息如下:
{context}

基于如上信息，回答用户的问题: {question}
"""

# 初始化大模型实例
llm = OpenAI(temperature=0.9)

# 询问大模型
# 上下文信息，内容来自百度搜索：https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E8%94%A1%E5%BE%90%E5%9D%A4%E7%8E%B0%E5%9C%A8%E6%83%85%E5%86%B5%E5%A6%82%E4%BD%95%EF%BC%8C%E9%80%82%E5%90%88%E4%BB%A3%E8%A8%80%E5%90%97&fenlei=256&rsv_pq=0xa7a1939c001fce9f&rsv_t=eff8ZrQaF01p7OBgTHgozWujQYNWapcqQOXNl8h0JjNCXeRLDKub%2F9RKM6s&rqlang=en&rsv_dl=tb&rsv_enter=0&rsv_sug3=2&rsv_sug1=2&rsv_sug7=101&rsv_btype=i&prefixsug=%25E8%2594%25A1%25E5%25BE%2590%25E5%259D%25A4%25E7%258E%25B0%25E5%259C%25A8%25E6%2583%2585%25E5%2586%25B5%25E5%25A6%2582%25E4%25BD%2595%25EF%25BC%258C%25E9%2580%2582%25E5%2590%2588%25E4%25BB%25A3%25E8%25A8%2580%25E5%2590%2597&rsp=7&inputT=1535&rsv_sug4=1559
context = """
半岛聚焦|风险提示傍身,矛头直指蔡徐坤!出道5年代言超30个...
3月7日，Mistine蜜丝婷品牌正式官宣签约蔡徐坤为品牌防晒代言人；4月11日，Meco蜜谷果汁茶官宣全新品牌代言人蔡徐坤；5月10日，燕京啤酒在国家品牌日官宣蔡徐坤为全线品牌代言人，并于31日官宣蔡...
半岛都市报
蔡徐坤的商业代言,将受到哪些影响?-虎嗅网
2023年7月4日 进入2023年,蔡徐坤早已官宣不少品牌代言。 3月7日,Mistine蜜丝婷品牌正式官宣签约蔡徐坤为品牌防晒代言人;4月11日,Meco蜜谷果汁茶官宣全新品牌代言人蔡徐坤;5月10日,燕京啤酒在国家...
虎嗅APP
蔡徐坤翻身无望!品牌撤图商场下架产品,圈内品牌方都在陆续...
2023年7月8日 除了代言商务，人们同样关注蔡徐坤在综艺节目方面的去向。甚至有网友为某综艺节目提建议，建议直接将赞助商的宣传中去掉蔡徐坤。不得不佩服网友们的想象力。即使是曾经积极支持的粉...
芋泥草莓聊娱乐
蔡徐坤风波升级!广告牌开撤,再谈代言暂停,疑似团队下场炸...
2023年6月27日 广告牌开撤,再谈代言暂停,疑似团队下场炸词条 2023年6月26日,蔡徐坤出道第12个年头,被曝“一夜情致女方怀孕”,事后蔡徐坤母亲以50万的价格协商让女方打胎,又怀疑女方骗人雇佣私家侦...
网易
央视频下架、代言品牌“切割”……蔡徐坤面临“灾难性后果”
7月3日，澎湃新闻记者就上述三个品牌目前代言合作事宜咨询电商客服，其中宝洁官方旗舰店客服回应称，目前蔡徐坤与汰渍品牌的合作已经结束了，结束时间方面没有具体数据。维达回应称，更多明星相关...
"""
# 问题
question = "蔡徐坤现在情况如何，适合代言吗"
print(f'Context: {context}')
print(f'Q: {question}')
print(f'A: {llm.predict(prompt.format(context=context, question=question))}')
