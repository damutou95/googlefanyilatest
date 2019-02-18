import pymongo


class GoogleFanyiPipeline(object):

    def __init__(self):
        host = '127.0.0.1'
        port = 27017
        user = 'root'
        db = 'googlefanyi'
        collection = 'fanyi'
        client = pymongo.MongoClient(host=host, port=port)
        mgd = client[db]
        self.post = mgd[collection]

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
