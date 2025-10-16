from flask import Flask, render_template, redirect, request
app = Flask (__name__)

@app.route("/")
def check():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run()