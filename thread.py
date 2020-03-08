import threading
import zipfile
import numpy as np

zippath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice.zip'
newpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\111\\password2.txt'


def replas(wordpath,newpath):        #修改文件格式
    f=open(wordpath,'r')
    new=open(newpath,'w')
    word=f.read()
    word=word.replace('\n','    ')
    new.write(word)
    f.close()
    new.close()

#replas(wordpath,newpath)
def openzip(no,part):
    f=open(newpath,'r')
    zf = zipfile.ZipFile(zippath, "r")
    f.read(no*part*8)
    for i in range(62*62*62*8):
        try:
            tmp=f.read(5)
            tmp=tmp[:4].encode(encoding='UTF-8', errors='strict')
            zf.extractall(pwd=tmp)
        except:
            print(str(no)+':'+tmp.decode()+'  '+str(i))
            pass
        else:
            print('password:'+tmp.decode())
            pa=open('passwd.txt','w')
            pa.write(tmp)
            pa.close
            break


one=62*62*62*5
th0=threading.Thread(target=openzip,args=(0,one)).start()
th1=threading.Thread(target=openzip,args=(1,one)).start()
th2=threading.Thread(target=openzip,args=(2,one)).start()
th3=threading.Thread(target=openzip,args=(3,one)).start()
th4=threading.Thread(target=openzip,args=(4,one)).start()
th5=threading.Thread(target=openzip,args=(5,one)).start()
th6=threading.Thread(target=openzip,args=(6,one)).start()
th7=threading.Thread(target=openzip,args=(7,one)).start()