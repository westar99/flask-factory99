from flask import Blueprint, render_template

bp = Blueprint('dashapp3',
                __name__,
                template_folder = 'templates',
                url_prefix="/dashapp3/")

@bp.route('/',methods=['GET'])
def main():
    return render_template('dashapp3.jinja2',title="Main Page")