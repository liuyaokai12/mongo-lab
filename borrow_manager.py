def borrow_book_register(db, borrow_doc):
    """借阅登记 insert_one"""
    coll = db["borrow_logs"]
    ret = coll.insert_one(borrow_doc)
    print(f"借阅登记成功，受影响文档数：1，_id={ret.inserted_id}")

def return_book_handle(db, filter_doc):
    """归还处理 update_many"""
    coll = db["borrow_logs"]
    ret = coll.update_many(filter_doc, {"$set": {"status": "已归还"}})
    print(f"归还处理完成，受影响文档数：{ret.modified_count}")

def query_overdue_borrow(db):
    """逾期查询 find"""
    coll = db["borrow_logs"]
    res = list(coll.find({"status": "借阅中", "overdue": True}))
    if len(res) == 0:
        print("【提示】暂无逾期借阅记录！")
    return res

def query_all_borrow(db, filter_doc=None):
    coll = db["borrow_logs"]
    if filter_doc is None:
        filter_doc = {}
    res = list(coll.find(filter_doc))
    if len(res) == 0:
        print("【提示】没有对应的借阅记录！")
    return res
