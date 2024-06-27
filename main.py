from src.extract.http_requester import HttpRequester
import pprint

if __name__ == '__main__':
    response = HttpRequester()
    pprint.pprint(response.http_response())