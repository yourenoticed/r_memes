from requests import Response, get

class R_Queries():
    def __init__(self, link: str):
        self.link = link
        
    # limit is 25 by default up to 100
    def get_after(self, meme_name: str, limit=25) -> Response:
        return get(self.link + "?after=" + meme_name + "&?" + str(limit))
    
    def get_before(self, meme_name: str, limit=25) -> Response:
        return get(self.link + "?before=" + meme_name + "&?" + str(limit))
    
    def get_recent(self, limit=25) -> Response:
        return get(self.link + "?limit=" + str(limit))