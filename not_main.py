import os
from apikey import apikey
#import langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

#os.environ['OPENAI_API_KEY'] ='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'




llm = ChatOpenAI(openai_api_key= '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')

print("Enter a prompt: ")
user_input = input()

print(llm.predict(text=user_input))

#look at internal documents eventually leverage chatgpt (potentially give people the option to use chatgpt)
#look more into query for langchain and vectorstore and retreivers

#Next steps for coding:
#-what type of employee is it - but don't limit what can be asked -> look at account being used
#1. loading data.txt and getting an answer based on our data
#2. look at entire directory
#3. create memory
#4. if answer is wrong, add/find appropriate rule to get correct answer in a rules.txt
#5. make it user-friendly

#Things to consider:
#admin/new-user, if incorrect sent to a group/team for QA
#if chatbot doesn't know -> send to a team member (can remain anonymous or not)
#show confidence level if less than X% (one for rephrasing, one for flagging and sending to supervisor)
#text to voice in response and voice to text when asking a question
#collect analytics
#cleaner interface (text-message style??)

#what's the big vision
#here is the 30% what will we do for the other 70%
#it is like a pitch to a VC
