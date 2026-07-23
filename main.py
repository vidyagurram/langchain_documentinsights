import os

from dotenv import load_dotenv

load_dotenv()


def main():
    print("Hello from langchain-documentationhelper!")
    print(os.environ.get("OPENAI_API_KEY"))
    print(f"Your OpenAI API key is: {os.getenv('OPENAI_API_KEY')}")


if __name__ == "__main__":
    main()
