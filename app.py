from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def todo():
    display = None

    if request.method == "POST":
        display = {
            "name": request.form.get("name", "").strip(),
            "title": request.form.get("title", "").strip(),
            "description": request.form.get("description", "").strip()
        }

    return render_template("index.html", display=display)

if __name__ == "__main__":
    app.run(debug=True)