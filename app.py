import flask
import random

server = flask.Flask(__name__)

registered_users = {}
submissions = {}


def generate_id():
    pool = list("abcdefghijklmnopqrstuvwxyz124567890")
    return ''.join(random.choice(pool) for i in range(5))

# The Web Page paths

@server.route("/",methods=["GET"])
def index_page():
    return flask.render_template("index.html")

# if you want the audience to see the questions after the quiz is done
@server.route("/questions",methods=["GET"])
def questions_page():
    return flask.render_template("questions.html")

# page to show the registered users
@server.route("/registered",methods=["GET"])
def registered_page():
    return flask.render_template("registered.html", n=len(registered_users))

# page to show the on going submissions
@server.route("/submissions",methods=["GET"])
def submissions_page():
    return flask.render_template("submissions.html")


# The POST Requests paths

@server.route("/api/post/register",methods=["POST"]) # to register a user, returns the id
def api_register_user():
    data = flask.request.get_json()
    print(data)
    try:
        a = generate_id()
        registered_users[a] = data['name']
        return flask.jsonify({"success":True, "id":a, "error": "none"})

    except Exception as e:
        return flask.jsonify({"success":False, "error": e})


# delete the registered user so that it can't make any more submissions
@server.route("/api/post/delete_registration",methods=["POST"])
def api_delete_registration():
    data = flask.request.get_json()
    print(data)
    if(data["id"] in registered_users and registered_users[data["id"]]==data["name"]):
        del registered_users[data["id"]]
        return flask.jsonify({"success":True, "error":"none"})
    else:
        return flask.jsonify({"success":False, "error":"request to delete a non-existing user"})

# to submit a score.
@server.route("/api/post/submission",methods=["POST"])
def api_add_submission():
    data = flask.request.get_json()

    try:
        if(data["id"] in registered_users and registered_users[data["id"]]==data["name"]):
            if(data["id"] not in submissions):
                submissions[data["id"]] = [data["name"],[int(data["score"])]]
                print(submissions)
                return flask.jsonify({"success":True, "error": "none"})
            else:
                submissions[data["id"]][1].append(int(data["score"]))
                print(submissions)
                return flask.jsonify({"success":True, "error": "none"})
        else:
            return flask.jsonify({"success":False, "error": "User is not registered"})
    except Exception as e:
        return flask.jsonify({"success":False, "error": e})

# Paths that return data. Used by the js in /registered and /submissions

@server.route("/api/get/registered_users", methods=["GET"])
def api_get_registered_users(): # for the registered.html webpage
    return flask.jsonify(registered_users)

@server.route("/api/get/submissions",methods=["GET"])
def api_get_submissions(): # for the submissions.html webpage
    return flask.jsonify(submissions)

# let the game begin !
if __name__ == "__main__":
    server.run(port=8000, host="0.0.0.0")