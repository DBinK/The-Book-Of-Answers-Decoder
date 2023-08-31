import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def openai_response(question):
    response  = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        #stream=True
        )
    
    return '{}'.format(response.choices[0].message)

"""

question = input('Ask something: ')

result = openai_response(question)

print(result)

"""
