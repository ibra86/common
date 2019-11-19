from flask import jsonify
from werkzeug.exceptions import HTTPException


def page_not_found(e):
    code = 404
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

# bp = Blueprint('errors', __name__)
#
# @bp.app_errorhandler(404)
# def handle_404(err):
#     return render_template('404.html'), 404
#
# @bp.app_errorhandler(500)
# def handle_500(err):
#     return render_template('500.html'), 500
