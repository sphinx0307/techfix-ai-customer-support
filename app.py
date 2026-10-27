from baseline_agent import BaselineAgent
from rag_agent import RAGAgent

print("=" * 60)
print("TechFix AI Customer Support")
print("=" * 60)

print("1. Baseline Agent")
print("2. AI Agent")

choice = input("\nChoose option : ")

if choice == "1":
    agent = BaselineAgent()
else:
    agent = RAGAgent()

print("\nType 'exit' to quit.")

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        break

    print("\nAgent :", agent.get_response(user))