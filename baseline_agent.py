from logger import log_interaction


class BaselineAgent:

    def __init__(self):

        self.responses = {
            "hello": "Hello! Welcome to TechFix Electronics Support.",
            "hi": "Hi! How can I help you today?",
            "warranty": "Please refer to your warranty card or contact support.",
            "refund": "Refund requests are processed within 7 working days.",
            "return": "Products can be returned within 30 days of purchase.",
            "shipping": "Shipping usually takes 3-5 business days.",
            "bye": "Thank you for contacting TechFix. Have a great day!"
        }

    def get_response(self, user_input):

        query = user_input.lower()
        words = query.split()
        
        for keyword in self.responses:
            if keyword in query:
                response = self.responses[keyword]
                log_interaction(user_input, response)
                return response

        response = (
            "Sorry, I don't understand your request. "
            "Please contact customer support."
        )

        log_interaction(user_input, response)

        return response