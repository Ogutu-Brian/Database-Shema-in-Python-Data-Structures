from . import(datetime, BaseModel)


class Question(BaseModel):
    """Defines all the properties of a question"""

    def __init__(self, subject="", question="", user=None,
                 created_at=datetime.datetime.now(), update_at=datetime.datetime.now()):
        super().__init__(self, created_at=created_at, update_at=update_at)
        self.subject = subject
        self.question = question
        self.user = user

    def to_json(self):
        json_data = {
            "id": self.id,
            "subject": self.subject,
            "question": self.question,
            "user": self.user
        }
        return json_data
