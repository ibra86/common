from flask import jsonify
from werkzeug.exceptions import HTTPException


def page_not_found(e):
    code = 404
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code