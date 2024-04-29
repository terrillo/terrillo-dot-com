import os

import yaml
import marko
import simplejson as json

from flask import Flask, request, render_template, abort, redirect, send_file
from flask_cors import CORS
from flask_caching import Cache

from tools.router import LOG, build_seo
from blueprints.seo import SEO

# Flask Config
app = Flask(__name__)
app.secret_key = "HGf42hr5Qrw7wTU2"

# Flask CORS
CORS(app)

# Flask Caching
config = {
    "CACHE_TYPE": "filesystem",
    "CACHE_DEFAULT_TIMEOUT": 1800,
    "CACHE_DIR": "/app/cache/flask/",
    "CACHE_KEY_PREFIX": "flask_",
}
app.config.from_mapping(config)
cache = Cache(app)


@app.before_request
def before_request():
    # HTTPS redirect
    if "http://terrillo.com" in request.host_url:
        return redirect(request.url.replace("http:", "https:"))

    # ENV
    if request.host == "localhost":
        app.jinja_env.cache = {}
        os.system("rm -rf /app/cache/flask/*")
    else:
        # PROD
        pass

    # Logging
    if not request.method == "OPTIONS" and request.method:
        LOG(str(request.url_rule))


@app.after_request
def after_request(response):
    # Headers
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response


@app.route("/", methods=["GET"])
@cache.cached(timeout=600)
def homepage():
    return render_template(
        "home.html",
        SEO=build_seo(
            request,
            {
                "title": "About",
                "description": "Software Consultant & Software Engineer",
            },
        ),
        HOME=True,
    )


@app.route("/favicon.ico", methods=["GET"])
@cache.cached(timeout=600)
def favicon():
    return send_file("/app/static/images/favicon.png", mimetype="image/png")


@app.route("/blog/", methods=["GET"])
@cache.cached()
def blog():
    POSTS = []
    POSTS_LIST = os.listdir("./blog/")
    POSTS_LIST.reverse()
    for post in POSTS_LIST:
        if ".yml" in post:
            with open("./blog/" + post, "r") as file:
                POST_OBJECT = yaml.safe_load(file)
                POST_OBJECT["slug"] = post.replace(".yml", "") + "/"
                POSTS.append(POST_OBJECT)
    return render_template(
        "blog.html",
        SEO=build_seo(
            request, {"title": "Blog", "description": "The writings of Terrillo Walls"}
        ),
        posts=POSTS,
    )


@app.route("/article/<slug>/", methods=["GET"])
@cache.cached()
def article(slug):
    POST_DATA = {}
    POST_META = False
    for post in os.listdir("./blog/"):
        if slug in post:
            if ".yml" in post:
                with open("./blog/" + post, "r") as file:
                    POST_META = yaml.safe_load(file)
                    POST_META["slug"] = post.replace(".yml", "")
            if ".md" in post:
                POST_DATA["html"] = marko.convert(open("./blog/" + post, "r").read())

    if "videos" in POST_META:
        for video in POST_META["videos"].keys():
            EMBED = """
           <iframe src="https://www.youtube.com/embed/{}" width="1920" height="1080" allowfullscreen uk-responsive uk-video="autoplay: false" class="mt2"></iframe>
            """.format(
                POST_META["videos"][video]
            )
            POST_DATA["html"] = POST_DATA["html"].replace(
                "<p>[[{}]]".format(video), EMBED
            )

    if not POST_META:
        return abort(404)

    return render_template(
        "article.html", SEO=build_seo(request, POST_META), post=POST_DATA
    )


# 404
@app.errorhandler(404)
@app.route("/<path:invalid_path>")
def handle_unmatchable(*args, **kwargs):
    return redirect("/", code=301)


# 500
@app.errorhandler(500)
@app.errorhandler(502)
def handle_servererror(*args, **kwargs):
    return (
        render_template(
            "500.html",
            SEO=build_seo(
                request, {"title": "Server Error", "description": "Server Error"}
            ),
        ),
        200,
    )


# Blueprints
app.register_blueprint(SEO, url_prefix="/")

# Main
if __name__ == "__main__":
    os.system("rm -rf /app/cache/flask/*")
    app.run(host="0.0.0.0", port=80, debug=True)
