def add_book(db, book_doc):
    coll = db["books"]
    ret = coll.insert_one(book_doc)
    print(f"新增图书，受影响文档数：1，_id={ret.inserted_id}")

def add_book_many(db, book_list):
    coll = db["books"]
    ret = coll.insert_many(book_list)
    print(f"批量新增图书，受影响文档数：{len(ret.inserted_ids)}")

def query_book_one(db, filter_doc):
    coll = db["books"]
    res = coll.find_one(filter_doc)
    if res is None:
        print("【提示】未查询到该图书！")
    return res

def query_books(db, filter_doc=None):
    coll = db["books"]
    if filter_doc is None:
        filter_doc = {}
    res = list(coll.find(filter_doc))
    if len(res) == 0:
        print("【提示】未查询到匹配的图书记录！")
    return res

def query_books_sort_by_score(db, filter_doc=None):
    coll = db["books"]
    if filter_doc is None:
        filter_doc = {}
    # 修正：使用真实字段 rating
    res = list(coll.find(filter_doc).sort("rating", -1))
    if len(res) == 0:
        print("【提示】无图书数据！")
    return res

def update_book_one(db, filter_doc, new_data):
    coll = db["books"]
    ret = coll.update_one(filter_doc, {"$set": new_data})
    print(f"单条更新完成，受影响文档数：{ret.modified_count}")

def update_book_many(db, filter_doc, new_data):
    coll = db["books"]
    ret = coll.update_many(filter_doc, {"$set": new_data})
    print(f"批量更新完成，受影响文档数：{ret.modified_count}")

def delete_book_one(db, filter_doc):
    coll = db["books"]
    ret = coll.delete_one(filter_doc)
    print(f"单条删除完成，受影响文档数：{ret.deleted_count}")

def delete_book_many(db, filter_doc):
    coll = db["books"]
    ret = coll.delete_many(filter_doc)
    print(f"批量删除完成，受影响文档数：{ret.deleted_count}")
