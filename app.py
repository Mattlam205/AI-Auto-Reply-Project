from flask import Flask,render_template,request
import ollama

app = Flask(__name__)

@app.route("/", methods =["GET", "POST"])

def home():
    ai_response = ""
    user_message = ""

    if request.method == "POST":
        user_message = request.form["message"]

        if user_message.strip() != "":
            response = ollama.chat(
             model = "llama3",
             messages =[
                {"role": "user", "content" : user_message}
                ]
        )

        ai_response = response["message"]["content"]

    return render_template("index.html", user_message = user_message , ai_response = ai_response)

app.run(debug=True)