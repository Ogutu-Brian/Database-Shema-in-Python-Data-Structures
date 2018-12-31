from .import (question_view, db, Question, request, jsonify, session)
import json


@question_view.route('/question', methods=['POST'])
def post_question():
    """Enables posting of a question into the system"""
    if request.is_json:
        errors, valid = db.questions.is_valid(request.json)
        if valid:
            subject = request.json["subject"]
            if "email" not in session:
                return jsonify({
                    "subject": "you must be logged in order to post a question",
                    "status": "error"
                }), 401
            user = db.users.query_by_field("email", session["email"])
            if not user:
                return jsonify({
                    "message": "A user with that email address is not in our system",
                    "status": "error"
                }), 401
            question = request.json["question"]
            question_item = Question(
                subject=subject, question=question, user=user[0])
            db.questions.insert(question_item)
            return jsonify({
                "data": {key: value for (key, value) in
                         question_item.to_json().items() if key != "user"},
                "user": question_item.to_json()["user"].to_json()["first_name"],
                "status": "success"
            }), 201
        else:
            return jsonify({
                "message": "you encountered {} errors".format(len(errors)),
                "data": errors,
                "status": "error"
            }), 401
    else:
        return jsonify({
            "message": "The data must be in JSON",
            "status": "error"
        }), 401


@question_view.route('/', methods=['GET'])
def get_questions():
    questions = [item.to_json() for item in db.questions.query_all()]
    return jsonify({
        "data": questions,
        "ststus": "success"
    }), 200
