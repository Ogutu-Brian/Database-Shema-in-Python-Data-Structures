from . import(user_view, User, jsonify, request,
              db, session, url_for, redirect)
import bcrypt


@user_view.route('/sign-up', methods=['POST'])
def sign_up():
    if request.is_json:
        data = request.json
        errors, valid = db.users.is_valid(data)
        if not valid:
            return jsonify({
                "message": "You encountered {} errors".format(len(errors)),
                "data": errors,
                "status": "error"
            }), 401
        # Encrypting the password
        data["password"] = bcrypt.hashpw(data["password"].encode(
            'utf8'), bcrypt.gensalt()).decode('utf8')
        user = User(first_name=data["first_name"], last_name=data["last_name"],
                    email=data["email"], password=data["password"])
        db.users.insert(user)
        return jsonify({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "password": user.password,
            "status": "success"
        }), 201
    else:
        return jsonify({
            "message": "the data must be in JSON",
            "status": "error"
        }), 401


@user_view.route('/log-in', methods=['POST'])
def log_in():
    if not request.is_json:
        return jsonify({
            "message": "The data must be in JSON",
            "status": "error"
        }), 401
    data = request.json
    if not data.get("email") and not data.get("password"):
        return jsonify({
            "message": "Please enter your email address and password",
            "status": "error"
        }), 401
    if not data.get("email"):
        return jsonify({
            "message": "Please enter your email address",
            "status": "error"
        }), 401
    if not data.get("password"):
        return jsonify({
            "message": "Please enter your password",
            "status": "error"
        }), 401
    user = db.users.query_by_field("email", data["email"])
    if not user:
        return jsonify({
            "message": "you have not created an account with us, please sign up to create an account",
            "status": "error"
        }), 401
    else:
        user = user[0]
        if bcrypt.checkpw(data["password"].encode('utf8'), user.password.encode('utf8')):
            session["email"] = user.email
            return jsonify({
                "message": "Welcome to stack overflow lite {}".format(user.first_name),
                "status": "success"
            }), 200
        else:
            return jsonify({
                "message": "Either your email address or your password is incorrect",
                "status": "error"
            }), 401


@user_view.route('/log-out', methods=['DELETE'])
def log_out():
    if not session.get("email"):
        return jsonify({
            "message": "The session had expired",
            "status": "error"
        }), 401
    else:
        mail = session["email"]
        session.pop("email")
        return jsonify({
            "message": "You have successfully logged out of stack overflow-lite, have a good day {}".format(
                db.users.query_by_field("email", mail)[0].to_json()["first_name"]),
            "status": "success"
        }), 200


@user_view.route('/', methods=['GET'])
def get_all_users():
    users = db.users.query_all()
    data = [user.to_json() for user in users]
    return jsonify({
        "data": data,
        "status": "success"
    }), 200
