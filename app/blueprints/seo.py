import os
import moment
import yaml
import marko

from flask import Blueprint, render_template, Response

SEO = Blueprint("SEO", __name__)
SEO_MAP = [
    ("/", "home.html"),
    ("/blog/", "blog.html"),
]


@SEO.route("/sitemap.xml", methods=["GET"])
def sitemap():
    SITES = []

    # Static Pages
    for site in SEO_MAP:
        if os.path.isfile("/app/templates/%s" % (site[1])):
            f = os.stat("/app/templates/%s" % (site[1]))
            DATE = moment.unix(f.st_mtime, utc=True).format("YYYY-M-D")
            SITES.append(
                {
                    "path": site[0],
                    "lastmod": DATE,
                }
            )

    # Blog Posts
    for post in os.listdir("./blog/"):
        if ".yml" in post:
            f = os.stat("./blog/" + post)
            DATE = moment.unix(f.st_mtime, utc=True).format("YYYY-M-D")
            SITES.append(
                {
                    "path": "/article/" + post.replace(".yml", "") + "/",
                    "lastmod": DATE,
                }
            )

    resp = Response(
        render_template("sitemap.xml", SITES=SITES), mimetype="application/xml"
    )
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@SEO.route("/robots.txt")
def robots():
    resp = Response(render_template("robots.txt"), mimetype="text/plain")
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp


@SEO.route("/feed/")
def feed():
    POSTS = []
    POSTS_LIST = os.listdir("./blog/")
    POSTS_LIST.reverse()
    for post in POSTS_LIST:
        if ".yml" in post:
            with open("./blog/" + post, "r") as file:
                POST_OBJECT = yaml.safe_load(file)
                POST_OBJECT["slug"] = post.replace(".yml", "") + "/"
                f = os.stat("./blog/" + post)
                POST_OBJECT["date"] = moment.unix(f.st_mtime, utc=True).strftime(
                    "%a, %d %b %Y %H:%M:%S %z"
                )
                POST_OBJECT["html"] = marko.convert(
                    open("./blog/" + post.replace(".yml", ".md"), "r").read()
                )
                if "videos" in POST_OBJECT:
                    for video in POST_OBJECT["videos"].keys():
                        EMBED = """
                    <iframe src="https://www.youtube.com/embed/{}" width="1920" height="1080" allowfullscreen uk-responsive uk-video="autoplay: false" class="mt2"></iframe>
                        """.format(
                            POST_OBJECT["videos"][video]
                        )
                        POST_OBJECT["html"] = POST_OBJECT["html"].replace(
                            "<p>[[{}]]".format(video), EMBED
                        )

                POSTS.append(POST_OBJECT)

    resp = Response(render_template("rss.xml", POSTS=POSTS), mimetype="application/xml")
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp
