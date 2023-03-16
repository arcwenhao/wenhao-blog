from flask import Flask, render_template, request
import requests
from smtplib import SMTP

MY_EMAIL = "wenhaoarcdesign@gmail.com"
MY_PASSWORD = "idrwhxtshesyvirm"

app = Flask(__name__)


@app.route("/")
def home():
    blog_data = requests.get("https://api.npoint.io/0a69203c71746f3dcbdf").json()
    return render_template("index.html", blogs=blog_data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg="Subject: New Contact Message\n\n"
                                    f"Name: {request.form['name']}\n"
                                    f"Email: {request.form['email']}\n"
                                    f"Phone: {request.form['phone']}\n"
                                    f"Message: {request.form['message']}\n")
    return render_template("contact.html")





@app.route("/post/<int:post_id>")
def post(post_id):
    blog_data = requests.get("https://api.npoint.io/0a69203c71746f3dcbdf").json()
    return render_template("post.html", id=post_id, blogs=blog_data)


if __name__ == "__main__":
    app.run(debug=True)