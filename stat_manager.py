def stat_book_category(db):
    """图书分类统计 aggregate"""
    coll = db["books"]
    pipe = [{"$group": {"_id": "$category", "book_count": {"$sum": 1}}}]
    res = list(coll.aggregate(pipe))
    return res

def stat_borrow_trend(db):
    """借阅趋势"""
    coll = db["borrow_logs"]
    pipe = [
        {"$group": {"_id": "$borrow_month", "borrow_count": {"$sum":1}}},
        {"$sort": {"_id": 1}}
    ]
    res = list(coll.aggregate(pipe))
    return res

def stat_book_sales_rank(db):
    """图书借阅畅销榜"""
    coll = db["borrow_logs"]
    pipe = [
        {"$group": {"_id": "$book_name", "borrow_times": {"$sum":1}}},
        {"$sort": {"borrow_times": -1}}
    ]
    res = list(coll.aggregate(pipe))
    return res
