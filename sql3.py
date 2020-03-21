import sys
import pymysql
import prettytable as pr
import os

os.system("cls")
link = pymysql.connect( #連結Mysql
host ="localhost",
user = "root",
passwd = "",
db = "python_ai_2018",
charset = "utf8",
port = 3306
)


while True:
    #主程式
    print("(0) 離開程式")
    print("(1) 顯示會員列表")
    print("(2) 新增會員資料")
    print("(3) 更新會員資料")
    print("(4) 刪除會員資料")
    print("(5) 新增會員的電話")
    print("(6) 刪除會員的電話")
    ans=input("指令 : ")


    c = link.cursor() # 取得指令操作變數

    if ans == "0":
        sys.exit()
    elif ans == "1":
        os.system("cls")
        c.execute("SELECT A.`id`,A.`name`,A.`birthday`,A.`address`,B.`tel` FROM member AS A LEFT JOIN tel AS B ON A.id=B.member_id")
        x=c.fetchall()

        r=pr.PrettyTable(["id","name","birthday","address","tel"],encoding="utf-8")
        for i in x:
            r.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(r)
    elif ans == "2":
        os.system("cls")
        c.execute("SELECT A.`id`,A.`name`,A.`birthday`,A.`address`,B.`tel` FROM member AS A LEFT JOIN tel AS B ON A.id=B.member_id")
        x=c.fetchall()

        r=pr.PrettyTable(["id","name","birthday","address","tel"],encoding="utf-8")
        for i in x:
            r.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(r)
        #清空印出表格
        i=input("請輸入會員姓名 : ")
        j=input("請輸入會員生日(請依照 1996-01-01 格式輸入): ")
        k=input("請輸入會員地址 : ")
        c.execute("insert into `member`(`name`,`birthday`,`address`) values(%s,%s,%s)",(i,j,k))
        link.commit()
    elif ans == "3":
        os.system("cls")
        c.execute("SELECT A.`id`,A.`name`,A.`birthday`,A.`address`,B.`tel` FROM member AS A LEFT JOIN tel AS B ON A.id=B.member_id")
        x=c.fetchall()

        r=pr.PrettyTable(["id","name","birthday","address","tel"],encoding="utf-8")
        for i in x:
            r.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(r)
        #清空印出表格
        q=input("請輸入要修改的會員編號 : ")
        i=input("請輸入要修改的會員姓名 : ")
        j=input("請輸入要修改的會員生日(請依照 1996-01-01 格式輸入): ")
        k=input("請輸入要修改的會員地址 : ")
        c.execute("update `member` set `name` = %s,`birthday` = %s ,`address` = %s where `id` = %s",(i,j,k,q))
        link.commit()
    elif ans == "4":
        os.system("cls")
        c.execute("SELECT A.`id`,A.`name`,A.`birthday`,A.`address`,B.`tel` FROM member AS A LEFT JOIN tel AS B ON A.id=B.member_id")
        x=c.fetchall()

        r=pr.PrettyTable(["id","name","birthday","address","tel"],encoding="utf-8")
        for i in x:
            r.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(r)
        #清空印出表格
        q=input("請輸入要刪除的資料編號 : ")
        c.execute("delete from `member` where `id`=%s",(q))
        link.commit()

    elif ans == "5":
        os.system("cls")
        c.execute("SELECT A.`id`,A.`name`,A.`birthday`,A.`address`,B.`tel` FROM member AS A LEFT JOIN tel AS B ON A.id=B.member_id")
        x=c.fetchall()

        r=pr.PrettyTable(["id","name","birthday","address","tel"],encoding="utf-8")
        for i in x:
            r.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(r)
        #清空印出表格
        q=input("請選擇要添加電話的會員編號 : ")
        i=input("請輸入要添加的電話號碼 : ")
        c.execute("insert into `tel`(`tel`,`member_id`) values(%s,%s)",(i,q))
        link.commit()

    elif ans == "6":
        os.system("cls")
        c.execute("SELECT A.`id`,A.`name`,A.`birthday`,A.`address`,B.`tel` FROM member AS A LEFT JOIN tel AS B ON A.id=B.member_id")
        x=c.fetchall()

        r=pr.PrettyTable(["id","name","birthday","address","tel"],encoding="utf-8")
        for i in x:
            r.add_row([i[0],i[1],i[2],i[3],i[4]])
        print(r)
        #清空印出表格
        q=input("請選擇要刪除電話的會員ID : ")
        c.execute("select `id`,`tel` from `tel` where `member_id`=%s order by `member_id` asc",(q) )
        x=c.fetchall()
        link.commit()
        r=pr.PrettyTable(["編號","電話"],encoding="utf-8")
        for i in x:
            r.add_row([i[0],i[1]])
        print(r)
        oo=input("請問要刪除的編號 : ")
        c.execute("delete `tel` from `tel` where `id`=%s",(oo))
        link.commit()




    link.close()
