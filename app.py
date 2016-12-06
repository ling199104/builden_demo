from flask import Flask,render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime
import temp_print


app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/')
def index():
	return render_template('index.html',current_time=datetime.utcnow())
"""
@app.route('/quiz/<name>')
def quiz(name):
	#name = getword.VocabularyQuiz(name)
	return render_template('quiz.html',name=temp_print.GetSubtitle(name))
	
@app.route('/quiz/')
def quiz2():
	#name = getword.VocabularyQuiz(name)
	return render_template('quiz.html',name=temp_print.GetSubtitle(44509))   
"""
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

if __name__ == "__main__":
	manager.run()