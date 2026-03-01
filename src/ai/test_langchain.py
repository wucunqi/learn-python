from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

def test_chat_model():
    chat = ChatOpenAI(
        model='deepseek-v3.2',
        temperature=0.7,
        api_key='sk-fd40556b06fe4959b40f4bcb5a545ee1',
        base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
    )

    # 消息格式可以简写为元组列表
    messages = [
        HumanMessage(content="你是谁")
    ]

    # 一次性返回完整结果
    # response = chat.invoke(messages)
    # print(response.content)

    # 流式输出
    response = chat.stream(messages)
    for chunk in response:
        print(chunk.content, end='', flush=True)


def test_vector_model():
    model = DashScopeEmbeddings(
        model='text-embedding-v1',
        dashscope_api_key='sk-fd40556b06fe4959b40f4bcb5a545ee1'
    )
    print(model.embed_query('我喜欢你'))


def test_prompt_template():
    prompt_template = PromptTemplate.from_template("我去面试{job}岗位，请生成一份自我介绍")
    prompt_text = prompt_template.format_prompt(job='高级软件开发工程师')
    print(dict(prompt_text))
    print(prompt_text.text)

    # model = ChatOpenAI(
    #     model='deepseek-v3.2',
    #     temperature=0.7,
    #     api_key='sk-fd40556b06fe4959b40f4bcb5a545ee1',
    #     base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'
    # )
    # print(model.invoke(prompt_text))

if __name__ == '__main__':
    test_prompt_template()












