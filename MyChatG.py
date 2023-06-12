import openai
import gradio

openai.api_key= "sk-"

messages = [{"role": "system", "content": "Sei uno psicologo"}]

def CustomChatGPT(user_input):
    messages.append({"role": "system", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "system", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "PSICOLOGO DIGITALE")
demo.launch(share= True)



