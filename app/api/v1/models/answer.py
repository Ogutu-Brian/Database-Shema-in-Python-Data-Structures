from . import uuid4, BaseModel, datetime


class Answer(BaseModel):
    """Defines the properties of an answer to a question"""

    def __init__(self, question=None, user=None, answer="",
                 created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()):
        super().__init__(created_at=created_at, updated_at=updated_at)
        self.question = question
        self.answer = answer
        self.user = user

    def to_json(self):
        json_data = {
            "id": self.id,
            "question": self.question,
            "answer": self.answer,
            "user": self.user
        }
        return json_data
