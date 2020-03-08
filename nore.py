import sys

sys.setrecursionlimit(100000000)
all="0123456789"
a=''
path="nore.txt"
f=open(path,'w')
def selec(lib,delib):
    word=''
    for each in lib:
        if each not in delib:
            word=word+each
    if len(lib)==2 or len(word)==0:
        return '\n'
    else:
        return word[0]

def run(can,cant,f,passwd):
    for i in range(len(can)):
        tmp=selec(can,cant)
        cant=cant+tmp
        nextps=passwd+tmp
        if len(can)==3:
            f.write(nextps)
            print("cin:"+nextps)
        else:
            for i in range(len(can)):
                if can[i]==tmp:
                    break
            ls=''
            if i+1<len(can):
                ls=ls+can[i+1:]
            if i>0:
                ls=ls+can[:i]
            run(ls,'',f,nextps)

run(all,a,f,'\n')
