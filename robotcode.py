from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/robotcode/line/<feet>')
def straight(feet=None):
	seconds = int(feet) * 1000
	return render_template('code.html', feet=feet, seconds=seconds)

@app.route('/robotcode/square/<feet>')
def square(feet=None):
	seconds = int(feet) * 1000
	return render_template('squarecode.html', feet=feet, seconds=seconds)

@app.route('/robotcode/hexagon/<feet>')
def hex(feet=None):
	seconds = int(feet) * 1000
	return render_template('hexagoncode.html', feet=feet, seconds=seconds)

@app.route('/robotcode/trick1/<feet>')
def neat(feet=None):
	seconds = int(feet) * 1000
	return render_template('trick1.html', feet=feet, seconds=seconds)

if __name__ == '__main__':
    app.run(debug=True)