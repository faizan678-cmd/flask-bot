from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.prompts import ChatPromptTemplate

llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.7,
    api_key="RyIgKDZLaJGSiQ7sDOB9ZCnGhleSf1oh"
)
def get_answer(question):

    response = llm.invoke([
        SystemMessage(content="your are a helpful caption and trending hastage generator based on niche and content,ganerate only 3 viral captions and 5 viral hastags ,dont answer other type of questions"),
        HumanMessage(content=question)
    ])
    return response.content