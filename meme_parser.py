from meme import Meme

class MemeParser():
    def __new__(self, start_id, sr_children):
        return self.get_memes(self, start_id, sr_children)

    def get_memes(self, start_id, sr_children) -> list:
        memes = list()
        for child in sr_children:
            if "data" in child and "post_hint" in child["data"] and child["data"]["post_hint"] == "image":
                memes.append(self.get_meme(self, start_id, child["data"]))
                start_id += 1
        return memes
            
    def get_meme(self, id, child_data):
        subreddit = child_data["subreddit"]
        name = child_data["name"]
        title = child_data["title"]
        url = child_data["url"]
        over_18 = child_data["over_18"]
        permalink = child_data["permalink"]
        meme = Meme(id, subreddit, name, title, url, over_18, permalink)
        return meme.get_json_obj()