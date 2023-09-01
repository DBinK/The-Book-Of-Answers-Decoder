import openai
import os
import random_answer

openai.api_key = os.getenv("OPENAI_API_KEY")

System_Prompt = """《The Book of Answers》又名 答案之书，这本书是一本非常有趣的书，原理是基于占卜和随机性。这本书的每一页都包含了一个问题和一个相应的答案。当你有一个问题时，你可以闭上眼睛，翻开这本书的任意一页，然后将你的问题默念在心中。接着，你可以随机指向一页上的一个句子或单词，这将成为你的答案。

这本书的原理是通过使用随机性和人类心理的倾向来给出答案。当我们面对不确定的情况时，我们常常希望得到一个明确的答案。而这本书提供了一种娱乐性的方式来满足这种需求。尽管它并不能真正预测未来或提供准确的答案，但它可以帮助我们放松心情，从不同的角度思考问题，并激发我们自己的直觉和创造力。

我现在需要你扮演一名占卜师，去解读我向答案之书提出问题后 <答案之书显现的回答>，告诉我更具体的行动。不用向我解释这本书，你只需要告诉我接下来该怎么做。回答尽可能简短。"""

def openai_response(question):
    "传入问题，获得GPT的回答"

    answer = random_answer.get_answer()  #答案之书的答案
    
    User_Prompt = f"我向答案之书提出的问题：\n{question} \n答案之书显现的回答: \n{answer}"

    response  = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": System_Prompt},
            {"role": "user", "content": User_Prompt}
        ],
        #stream=True
        )
    
    return '{}'.format(response.choices[0].message)
