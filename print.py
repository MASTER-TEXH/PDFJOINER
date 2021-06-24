import os,fnmatch
pdfs = os.listdir()
fle= list()
x=int(0)
for i in pdfs:
    if fnmatch.fnmatch(i,"*.pdf"):
        fle.append(i)
        print (i,type(i))
        x+=1
cmd = " ".join(fle)


os.system('cmd /k ".\gswin64.exe  -sDEVICE=pdfwrite  -dNOPAUSE -dBATCH -sOutputFile=Listo.pdf  -dLastPage=1 {}"'.format(cmd))
