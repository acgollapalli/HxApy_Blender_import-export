
from datetime import datetime


def TS():
    return datetime.now().strftime("%d%m%y-%H%M%S")


def DS(start, end):
    delta = end - start
    s = delta.seconds

    h = s // 3600
    s = s - (h*3600)
    m = s // 60
    s = s - (m*60)

    if (h > 0):
        return f"Done in: {h}h{m}m{s}s"
    elif (m > 0):
        return f"Done in: {m}m{s}s"
    elif (s > 0):
        return f"Done in: {s}s"


def FlattenList_1(_list):
    res = []
    for inner in _list:
        for el in inner:
            res.append(el)
    return res


def RestoreFaces(references):
    faces = []
    tupl = []
    for r in references:
        if (r < 0):
            r = -r - 1
            tupl.append(r)
            faces.append(tuple(tupl))
            tupl = []
        else:
            tupl.append(r)
    return faces


def BreakUp(data, length, step):
    return [tuple(data[x:x+step]) for x in list(range(0, length, step))]
