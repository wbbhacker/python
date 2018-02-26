from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


# @app.route('/hello')
# def hello():
# 	return 'hello'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    

@app.route('/user/<username>')
def show_user_profile(username):
	return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
	return 'Post %s' % post_id

@app.route('/project/')
def project():
	return 'The project page'


@app.route('/about')
def about():
	return 'The about page'

# with app_request_content():
# 	print(index)