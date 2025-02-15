from .base import SimpleHTTPRequestHendler
from .file import FileRequestHandler


class RestserverHandler(SimpleHTTPRequestHendler, FileRequestHandler):
    pass
