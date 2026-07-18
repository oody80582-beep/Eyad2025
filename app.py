from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/games")
def games():
    return render_template("games.html")


@app.route("/racing")
def racing():
    return render_template("racing.html")


@app.route("/openworld")
def openworld():
    return render_template("openworld.html")


@app.route("/action")
def action():
    return render_template("action.html")


@app.route("/sports")
def sports():
    return render_template("sports.html")


@app.route("/puzzle")
def puzzle():
    return render_template("puzzle.html")


@app.route("/horror")
def horror():
    return render_template("horror.html")


# صفحات الألعاب

@app.route("/asphalt")
def asphalt():
    return render_template("asphalt.html")


@app.route("/gta5")
def gta5():
    return render_template("gta5.html")


@app.route("/fcmobile")
def fcmobile():
    return render_template("fcmobile.html")


@app.route("/braintest")
def braintest():
    return render_template("braintest.html")


@app.route("/granny")
def granny():
    return render_template("granny.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
