class BaseCollection:
    """defines all the operarions done in other data collections 
    and template methods that are overridded
    """

    def __init__(self):
        self.data = {}
        self.index = 0

    def insert(self, item):
        """Enables insertion of data into the collection"""
        self.data[self.index] = item
        self.index += 1

    def query_by_field(self, field, value):
        """Queries by field name of the to find a given object"""
        result = []
        for item in self.data.values():
            if item.to_json().get(field) == value:
                result.append(item)
        return result

    def is_valid(self, item):
        """To be overrieden depending on the nature of the model and waht is to be ladidated"""
        errors = []
        return errors, len(errors) == 0

    def query_all(self):
        """Queries all the items in the scheme"""
        result = []
        for item in self.data.values():
            result.append(item)
        return result

    def clear(self):
        """This clears all the data in the collection and returns the empty dictionary"""
        self.data = {}
        return self.data


class UserCollection(BaseCollection):
    def is_valid(self, item):
        errors = []
        if not item.get('password'):
            errors.append({
                "message": "passowrd must be provided",
                "status": "error"
            })
        if not item.get('email'):
            errors.append({
                "message": "an email must be provided",
                "status": "error"
            })
        for ite_m in self.data.values():
            if item.get("email") == ite_m.to_json().get("email"):
                errors.append({
                    "message": "A user with the email address exists",
                    "status": "error"
                })
        if not item.get('first_name'):
            errors.append({
                "message": "first name must be provided",
                "status": "error"
            })
        if not item.get('last_name'):
            errors.append({
                "message": "last name must be provided",
                "status": "error"
            })
        return errors, len(errors) == 0

    def validate_password(self):
        pass


class QuestionCollection(BaseCollection):
    def is_valid(self, item):
        errors = []
        if not item.get('subject'):
            errors.append({
                "message": "subject must be provided",
                "status": "error"
            })
        # if not item.get("user"):
        #     errors.append({
        #         "message": "user must be propvided",
        #         "status": "error"
        #     })
        if not item.get('question'):
            errors.append({
                "message": "a question must be provied",
                "status": "error"
            })
        return errors, len(errors) == 0


class AnswerCollection(BaseCollection):
    def is_valid(self, item):
        errors = []
        if not item.get('question'):
            errors.append({
                "message": "question must be provided",
                "status": "error"
            })
        # if not item.get('user'):
        #     errors.append({
        #         "message": "a user must be provided",
        #         "status": "error"
        #     })
        if not item.get('answer'):
            errors.append({
                "message": "answer must be provided",
                "status": "error"
            })
        return errors, len(errors) == 0
