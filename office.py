import msoffcrypto
import threading
import PyPDF4

path='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\下一步工作.docx'
newpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\11111.docx'

path1='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\网络攻防实践.xlsx'
newpath1='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\22222.xlsx'

path2='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\文档2.pdf'
newpath2='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\44444.pdf'

passpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\nore.txt'
def openof(path,newpath,passwords,no):
    print('start'+str(no))
    start=no*226800*9
    lll=50000*9
    passwd=open(passwords,'r')
    passwd.read(lll)
    passwd.read(start)
    f = msoffcrypto.OfficeFile(open(path, 'rb'))
    f1 = msoffcrypto.OfficeFile(open(path1, 'rb'))
    pdf = PyPDF4.PdfFileReader(open(path2, 'rb'))
    for i in range(176800):
        try:
            tmp=passwd.read(9)
            tmp=tmp[:8]
            f.load_key(password=tmp)
            f.decrypt(open(newpath,'wb'))
        except:
            print('0:'+str(no)+' '+str(i)+':'+tmp)
            pass
        else:
            print('password:'+tmp)
            pa = open('passwd1.txt', 'w')
            pa.write(tmp)

        try:
            f1.load_key(password=tmp)
            f1.decrypt(open(newpath1,'wb'))
        except:
            print('1:'+str(no)+' ' + str(i) + ':' + tmp)
            pass
        else:
            print('password:'+tmp)
            pa1 = open('passwd2.txt', 'w')
            pa1.write(tmp)

        try:
            pdf.decrypt(tmp)
            pdf.getDocumentInfo()
        except:
            print('2:'+str(no)+' ' + str(i) + ':' + tmp)
            pass
        else:
            print('password:' + tmp)
            print(pdf.getDocumentInfo())
            pa1 = open('passwd3.txt', 'w')
            pa1.write(tmp)

    print("over:"+str(no))

th0=threading.Thread(target=openof,args=(path,newpath,passpath,0)).start()
th1=threading.Thread(target=openof,args=(path,newpath,passpath,1)).start()
th2=threading.Thread(target=openof,args=(path,newpath,passpath,2)).start()
th3=threading.Thread(target=openof,args=(path,newpath,passpath,3)).start()
th4=threading.Thread(target=openof,args=(path,newpath,passpath,4)).start()
th5=threading.Thread(target=openof,args=(path,newpath,passpath,5)).start()
th6=threading.Thread(target=openof,args=(path,newpath,passpath,6)).start()
th7=threading.Thread(target=openof,args=(path,newpath,passpath,7)).start()