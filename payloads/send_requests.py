import requests


class SendRequests:
    def __init__(self):
        super().__init__()

    def GET(self, url):
        r = requests.get(url)
        return str(r.headers)

    def POST(self, url):
        r = requests.get(url)
        return str(r.status_code)


r = SendRequests()
