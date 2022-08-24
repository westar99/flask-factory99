import os

from flask import Flask,render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'development'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/')
    def hello():
        return render_template('index.jinja2',title='index page')
    
    from .main import main
    #from .dashapp1 import dashapp1
    from .dashapp1 import bp as bp_dashapp1
    from .dashapp1.dashapp1 import add_dash
    from .dashapp2 import dashapp2
    from .dashapp3 import dashapp3
    
    app.register_blueprint(main.bp)#main.py 에서 bp를 가져옴
    #app.register_blueprint(dashapp1.bp)#dashapp1.py 에서 bp를 가져옴
    app.register_blueprint(bp_dashapp1)
    app.register_blueprint(dashapp2.bp)#dashapp2.py 에서 bp를 가져옴
    app.register_blueprint(dashapp3.bp)
    
    app = add_dash(app)
    return app 