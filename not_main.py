import os
from apikey import apikey
#import langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

#os.environ['OPENAI_API_KEY'] ='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'




llm = ChatOpenAI(openai_api_key= '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')

user_input = input()

print(llm.predict(text=user_input))
