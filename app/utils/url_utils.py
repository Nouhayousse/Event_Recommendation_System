# app/utils/url_utils.py

from urllib.parse import urlparse

def clean_url(url: str):

    if not url:
        return None

    parsed = urlparse(url)

    clean = (
        f"{parsed.scheme}://"
        f"{parsed.netloc}"
        f"{parsed.path}"
    )

    return clean.rstrip("/")