from flask import (Flask, session, jsonify, request)
from instance.config import secret_key
from . import(question_view, answer_view, user_view)


def create_app():
    app = Flask(__name__)
    app.secret_key = secret_key
    app.register_blueprint(question_view, url_prefix="/api/v1/questions")
    app.register_blueprint(answer_view, url_prefix="/api/v1/answers")
    app.register_blueprint(user_view, url_prefix="/api/v1/users")

    @app.errorhandler(404)
    def page_not_found_handler(error):
        return jsonify({
            "message": "The requested URL was not found on the server",
            "status": "error"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed_handler(error):
        if request.method == 'POST':
            return jsonify({
                "message": "You could be doing a post instead of a get",
                "status": "eror"
            }), 405
        return jsonify({
            "message": "You could be doing a get instead of a post",
            "status": "error"
        }), 405
    return app


app = create_app()
if __name__ == "__main__":
    app.run()
