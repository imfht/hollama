import flask
app = flask.Flask(__name__)
from models import PathSetting
# init sqlalchemy
from models import db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index(subpath):
    # load path setting from database
    path_setting = PathSetting.query.filter_by(path=subpath).first()
    if path_setting is None:
        return 'Path not found', 404
    if path_setting.response_as_json:
        return flask.jsonify(flask.json.loads(path_setting.response))
    else:
        return path_setting.responsel

if __name__ == '__main__':
    app.run(debug=True)