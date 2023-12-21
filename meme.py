class Meme():
    def __init__(self, id: int, subreddit: str, name: str, title: str, url: str, over_18: bool, permalink: str):
        self.id = id
        self.subreddit = subreddit
        self.name = name
        self.title = title
        self.url = url
        self.over_18 = over_18
        self.permalink = permalink
    
    def get_json_obj(self) -> dict:
        return dict({"subreddit": self.subreddit,\
                    "name": self.name,\
                    "title": self.title,\
                    "url": self.url,\
                    "over_18": self.over_18,\
                    "permalink": self.permalink})