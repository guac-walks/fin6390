import os
from apikey import apikey
#import langchain
#from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

#os.environ['OPENAI_API_KEY'] ='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'




llm = ChatOpenAI(openai_api_key= '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')

user_input = 'What is the date?'

llm.predict(text=user_input)
