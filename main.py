from flask import Flask,jsonify

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
        }

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user", methods = ["GET"])
def get_user():
    yerbolat = User(name = "Yerbolat", age = 33)
    return jsonify(yerbolat.serialize())

@app.route("/users", methods = ["GET"])
def get_users():
    userlist = []
    user1 = User("Vasya", 18)
    user2 = User("John", 28)
    userlist.append(user1.serialize())
    userlist.append(user2.serialize())
    return jsonify(userlist)

if __name__ == "__main__":
    app.run()

