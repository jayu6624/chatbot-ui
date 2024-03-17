from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo




app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://Jaydeep:jaydeep%406624@cluster0.e1eiczn.mongodb.net/chatbot"
mongo = PyMongo(app)

@app.route("/")
def hello():
    chats= mongo.db.chats.find({})
    mychats = [chat for chat in chats]
    print(mychats)
    return render_template("index.html",mychats=mychats)

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        print(request.json)
        question=request.json.get("question")
        data = {"result":question}
        return jsonify(data)
    data = {"result": "In the quiet of dawn, whispers of dreams unfurl. The sun ignites hope, painting the sky with possibilities."}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
