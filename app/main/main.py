from flask import Blueprint, render_template

bp = Blueprint('main',
                __name__,
                template_folder = 'templates',
                url_prefix="/main")

@bp.route('/',methods=['GET'])
def main():
    return render_template('main.jinja2',title="Main Page")