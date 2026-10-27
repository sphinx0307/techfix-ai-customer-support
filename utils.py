class SafetyGuard:

    def check(self, user_input):

        query = user_input.lower()

        restricted_requests = [
                        "another customer",
                        "customer details",
                        "customer information",
                        "delete account",
                        "delete my account",
                        "close my account",
                        "hack",
                        "password",
                        "credit card",
                        "bank account"
                    ]

        for item in restricted_requests:

            if item in query:

                return (
                    False,
                    "I'm sorry, but I cannot assist with that request. "
                    "Please contact an authorized TechFix support representative."
                )

        return True, None