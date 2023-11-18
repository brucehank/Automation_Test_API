import requests
import json
from Log import *

log = Log()

class HttpClient(object):

    def __init__(self) -> None:
        self.session = requests.Session()

    #  API Send
    def request(self, requestMethod:str, requestUrl:str, paramsType:str, requestData:str = None, params:str = None, headers:str = None, **kwargs) -> json:
        
        if requestMethod == "post":
            
            print("---", type(requestData))

            if paramsType == "form":
                self.__request_log(url = requestUrl, method = requestMethod, data = requestData, headers = headers)
                response = self.__post(url = requestUrl, data = json.dumps(eval(requestData)),headers = headers, **kwargs)
                self.__response_log(response)
                return response
            elif paramsType == "json":
                self.__request_log(url = requestUrl, method = requestMethod, jsonData = requestData, headers = headers)
                response = self.__post(url = requestUrl, json = json.dumps(eval(requestData)),headers = headers, **kwargs)
                self.__response_log(response)
            
                return response
        elif requestMethod == "get":
            
            if paramsType == "url":
                self.__request_log(url = requestUrl, method = requestMethod, params = params ,headers = headers)
                response = self.__get(url = requestUrl, params = params, headers = headers, **kwargs)
                self.__response_log(response)
            
                return response

    #  POST 
    def __post(self, url, data = None, json = None, headers=None,**kwargs):
        response = self.session.post(url=url, data = data, json=json, headers = headers)
        return response

    #  GET
    def __get(self, url, params = None, headers = None, **kwargs):
        response = self.session.get(url, params = params, headers=headers, **kwargs)
        return response
    
    #  Request log
    def __request_log(self, url, method, data=None, jsonData=None, params=None, headers=None):
        log.debug("API Request Url: {}".format(url))
        log.debug("API Request Method: {}".format(method))
        log.debug("API Request Headers: {}".format(json.dumps(headers, indent=4, ensure_ascii=False)))
        log.debug("API Request params: {}".format(json.dumps(params, indent=4, ensure_ascii=False)))
        log.debug("API Request data: {}".format(json.dumps(data, indent=4, ensure_ascii=False)))
        log.debug("API Request json: {}".format(json.dumps(jsonData, indent=4, ensure_ascii=False)))

    #  Response log
    def __response_log(self, resp):
        try:
            resp.raise_for_status()
            log.debug("Response Message: {}".format(resp.text, ensure_ascii=False))
        except requests.exceptions.HTTPError as e:
            log.error("Status Code Error: {}".format(e))
        except requests.exceptions.InvalidURL as e:
            log.error("Invalid URL: {}".format(e))
        except requests.exceptions.RequestException as e:
            log.error("Requests Error: {}".format(e))
        except Exception as e:
            log.error("Response Error: {}".format(e))

            