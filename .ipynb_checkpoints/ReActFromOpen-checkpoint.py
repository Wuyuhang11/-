import os
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain_wenxin import ChatWenxin
from langchain.schema import (
    AIMessage,
    HumanMessage,
)

def query_wenxin(user_question):
    # 谷歌搜索的Key
    os.environ["SERPAPI_API_KEY"] = '31a3c96f0ce535fd1b43117d3c9298c66753b6dae1da9074708f03ecc8282367'

    # 文心model
    WENXIN_APP_Key = "6EMY3gUCVVCe9aT40GsbEuE6"
    WENXIN_APP_SECRET = "zLMlLQOn80gpnVwCsZ4mnAr3vHhtBG7r"

    chat_model = ChatWenxin(
        temperature=0.9,
        model="ernie-bot-turbo",
        baidu_api_key=WENXIN_APP_Key,
        baidu_secret_key=WENXIN_APP_SECRET,
        verbose=True,
    )

    # 加载 serpapi 工具
    tools = load_tools(["serpapi"])

    # 初始化代理
    agent = initialize_agent(tools, chat_model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
                             handle_parsing_errors=True)

    # try:
    #     # 运行 agent
    #     res = agent.run(
    #         "以传入的信息为主，根据隋朝的背景信息介绍诗词的含义和背景信息，无需反复思考，过程尽量言简意赅）：" + user_question)
    # except ValueError as e:
        # 如果SerpAPI没有返回结果，直接使用ReAct框架处理
    response = chat_model(
        [
            HumanMessage(content="以传入的信息为主，根据隋朝的背景信息介绍诗词的含义和背景信息，无需反复思考，过程尽量言简意赅（注意：根据您提供的信息这些内容请省略...，直接说主要内容）,传入信息如下：" + user_question)
        ]
    )
    # print(response.content.__str__())
    print("res:",response.content.__str__())
    # for char in res:
    #     yield char
    return response.content.__str__()



