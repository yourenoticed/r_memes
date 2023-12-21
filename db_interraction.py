import pymongo
from random import randrange
from meme import Meme

class DatabaseInterraction():
    def __init__(self, uri: str, db: str, collection: str):
        self.cluster = pymongo.MongoClient(uri)
        self.db = self.cluster.get_database(db)
        self.collection = self.db.get_collection(collection)
        
    def get_sr_size(self, sr: str) -> int:
        sub_r = self.collection.find_one({"subreddit": sr})
        if sub_r is not None:
            return sub_r["size"] 
        return 0
    
    def add_memes(self, sr: str, memes: list[Meme]):
        sub_r = self.collection.find_one({"subreddit": sr})
        if sub_r is None:
            self.collection.insert_one({"_id": self.get_collection_size(), "subreddit": sr, "size": len(memes), "posts": memes})
        else:
            for meme in memes:
                if self.collection[{"subreddit": sr}]["posts"].find_one({"name": meme["name"]}) is None:
                    size = sub_r["size"] 
                    sub_memes = sub_r["posts"]
                    self.collection[{"subreddit": sr}].update_one({"posts": sub_memes}, {"$addToSet": {"posts" : [meme]}}) 
                    self.collection[{"subreddit": sr}].update_one({"size": size}, {"$set": {"size": size + 1}})
                else: 
                    break
        
    def get_random_meme(self, sr: str) -> str:
        posts = self.collection.find_one({"subreddit": sr})["posts"]
        if posts is not None:
            return posts[self.get_random_id(sr)]["url"]
        
    
    def get_random_id(self, sr: str) -> int:
        num = randrange(0, self.get_sr_size(sr))
        return num
    
    def get_last_name(self, sr: str) -> int:
        return self.collection.find_one({"subreddit": sr})["posts"][self.get_sr_size(sr) - 1]["name"]
    
    def get_collection_size(self) -> int:
        return self.collection.estimated_document_count()

  
