from flask import Flask, render_template

app = Flask(__name__)


@app.route("signin.html")
def sign_in():
    return render_template("signin.html")


@app.route('signup.html')
def sign_up():
    return render_template("signup.html")


@app.route('home.html')
def home():
    return render_template("home.html")


@app.route('about.html')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)