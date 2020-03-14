from flask import Flask
from flask import render_template

# app = Flask(__name__, template_folder='templates')
app = Flask(__name__)

@app.route('/')
def main():
	return "Hello Flask"
	# msg = "Hello Students"
	# return render_template('result.html', msg=msg)

if __name__ == '__main__':
	app.run(debug=True)