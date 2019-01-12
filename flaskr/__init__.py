import os

from flask import Flask
from flask import render_template
<<<<<<< HEAD
from flask import request
from flask import Response
from nltk.sentiment.vader import SentimentIntensityAnalyzer
=======
from flask import jsonify

>>>>>>> 3eb0dd63c754ca9d9acd1a35117054b5f43d8e00


def create_app(test_config=None):
    # create and configure the app

    app = Flask(__name__, instance_relative_config=True, template_folder='template')
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/index')
    def index():

        return render_template("./index.html", title='Home')

    @app.route('/demo')
    def demo():
        return render_template("./demo.html", title='Home')


    @app.route('/background_process_test')
    def background_process_test():
        print ("Hello")
        return "nothing"

    @app.route('/loadDoc')
    def loadDoc():
        ind = int(request.args.get("id"))
        resource_path = os.path.join(app.root_path, 'news_reuters.csv')
        with open(resource_path, encoding = 'UTF-8') as f:
            for num, line in enumerate(f):
                if num < ind:
                    continue
                else:
                    sia = SentimentIntensityAnalyzer()
                    line = line.strip().split(',')
                    if len(line) not in [6, 7]:
                        continue
                    if len(line) == 6:
                        ticker, name, day, headline, body, newsType = line
                    else:
                        ticker, name, day, headline, body, newsType, suggestion = line
                    content = headline + ' ' + body
                    pscores = sia.polarity_scores(content)['compound']
                    print("scoresss" + str(pscores))
                    return str(pscores),200
            return Response("{}", status=201, mimetype='application/json')



    @app.route('/background_process_test')
    def background_process_test():
        res = {'msg':'you got it'}
        return jsonify(res)

    return app
