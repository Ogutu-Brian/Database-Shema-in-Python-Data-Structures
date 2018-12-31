from .import (answer_view, Answer, session, db, request, jsonify)


@answer_view.route('/answer', methods=['POST'])
def post_answer():
    """Developes an endpoin for posting an answeer to a question"""
    if request.is_json:
        errors, valid = db.answers.is_valid(request.json)
        if not valid:
            return jsonify({
                "message": "You have encountered {} errors".format(len(errors)),
                "data": errors,
                "status": "error"
            }), 401
        else:
            answer = request.json["answer"]
            question = db.questions.query_by_field(
                "id", request.json["question"])
            if not question:
                return jsonify({
                    "message": "A question with that id does not exist",
                    "status": "error"
                }), 401
            else:
                question = question[0]
            if not "email" in session:
                return jsonify({
                    "message": "You must be logged in in order to answer a question",
                    "status": "error"
                }), 401
            user = db.users.query_by_field("email", session["email"])
            if not user:
                return jsonify({
                    "message": "There is no user bearing that email address",
                    "status": "error"
                }), 401
            else:
                user = user[0]
            answer_item = Answer(question=question, user=user, answer=answer)
            db.answers.insert(answer_item)
            return jsonify({
                "data": {key: value for (key, value) in
                         answer_item.to_json().items() if key != "question" and key != "user"},
                "question": answer_item.question.to_json()["question"],
                "user": answer_item.user.to_json()["first_name"],
                "status": "success"
            }), 201
    else:
        return jsonify({
            "message": "The data must be in JSON",
            "status": "error"
        }), 401


@answer_view.route('/', methods=['GET'])
def get_answers():
    data = []
    questions = db.answers.query_all()
    for item in questions:
        content = {key: value for (key, value) in item.to_json(
        ).items() if key != "question" and key != "user"}
        content["user"] = item.to_json()["user"].to_json()["first_name"]
        content["question"] = item.to_json()["question"].to_json()["question"]
        data.append(content)
    return jsonify({
        "data": data,
        "status": "success"
    }), 200
