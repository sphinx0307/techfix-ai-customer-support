from langchain_ollama import ChatOllama
from utils import SafetyGuard
from memory import ConversationMemory
from vectorstore import VectorStoreManager
from logger import log_interaction
from prompts import SYSTEM_PROMPT
from tools import SupportTicketTool
from feedback import FeedbackManager


class RAGAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="mistral",
            temperature=0
        )

        self.memory = ConversationMemory()
        self.guard = SafetyGuard()
        manager = VectorStoreManager()
        self.vector_db = manager.build()
        self.feedback = FeedbackManager()
        self.ticket_tool = SupportTicketTool()

    def get_response(self, user_input):

        allowed, message = self.guard.check(user_input)

        if not allowed:

            self.memory.add("User", user_input)
            self.memory.add("Assistant", message)

            log_interaction(user_input, message)

            return message

       
        # TOOL 2 : SUPPORT TICKET
        
        ticket_keywords = [
            "issue",
            "problem",
            "broken",
            "repair",
            "overheat",
            "heating",
            "battery",
            "charging",
            "not working",
            "screen",
            "display"
        ]

        if any(word in user_input.lower() for word in ticket_keywords):

            ticket = self.ticket_tool.generate_ticket(user_input)

            self.memory.add("User", user_input)
            self.memory.add("Assistant", ticket)

            log_interaction(user_input, ticket)

            return ticket

        # -----------------------------
        # RAG SEARCH
        # -----------------------------
        docs = self.vector_db.similarity_search(
            user_input,
            k=3
        )

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        conversation = self.memory.get_context()

        prompt = f"""
{SYSTEM_PROMPT}

Conversation History:

{conversation}

Knowledge Base:

{context}

Answer ONLY using the knowledge base.

If the answer is not available, reply exactly:

I couldn't find this information in the TechFix knowledge base.

User Question:

{user_input}
"""

        response = self.llm.invoke(prompt)

        answer = response.content

        self.memory.add("User", user_input)
        self.memory.add("Assistant", answer)

        log_interaction(user_input, answer)

        print("\nWas this response helpful?")
        print("1. Yes")
        print("2. No")

        choice = input("Choice : ")

        if choice == "1":
            self.feedback.save_feedback(
                user_input,
                answer,
                "Helpful"
            )
        else:
            self.feedback.save_feedback(
                user_input,
                answer,
                "Not Helpful"
            )

        return answer