import flask
import random, string

server = flask.Flask(__name__)

d = open("data.json","r")
d_w = open("data.json","w")

registered_users = {}
submissions = dict(d.read())


def generate_id():
    pool = list("abcdefghijklmnopqrstuvwxyz124567890")
    return ''.join(random.choice(pool) for i in range(5))

@server.route("/",methods=["GET"])
def index_page():
    return flask.render_template("index.html")

@server.route("/questions",methods=["GET"])
def questions_page():
    return flask.render_template("questions.html")

@server.route("/registered",methods=["GET"])
def registered_page():
    return flask.render_template("registered.html", n=len(registered_users))


@server.route("/submissions",methods=["GET"])
def submissions_page():
    return flask.render_template("submissions.html")


@server.route("/api/post/register",methods=["POST"])
def api_register_user():
    data = flask.request.get_json()
    print(data)
    try:
        a = generate_id()
        registered_users[a] = data['name']
        return flask.jsonify({"success":True, "id":a, "error": "none"})

    except Exception as e:
        return flask.jsonify({"success":False, "error": e})


@server.route("/api/post/delete_registration",methods=["POST"])
def api_delete_registration():
    data = flask.request.get_json()
    print(data)
    if(data["id"] in registered_users and registered_users[data["id"]]==data["name"]):
        del registered_users[data["id"]]
        return flask.jsonify({"success":True, "error":"none"})
    else:
        return flask.jsonify({"success":False, "error":"request to delete a non-existing user"})

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

    d_w.write(str(submissions))

@server.route("/api/get/registered_users", methods=["GET"])
def api_get_registered_users(): # for the registered.html webpage
    return flask.jsonify(registered_users)

@server.route("/api/get/submissions",methods=["GET"])
def api_get_submissions(): # for the submissions.html webpage
    return flask.jsonify(submissions)


if __name__ == "__main__":
    server.run(port=8000, host="0.0.0.0", debug=True)