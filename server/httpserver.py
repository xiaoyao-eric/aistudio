from flask import request, Response, jsonify, redirect, render_template

from server import app

@app.route('/aistudio')
def portal():
    return render_template('index.html')