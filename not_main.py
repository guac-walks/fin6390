import os
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

#functions

def user_is_client():
    #load our data
    loader = TextLoader("C:/Users/chand/OneDrive - Utah Valley University/code/fin6390_project/client.txt")
    doc = loader.load()

    #go to split and embed doc function
    db = split_embed_doc(doc)

    #go to user input function
    u_input, f_answer = user_input(db)

    return u_input, f_answer


def user_is_employee():
    #load our data
    loader = TextLoader("C:/Users/chand/OneDrive - Utah Valley University/code/fin6390_project/employee.txt")
    doc = loader.load()

    #go to split and embed doc function
    db = split_embed_doc(doc)

    #go to user input function
    u_input, f_answer = user_input(db)

    return u_input, f_answer

def split_embed_doc(doc):
    #split document 
    text_splitter = RecursiveCharacterTextSplitter(separators=['#', '\n\n', '\n'], chunk_size=100, chunk_overlap=20)
    final_split = text_splitter.split_documents(documents=doc)

    #embed docs and load into VectorStore
    db = Chroma.from_documents(final_split, OpenAIEmbeddings())
    return db

def user_input(db):
    #embed query and print response
    print("Enter a prompt: ")
    user_input = input()
    #text = "What can I wear"

    #embedding_query = OpenAIEmbeddings.embed_query(text=text)
    answer = db.similarity_search(user_input)
    f_answer = answer[0].page_content
    return user_input, f_answer

def print_prompt(u_input, f_answer):
    print(f_answer + '\n\n')

    prompt = "Use the following question, " + u_input + ", to respond to the employee using the following info to center your response around: " + f_answer 

    #check
    print(llm.predict(text=prompt))
    return


#program begins running from here
os.environ['OPENAI_API_KEY'] =''

llm = ChatOpenAI()

print('Are you a client or employee?')
user_type = input()
user_type = user_type.lower()

if user_type == 'client':
    u_input, f_answer = user_is_client()
    print_prompt(u_input, f_answer)
if user_type == 'employee':
    u_input, f_answer = user_is_employee()
    print_prompt(u_input, f_answer)


#look at internal documents eventually leverage chatgpt (potentially give people the option to use chatgpt)
#look more into query for langchain and vectorstore and retreivers

#Next steps for coding:
#-what type of employee is it - but don't limit what can be asked -> look at account being used
#1. loading data.txt and getting an answer based on our data
#2. look at entire directory
#3. create memory
#4. if answer is wrong, add/find appropriate rule to get correct answer in a rules.txt
#5. make it user-friendly/make it conversational (by adding memory and agents)
#6. Have the AI answer truthfully via a prompt and have it store memory in a new file

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

