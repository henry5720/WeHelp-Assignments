from flask import Flask
from . import config

from .routes.index import index_bp
from .routes.member import member_bp
from .routes.check import check_bp
from .routes.signup import signup_bp

def create_app():
    # 建立 Application > 設定 static 路徑
    app = Flask(
                    __name__,
                    static_folder="static",
                    static_url_path="/"
                )
                
    # 設定配置文件
    app.config.from_object(config)

    # 設定session 密鑰
    app.secret_key="something cryptic"
    
    # 登錄藍圖
    app.register_blueprint(index_bp)
    app.register_blueprint(member_bp)
    app.register_blueprint(check_bp)
    app.register_blueprint(signup_bp)
    
    ''' not sure
    配置 > 連線資料庫資料 
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '0973'
    app.config['MYSQL_DATABASE'] = 'website'
    '''

    return app 