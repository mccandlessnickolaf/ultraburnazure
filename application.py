from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://afflat3d1.com/lnk.asp?o=12160&c=918273&a=279700&k=2D9CAC75146A2EB5C61F9C1709772156&l=15052", code=302)
