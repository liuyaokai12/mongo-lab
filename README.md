# MongoDB图书情报检索与统计平台实训
> 班级：24数科1班
> 学号：202414870112
> 姓名：刘曜恺

## 项目简介
本实训使用Python3 + PyMongo操作MongoDB数据库，搭建图书借阅管理系统，依次完成任务1~任务6：数据库与集合创建、数据导入、增删改查、聚合管道统计、索引建立与性能测试。

## 文件清单（一共13个）
1. 24数科1班202414870112刘曜恺.doc：实训报告文档
2. README.md：项目说明文档
3. book_manager.py：图书信息管理模块
4. books.txt：图书原始数据集
5. books_full.txt：完整图书数据集
6. borrow_logs.txt：借阅日志数据集
7. borrow_manager.py：图书借阅业务模块
8. category_stats.txt：分类统计结果文件
9. main.py：程序主入口，菜单交互界面
10. mongodb_connect.py：MongoDB数据库连接模块
11. reader_manager.py：读者信息管理模块
12. readers.txt：读者原始数据集
13. stat_manager.py：数据聚合统计模块

## 运行环境
1. 启动本地MongoDB服务，连接地址：`127.0.0.1:27017`
2. 电脑安装Python3环境；在PyCharm终端输入下面命令，安装依赖库
```bash
pip install pymongo

