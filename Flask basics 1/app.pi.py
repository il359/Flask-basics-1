from flask import Flask, render_template
import random

app = Flask(__name__)

my_college = "ASRJC"
rival_college = "ACJC"
secret_text = "Secret text"
secret_nums = [1111, 7722, 2, 991122334455667788]
secret_info = {"name": "DUSP", "description": "skjdf", "gender": "unknown", "type": "human"}
@app.route("/")
def home():
    return "<h1>Hello World!</h1><p>This is my page.</p>"

@app.route("/about")
def about():
    return render_template("about.html", my_college=my_college, rival_college=rival_college)

@app.route("/secret")
def secret():
    lucky_num = random.choice(secret_nums)
    return render_template("secret.html", secret_text=secret_text,lucky_num=lucky_num, secret_info=secret_info)
    

if __name__ == "__main__":
    app.run(debug=True, port=12345)
