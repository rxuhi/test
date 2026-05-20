from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/write", methods=["GET", "POST"])
def write():

    if request.method == "POST":

        title = request.form["title"]
        content = request.form["content"]
        mbti = request.form["mbti"]

        post = {
            "title": title,
            "content": content,
            "mbti": mbti,
            "likes": 0
        }

        posts.append(post)

        return redirect("/")

    return render_template("write.html")

@app.route("/like/<int:index>")
def like(index):

    posts[index]["likes"] += 1

    return redirect("/")

app.run(debug=True)
