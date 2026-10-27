import json
import os


class FeedbackManager:

    def __init__(self):
        self.file_path = "data/feedback.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)

    def save_feedback(self, question, answer, feedback):

        with open(self.file_path, "r") as file:
            data = json.load(file)

        data.append({
            "question": question,
            "answer": answer,
            "feedback": feedback
        })

        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)