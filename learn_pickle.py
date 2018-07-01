# 序列化案例
import pickle
class Person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show(self):
        print(self.name+"_"+str(self.age))
aa = Person("JGood", 2)
aa.show()
bb = Person("BB", 4)
bb.show()
with open('p.txt','wb') as f:
    pickle.dump(aa,f,0)
    pickle.dump(bb,f,0)
    #f.close() 使用with不必手动关闭文件

with  open('p.txt','rb') as f:
    aa = pickle.load(f)
    bb = pickle.load(f)

aa.show()
bb.show()
