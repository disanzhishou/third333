import PyPDF4
path='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\文档1.pdf'
newpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\333\\python msoffice\\测试1.pdf'
passpath='C:\\Users\\MSI\\Desktop\\攻防\\YU\\111\\zip\\password\\passwd2.txt'

def pdfopen(path,passwords,start):
    pdf=PyPDF4.PdfFileReader(open(path,'rb'))
    f=open(passwords,'r')
    f.read(start)
    while True:
        try:
            tmp=f.read(12)
            tmp=tmp[:8]
            pdf.decrypt(tmp)
            pdf.getDocumentInfo()
        except:
            print(tmp)
        else:
            print('password:' + tmp)
            print(pdf.getDocumentInfo())
            break

pdfopen(path,passpath,0)