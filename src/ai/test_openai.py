from openai import OpenAI

# 高效调用OpenAI的各类API（聊天、语音转文字等），无需处理底层http请求等细节
client:OpenAI = OpenAI(
    api_key = 'sk-fd40556b06fe4959b40f4bcb5a545ee1',
    base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
)

message = [
    {"role": "user", "content": "小红有5只猫"},
    {"role": "assistant", "content": "知道了"},
    {"role": "user", "content": "小明有3只狗"},
    {"role": "assistant", "content": "知道了"},
    {"role": "user", "content": "一共有多少只宠物？"},
]

completion = client.chat.completions.create(
    model = 'deepseek-v3.2',
    messages = message,
    stream = True
)

for chunk in completion:
    delta = chunk.choices[0].delta
    if hasattr(delta, "content") and delta.content:
        print(delta.content, end="", flush=True)

