import os
import toml
import moment

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

from .tools import markdown_parser

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="/static"), name="static")

templates = Jinja2Templates(directory="/code/app/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(
        "home.jinja",
        {
            "request": request,
            "SEO": {
                "title": "About",
                "description": "Software Consultant &amp; Software Engineer",
                "type": "website",
                "image": "terrillo-m-walls.jpg",
            },
        },
    )


@app.get("/send-email")
def send(request: Request):
    return templates.TemplateResponse("send.jinja", {"request": request})


@app.get("/blog/")
def blog(request: Request):
    # Blog
    POSTS = []
    POSTS_LIST = os.listdir("/code/app/blog/")
    POSTS_LIST.reverse()
    for post in POSTS_LIST:
        if ".toml" in post:
            POST_OBJECT = toml.loads(open(f"/code/app/blog/{post}", "r").read())
            POST_OBJECT["slug"] = post.replace(".toml", "")
            POSTS.append(POST_OBJECT)

    POSTS = sorted(POSTS, key=lambda d: d["slug"], reverse=True)[:3]

    return templates.TemplateResponse(
        "blog/landing.jinja",
        {
            "request": request,
            "SEO": {
                "title": "Blog",
                "description": "Khabin Technology Company & Products Updates",
                "type": "website",
                "image": "terrillo-m-walls.jpg",
            },
            "posts": POSTS,
        },
    )


@app.get("/blog/{slug}/")
def article(request: Request, slug):
    try:
        POST_OBJECT = toml.loads(
            open(f"/code/app/blog/{slug}.toml", "r").read()
        )
    except:
        raise HTTPException(status_code=404)

    if "markdown" in POST_OBJECT:
        POST_OBJECT["html"] = markdown_parser(POST_OBJECT["markdown"])

    IMAGE = None
    if "image" in POST_OBJECT:
        IMAGE = "static/images/blog/" + POST_OBJECT["image"]

    return templates.TemplateResponse(
        "blog/article.jinja",
        {
            "request": request,
            "SEO": {
                "title": POST_OBJECT["title"],
                "description": POST_OBJECT["description"],
                "type": "article",
                "image": IMAGE,
            },
            "post": POST_OBJECT,
        },
    )


@app.get("/sitemap.xml")
def sitemap(request: Request):
    SITES = []
    STATIC = [
        ("/", "home.jinja", "1.0"),
        ("/blog/", "blog/landing.jinja", "0.9"),
    ]

    for page in STATIC:
        if os.path.isfile("/code/app/templates/%s" % (page[1])):
            f = os.stat("/code/app/templates/%s" % (page[1]))
            DATE = moment.unix(f.st_mtime, utc=True).format("YYYY-M-D")
            SITES.append(
                {
                    "path": page[0],
                    "lastmod": DATE,
                    "priority": page[2],
                }
            )

    POSTS_LIST = os.listdir("/code/app/blog/")
    POSTS_LIST.reverse()
    for post in POSTS_LIST:
        if ".toml" in post:
            f = os.stat("/code/app/blog/%s" % (post))
            DATE = moment.unix(f.st_mtime, utc=True).format("YYYY-M-D")
            SITES.append(
                {
                    "path": "/blog/" + post.replace(".toml", "") + "/",
                    "lastmod": DATE,
                    "priority": "0.8",
                }
            )

    return templates.TemplateResponse(
        "sitemap.xml",
        {"request": request, "SITES": SITES},
        media_type="application/xml",
    )


@app.get("/robots.txt")
def robots(request: Request):
    return templates.TemplateResponse(
        "robots.txt",
        {"request": request},
        media_type="text/plain",
    )


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/")
