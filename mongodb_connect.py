from pymongo import MongoClient

def get_db():
    # 创建连接
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["library"]
    return client, db
