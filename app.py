import random
from flask import Flask, render_template as rend
app = Flask(__name__)
frettir = {
	"1":["yeet", "maður yeetaði"],
	"2":[]
	}
@app.route('/')
def index():
	return rend("frettir.html", title="index", frettir=frettir.keys())
@app.route("/<frett>")
def frett(frett):
	if frett in frettir.keys():
		return rend("frett.html", title=frettir[frett][0], content=frettir[frett][1])
	else:
		return page_not_found(None)
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return rend('404.html'), 404


if __name__ == "__main__":
	app.run(debug=True)