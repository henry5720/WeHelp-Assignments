from flask import Flask
# 載入 config.py > config{}
from .config import config 
from .views.index import index_bp
from .views.member import member_bp
from .views.check import check_bp
from .views.signup import signup_bp
from .api.search_api import search_bp
from .api.change_api import change_bp

def create_app(mode):
    # 建立 Application > 設定 static 路徑
    app = Flask(
                    __name__,
                    static_folder="static",
                    static_url_path="/"
                )
                
    # 設定配置文件
    app.config.from_object(config[mode])

    # 設定session 密鑰
    app.secret_key="something cryptic"
    
    # 登錄藍圖
    app.register_blueprint(index_bp)
    app.register_blueprint(member_bp)
    app.register_blueprint(check_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(search_bp)
    app.register_blueprint(change_bp)

    return app