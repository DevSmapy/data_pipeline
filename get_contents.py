from requests import get
#from xmltodict import parse
from xml.etree.ElementTree import fromstring as parse
from json import dumps

class GetContents:
    def __init__(self, url:str):
        self.url = url

    def _get_contents(self):
        return get(self.url).text
    
    def _convert_to_dict(self, contents:str):
        #return parse(contents)
        return parse(contents)
    
    def _convert_to_json(self, contents:dict):
        return [dumps(contents["response"]["body"]["items"]["item"], indent=4)]
    
    def get_contents(self):
        contents = self._get_contents()
        contents_dict = self._convert_to_dict(contents)
        contents_json = self._convert_to_json(contents_dict)
        return contents_json