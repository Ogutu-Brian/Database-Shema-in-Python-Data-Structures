from . import uuid4, datetime, BaseModel


class User(BaseModel):
    """Defines all the user properties"""

    def __init__(self, first_name="", last_name="", email="", password="",
                 created_at=datetime.datetime.now(), updated_at=datetime.datetime.now()):
        super().__init__(created_at=updated_at, updated_at=updated_at)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def to_json(self):
        json_data = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password
        }
        return json_data
