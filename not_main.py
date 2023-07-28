import os
import getpass
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

os.environ['OPENAI_API_KEY'] =''


#llm = ChatOpenAI(openai_api_key= '')

#load our data
loader = TextLoader("data.txt")
doc = loader.load()

#split document 
text_splitter = RecursiveCharacterTextSplitter(separators=['#', '\n\n', '\n'], chunk_size=100, chunk_overlap=20)
final_split = text_splitter.split_documents(documents=doc)

#embed docs and load into VectorStore
db = Chroma.from_documents(final_split, OpenAIEmbeddings())

#embed query and print response
#print("Enter a prompt: ")
#user_input = input()
text = "Can I take a day off?"

#embedding_query = OpenAIEmbeddings.embed_query(text=text)
answer = db.similarity_search(text)
print(answer[0].page_content)

#check
#print(llm.predict(text=user_input))

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

