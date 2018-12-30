from ..schema.collections import (
    UserCollection, QuestionCollection, AnswerCollection)


class Database:
    """The main database holding all the schemas"""

    def __init__(self):
        self.users = UserCollection()
        self.questions = QuestionCollection()
        self.answers = AnswerCollection()

    def tear_down(self):
        """Clears every content of the database """
        self.users.clear()
        self.questions.clear()
        self.answers.clear()
