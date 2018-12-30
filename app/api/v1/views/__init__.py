from flask import Blueprint
from ..schema.db import Database
from ..models.user import User
from ..models.question import Question
from ..models.answer import Answer
from flask import(jsonify, request, session, url_for, redirect)
db = Database()
question_view = Blueprint('views.question', __name__)
answer_view = Blueprint('views.answer', __name__)
user_view = Blueprint('views.user', __name__)
