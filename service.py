from meme_parser import MemeParser
from r_queries import R_Queries
from db_interraction import DatabaseInterraction
from json import loads

SR_LINK = "http://www.reddit.com/r/"

class Service():
    def __init__(self):
        self.init_db()
    
    def _get_uri(self):
        with open(".db_uri", "r") as file:
            uri = file.readline().strip("\n").strip()
        return uri
    
    def init_db(self):
        self.db = DatabaseInterraction(self._get_uri(), "memes", "memes")
        
    # return an url of the meme picture
    def get_random_meme(self, sr: str) -> str:
        return self.db.get_random_meme(sr)
    
    def add_memes(self, sr: str):
        query = R_Queries(SR_LINK + sr + "/new.json")
        size = self.db.get_sr_size(sr)
        response = query.get_recent(100)
        memes = loads(response.text)
        while "data" not in memes:
            response = query.get_recent(100)
            memes = loads(response.text)
        obj_memes = MemeParser(size, memes["data"]["children"])
        self.db.add_memes(sr, obj_memes)