from flask import Blueprint, render_template
from service import Service

views = Blueprint(__name__, "views")

@views.route("/<sr>")
def get_subreddit_memes(sr: str):
    service = Service()
    image_src = service.get_random_meme(sr)
    return render_template("index.html", image_src=image_src, subreddit=sr)