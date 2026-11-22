"""Check the Stanton testimonial and logo on disk or on a Netlify preview."""
import argparse
import hashlib
import struct
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlsplit
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
ROUTES = ("/", "/industries/marketing-pr-agencies")
LOGO = "/stanton-company-logo.png"


class Testimonial(HTMLParser):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.inside = False
        self.field = None
        self.logo = []
        self.words = {"blockquote": [], "figcaption": []}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "figure" and "case-quote" in attrs.get("class", "").split():
            self.inside = True
            self.count += 1
        if self.inside and tag == "img":
            self.logo.append((attrs.get("src"), attrs.get("alt")))
        if self.inside and tag in self.words:
            self.field = tag

    def handle_endtag(self, tag):
        if tag == self.field:
            self.field = None
        if tag == "figure":
            self.inside = False

    def handle_data(self, data):
        if self.inside and self.field:
            self.words[self.field].append(data)


def get_page(base, route):
    if base:
        with urlopen(urljoin(base, route), timeout=20) as response:
            assert response.status == 200 and response.headers.get_content_type() == "text/html", route
            return response.read().decode("utf-8")
    return (ROOT / ("index.html" if route == "/" else route[1:] + ".html")).read_text()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", help="Preview origin, e.g. https://deploy-preview-123--site.netlify.app")
    base = parser.parse_args().base_url
    reference = None
    asset = (ROOT / LOGO[1:]).read_bytes()
    assert asset.startswith(b"\x89PNG\r\n\x1a\n") and struct.unpack(">II", asset[16:24]) == (702, 171)
    for route in ROUTES:
        figure = Testimonial()
        figure.feed(get_page(base, route))
        assert figure.count == 1 and figure.logo == [(LOGO, "Stanton & Company")], (route, figure.logo)
        words = {key: " ".join(" ".join(parts).split()) for key, parts in figure.words.items()}
        assert words["blockquote"] and "Emily Michels" in words["figcaption"], (route, words)
        if reference is not None:
            assert reference == words, "Agency quote or attribution differs from homepage"
        reference = words
        if base:
            url = urljoin(urljoin(base, route), figure.logo[0][0])
            with urlopen(url, timeout=20) as response:
                assert response.status == 200 and response.headers.get_content_type() == "image/png", url
                assert urlsplit(response.url).path == LOGO, response.url
                assert hashlib.sha256(response.read()).digest() == hashlib.sha256(asset).digest(), url
        print(f"PASS {route}  {LOGO}  702 x 171")


if __name__ == "__main__":
    main()
