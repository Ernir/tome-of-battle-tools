from bs4 import BeautifulSoup
from TomeOfBattle.settings import DEBUG


class BeautifulMiddleware(object):
    # Cleans up the HTML output.
    # Source :http://pyevolve.sourceforge.net/wordpress/?p=814
    def process_response(self, request, response):
        if not DEBUG:
            return response

        if response.status_code == 200:
            if response["content-type"].startswith("text/html"):
                beauty = BeautifulSoup(response.content)
                response.content = beauty.prettify()
        return response