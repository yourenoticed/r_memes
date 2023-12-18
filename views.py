import requests
from flask import Blueprint, render_template
from random import randrange
from json import loads

views = Blueprint(__name__, "views")

@views.route("/<sr>")
def index(sr: str):
    subreddit = "http://www.reddit.com/r/" + sr + ".json"
    image_src = get_image_src(subreddit)
    return render_template("index.html", image_src=image_src)

def get_image_src(subreddit: str) -> str:
    response = requests.get(subreddit)
    sr = loads(response.text)
    while "data" not in sr:
        response = requests.get(subreddit)
        sr = loads(response.text)
    posts = sr["data"]["children"]
    post_i = get_random(posts)
    return posts[post_i]["data"]["url"]

def get_random(children_json: dict) -> int:
    range_limit = len(children_json)
    ind = randrange(1, range_limit)
    while "data" not in children_json[ind] or children_json[ind]["data"]["post_hint"] != "image":
        ind += 1
    return ind