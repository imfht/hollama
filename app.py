import flask
app = flask.Flask(__name__)
from models import PathSetting,RequestLog
# init sqlalchemy
from models import db
import json
from flask import request
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    path_setting = PathSetting.query.filter_by(path='').first()
    if path_setting.response_as_json:
        return flask.jsonify(flask.json.loads(path_setting.response))
    else:
        return path_setting.response

@app.before_request
def before_request():
    request_info = {
        'ip_addr': request.remote_addr,
        'path': request.path,
        'method': request.method,
        'headers': json.dumps(dict(request.headers)),
        'data': request.get_data(as_text=True),
        'remote_addr': request.remote_addr
    }
    # 创建 RequestLog 实例
    log_entry = RequestLog(**request_info)
    # 保存到数据库
    db.session.add(log_entry)
    db.session.commit()
    
@app.route('/<path:subpath>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def anypage(subpath):
    # load path setting from database
    print('subpatch is ', subpath)
    path_setting = PathSetting.query.filter_by(path=subpath).first()
    if path_setting is None:
        return 'Path not found', 404
    if path_setting.response_as_json:
        return flask.jsonify(flask.json.loads(path_setting.response))
    else:
        return path_setting.response

if __name__ == '__main__':
    app.run(debug=False, port=11434)