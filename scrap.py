import sys
import base64
from Wappalyzer import Wappalyzer, WebPage
import warnings
warnings.filterwarnings("ignore", message="""Caught 'unbalanced parenthesis at position 119' compiling regex""", category=UserWarning )
import requests.structures as struc
import json
class scrap():
    def __init__(self,httpResponse,httpResponseHeaders,url):
        self.httpResponse=httpResponse
        self.httpResponseHeader=json.loads(httpResponseHeaders)
        self.httpResponseHeaderNoCaseSens=struc.CaseInsensitiveDict([])
        self.httpResponseHeaderNoCaseSens.update(self.httpResponseHeader)
        self.url=url
        #webpage = WebPage.new_from_url('https://www.facebook.com')
    def getTech(self):
        httpResponse=WebPage(self.url,self.httpResponse,self.httpResponseHeaderNoCaseSens)
        tech=Wappalyzer.latest().analyze(httpResponse)
        return tech
def main():
    message_bytes = base64.b64decode(sys.argv[1])
    headers_bytes=sys.argv[2]
    url=base64.b64decode(sys.argv[3])
    stream = scrap(message_bytes.decode('ascii'),headers_bytes,url)
    output = stream.getTech()
    print(output)
if __name__ == "__main__":
    main()
