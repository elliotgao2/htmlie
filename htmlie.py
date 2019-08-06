import sys

import click
from pyquery import PyQuery as pq


def main():
    r = ""
    if sys.argv[-1].startswith(":"):
        attr = sys.argv.pop(-1).split(":")[-1]
    else:
        attr = "outer_html"
    selector = " ".join(sys.argv[1:])
    if not sys.stdin.isatty():
        data = sys.stdin.read()
        d = pq(data).xhtml_to_html()
        if attr == "text":
            r = [pq(i).text() for i in d(selector)]
        elif attr == "html":
            r = [pq(i).html() for i in d(selector)]
        elif attr == "outer_html":
            r = [pq(i).outer_html() for i in d(selector)]
        elif attr == "json":
            r = []
            for i in d(selector):
                dd = pq(i)
                r.append(
                    {
                        "tag": i.tag,
                        "href": dd.attr("href"),
                        "title": dd.attr("title"),
                        "text": dd.attr("text"),
                        "src": dd.attr("src"),
                        "class": dd.attr("class"),
                    }
                )
        else:
            r = [pq(i).attr(attr) for i in d(selector)]
    for i in r:
        print(i)
