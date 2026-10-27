class ConversationMemory:

    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append(
            {
                "role": role,
                "message": message
            }
        )

    def get_context(self):

        context = ""

        for item in self.history[-6:]:

            context += f"{item['role']}: {item['message']}\n"

        return context

    def clear(self):
        self.history = []