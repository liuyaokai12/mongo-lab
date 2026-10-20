def query_reader(db, filter_doc=None):
    coll = db["readers"]
    if filter_doc is None:
        filter_doc = {}
    res = list(coll.find(filter_doc))
    if len(res) == 0:
        print("【提示】未找到匹配读者信息！")
    return res

def stat_reader_by_college(db):
    """学院人数统计 count_documents"""
    coll = db["readers"]
    college_list = coll.distinct("college")
    result = []
    for col in college_list:
        count = coll.count_documents({"college": col})
        result.append({"学院": col, "人数": count})
    return result

def reader_level_distribute(db):
    """读者等级分布 distinct"""
    coll = db["readers"]
    level_list = coll.distinct("level")
    result = []
    for lv in level_list:
        cnt = coll.count_documents({"level": lv})
        result.append({"读者等级": lv, "数量": cnt})
    return result
