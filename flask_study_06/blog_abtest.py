from flask import Flask, make_response, jsonify, request, render_template
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS

from blog_view import blog
from blog_control.user_mgmt import User
import os

# https를 쓰지 않을 경우, 보안 이슈로 에러가남 (다음 설정을 통해 http에서도 에러가 나지 않도록함)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path="/static")
app.secret_key = "dhsun2" # 서버를 띄울때마다 특별한 코드로 변경 할 수있도록 랜덤설정 장점으로 보안성이 좋을 수 있음
CORS(app)

app.register_blueprint(blog.blog_abtest, url_prefix='/blog')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong" # strong으로 설정하면 보안성이 조금더 강화됨

@login_manager.user_loader
def load_user(user_id):# 서버 실행시 유저 정보를 가져와야
    return User.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)

