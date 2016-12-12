# -*- coding: utf-8 -*- 

class TestClass:

    def __init__(self, code, name):
        self.code = code
        self.name = name


classes = []
classes.append(TestClass(1, u'テスト１'))
classes.append(TestClass(2, u'テスト２'))

for cls in classes:
    print "===== Class ====="
    print 'code --> ' + str(cls.code)
    print 'name --> ' + cls.name
