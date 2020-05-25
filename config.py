import os
here = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    配置基类
    """
    SECRET_KEY = '#+^aOjdlPHFD09)&*2P3JR-0CFE)&H12EAa;OPFG=0'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN = 'email@qq.com'
   
    FLASK_POSTS_PER_PAGE = 15 #15#每一页显示15条微博
    MAX_POSTS_PER_PAGE = 50 #前50条微博里寻找热门微博
    MAIL_USE_SSL = True
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'email@qq.com'
    MAIL_PASSWORD = '授权码'
    FLASK_MAIL_SENDER = '微博团队<2298770114@qq.com>'
    FLASK_MAIL_SUBJECT_PREFIX = '[微博]'

 #FLASK_HOTPOSTS_PER_PAGE = 10 #显示最热的10条微博
 
class DevelopmentConfig(Config):
    """
    开发状态
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-dev.sqlite')

class TestingEmptyConfig(Config):
    """
    测试状态：数据库无数据
    """
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-test-empty.sqlite')


class TestingFullConfig(TestingEmptyConfig):
    """
    测试状态：数据库有数据
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-test-full.sqlite')


class ProductionConfig(Config):
    """
    生产状态
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(here, 'data-prod.sqlite')


class HerokuConfig(Config):
    """
    Heroku平台配置
    """
    SSL_DISABLE = False     # 启动 SLL 安全检查
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    @classmethod
    def init_app(cls, app):
        # 将日志输出到 stderr
        import logging
        file_handler = logging.StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)
        # 处理代理服务器首部。在 Heroku 中，客户端没有直接托管程序，而是连接反向服务
        # 代理器，最后把请求重定向到程序上。这种连接方式中，只在代理服务器中运行 SSL 模式。
        from werkzeug.contrib.fixers import ProxyFix#使用werkzegu包来应付proxyfix
        app.wsgi_app = ProxyFix(app.wsgi_app)


config = {
    'development': DevelopmentConfig,
    'testing-empty': TestingEmptyConfig,
    'testing-full': TestingFullConfig,
    'production': ProductionConfig,
    'heroku': HerokuConfig,
    'default': DevelopmentConfig
}
