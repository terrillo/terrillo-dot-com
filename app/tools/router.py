import datetime


def LOG(v):
    x = datetime.datetime.now()
    print("[{}] - {}".format(x.strftime("%x %X"), v))


def build_seo(request, obj):
    obj["path"] = request.path
    return obj
