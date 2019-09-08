import random
from flask import Flask, render_template as rend
app = Flask(__name__)
frettir = {"1":["yeet", "maður yeetaði"]}
@app.route('/')
def index():
	return rend("base.html", title="index") + '<h1>oh hi there</h1>'
@app.route("/<frett>")
def frett(frett):
	return rend("base.html", title=frettir[frett][0], content=frettir[frett][1])

if __name__ == "__main__":
	app.run(debug=True)