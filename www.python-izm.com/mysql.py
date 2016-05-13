# -*- coding: utf-8 -*- 

import MySQLdb

if __name__ == "__main__":

    connector = MySQLdb.connect(host="localhost", db="kose_development", user="root", passwd="", charset="utf8")
    cursor = connector.cursor()
    cursor.execute("select * from user_infos order by id")
    
    result = cursor.fetchall()

    for row in result:
        print "===== Hit! ====="
        print "id -- " + str(row[0])
        print "name -- " + str(row[1])
        
    cursor.close()
    connector.close()

# python mysql.py
    
# id -- 1
# name -- wenbo
# ===== Hit! =====
# id -- 2
# name -- asdf
# ===== Hit! =====
# id -- 3
# name -- asdf
# ===== Hit! =====
# id -- 4
# name -- asdf
# ===== Hit! =====
# id -- 5
# name -- wenbo
# ===== Hit! =====
# id -- 6
# name -- wenbo
# ===== Hit! =====
# id -- 7
# name -- wenbo
# ===== Hit! =====
# id -- 8
# name -- wenbo
# ===== Hit! =====
# id -- 9
# name -- asdfasdf
# ===== Hit! =====
# id -- 10
# name -- asdfasdf
# ===== Hit! =====
# id -- 11
# name -- asdfasdf
# ===== Hit! =====
# id -- 12
# name -- asdfasdf
# ===== Hit! =====
# id -- 13
# name -- asdfasdf
# ===== Hit! =====
# id -- 14
# name -- asdf
# ===== Hit! =====
# id -- 15
# name -- asdf
# 4m➜  www.python-izm.com git:(master) ✗ 
