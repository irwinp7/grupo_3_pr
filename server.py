from flask import Flask, render_template

app = Flask(__name__)
@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":

    ip = "172.31.14.211"
    port = "80"
    app.run (ip,port)