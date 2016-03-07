from flask import Flask,render_template,url_for
from remote import Remote

app = Flask(__name__,static_url_path='/static')



@app.route('/')
def index():
	return render_template('index.html')


@app.route('/remote/<cmd>')
def remote(cmd):
	r=Remote()
	if cmd == "on":
		r.on()
	else:
		r.off()

	return "ok"







if __name__=='__main__':

	app.run('0.0.0.0',port=7000,debug=True)