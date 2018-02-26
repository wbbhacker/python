from flask import Flask
app = Flask(__name__)

application = app

@app.route('/')
def hello_world():
    return 'Hello, World!sss'

if __name__ == '__main__':
	app.run()