from mongodb_connect import get_db
from book_manager import add_book, add_book_many, query_book_one, query_books, query_books_sort_by_score, update_book_one, delete_book_one
from reader_manager import query_reader, stat_reader_by_college, reader_level_distribute
from borrow_manager import borrow_book_register, return_book_handle, query_overdue_borrow, query_all_borrow
from stat_manager import stat_book_category, stat_borrow_trend, stat_book_sales_rank

def main():
    # 程序启动，连接数据库
    client, db = get_db()
    print("="*50)
    print("📚 图书管理系统启动")
    print("✅ MongoDB数据库连接成功")
    # 打印各集合文档总数
    cnt_books = db["books"].count_documents({})
    cnt_readers = db["readers"].count_documents({})
    cnt_borrow = db["borrow_logs"].count_documents({})
    print(f"books集合文档总数：{cnt_books}")
    print(f"readers集合文档总数：{cnt_readers}")
    print(f"borrow_logs集合文档总数：{cnt_borrow}")
    print("="*50)

    while True:
        print("\n========== 主菜单 ==========")
        print("1. 新增单本图书")
        print("2. 按书名查询单本图书")
        print("3. 按评分排序查询图书")
        print("4. 更新图书评分")
        print("5. 删除图书")
        print("6. 读者学院统计、等级分布")
        print("7. 借阅登记 / 归还处理")
        print("8. 查询逾期借阅记录")
        print("9. 图书分类统计 & 畅销榜")
        print("10.退出系统")
        choice = input("\n请输入功能序号：")

        if choice == "1":
            name = input("图书名称：")
            cat = input("图书分类：")
            score = float(input("图书评分："))
            # 修正字段 title、rating，匹配数据库
            doc = {"title": name, "category": cat, "rating": score}
            add_book(db, doc)

        elif choice == "2":
            bk_name = input("输入图书名称查询：")
            data = query_book_one(db, {"title": bk_name})
            if data:
                print(data)

        elif choice == "3":
            print("按评分从高到低展示全部图书")
            data = query_books_sort_by_score(db)
            for item in data:
                print(item)

        elif choice == "4":
            bk_name = input("待更新图书名称：")
            new_score = float(input("输入新评分："))
            update_book_one(db, {"title": bk_name}, {"rating": new_score})

        elif choice == "5":
            del_name = input("要删除的图书名称：")
            delete_book_one(db, {"title": del_name})

        elif choice == "6":
            print("\n【读者学院统计】")
            col_data = stat_reader_by_college(db)
            for item in col_data:
                print(item)
            print("\n【读者等级分布】")
            lv_data = reader_level_distribute(db)
            for item in lv_data:
                print(item)

        elif choice == "7":
            sub_opt = input("1.借阅登记  2.归还处理 请选择：")
            if sub_opt == "1":
                bkname = input("图书名称：")
                rname = input("读者姓名：")
                borrow_doc = {"book_name":bkname, "reader_name":rname, "status":"借阅中", "overdue":False, "borrow_month":"2026‑10"}
                borrow_book_register(db, borrow_doc)
            elif sub_opt == "2":
                bkname = input("归还图书名称：")
                rname = input("读者姓名：")
                return_book_handle(db, {"book_name":bkname, "reader_name":rname, "status":"借阅中"})

        elif choice == "8":
            print("【逾期借阅记录】")
            overdue_data = query_overdue_borrow(db)
            for rec in overdue_data:
                print(rec)

        elif choice == "9":
            print("\n图书分类统计：")
            cat_stat = stat_book_category(db)
            for s in cat_stat:
                print(s)
            print("\n图书借阅畅销榜：")
            rank_data = stat_book_sales_rank(db)
            for r in rank_data:
                print(r)

        elif choice == "10":
            print("\n正在关闭数据库连接，准备退出程序...")
            client.close()
            print("✅ 数据库连接已关闭，程序结束！")
            break
        else:
            print("❌ 输入无效，请重新选择菜单序号！")

if __name__ == "__main__":
    main()
