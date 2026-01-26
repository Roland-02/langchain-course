from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def main():
    print("Hello from langchain-course!")

    text = "What is the capital of Nigeria?"

    # Same as using s strings directly
    prompt = PromptTemplate(input_variables=["question"], template="summary_template {question}")

    llm = ChatGoogleGenerativeAI(
        model="gemini-3-pro-preview",
        temperature=1.0,  # Gemini 3.0+ defaults to 1.0
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
    )

    chain = prompt | llm

    response = chain.invoke({"question": text})

    print(response.content)

if __name__ == "__main__":
    main()
