from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


load_dotenv()

def main():
    print("Hello from langchain-course!")

    text = "What is the capital of Nigeria?"

    # Same as using s strings directly
    prompt = PromptTemplate(
        input_variables=["question"], template="Answer the following question: {question}"
    )

    llm = ChatOllama(
        model="gemma3:270m",
        temperature=0,
    )

    chain = prompt | llm

    response = chain.invoke({"question": text})
    print(response.content)

if __name__ == "__main__":
    main()
