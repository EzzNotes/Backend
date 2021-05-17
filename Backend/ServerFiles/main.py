from flask import Flask, Blueprint, request, url_for, redirect, make_response

Main = Blueprint("main", __name__)

@Main.route("/")
def index(): 
    return render_template("index.html")


# ------------------------------------------------------- Error Page ---------------------------------------------------

@Main.route('/<page_name>')
def other_page(page_name):
    response = make_response('The page named %s does not exist.' \
                            % page_name, 404)