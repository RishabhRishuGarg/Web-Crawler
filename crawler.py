import urllib2
import re
import string
from os.path import basename
from urlparse import urlsplit
f=open('database.txt','w')
f.write("Image ID")
f.write("\t\t")
f.write("Shutter")
f.write("\t\t")
f.write("ISO")
f.write("\t\t")
f.write("Aperture")
f.write("\t\t")
f.write("Focal Length")
f.write("\n")
url = "http://www.dpchallenge.com/photo_gallery.php?GALLERY_ID=19&page=20"
str_ = urllib2.urlopen(url).read()
size=len(str_)
base="http://www.dpchallenge.com"
def store(image_id,shutter,ISO,aperture):
    f.write(str(image_id))
    f.write("\t\t")
    f.write(shutter)
    f.write("\t\t")
    f.write(ISO)
    f.write("\t\t")
    f.write(aperture)
    f.write("\t\t")
    f.write("Not available")
    f.write("\n")
def getdata(url,image_id):
    str_i = urllib2.urlopen(url).read()
    size_i=len(str_i)
    i=0
    shutter=""
    ISO=""
    aperture=""
    while(i!=size_i):
        if(str_i[i]=='A' and str_i[i+1]=='p' and str_i[i+2]=='e' and str_i[i+3]=='r' and str_i[i+4]=='t' and str_i[i+5]=='u' and str_i[i+6]=='r' and str_i[i+7]=='e'):
            i=i+13
            while(str_i[i].isspace()):
                i=i+1
            while(str_i[i]!='<'):
                aperture=aperture+str_i[i]
                i=i+1
        if(str_i[i]=='I' and str_i[i+1]=='S' and str_i[i+2]=='O'):
            i=i+8
            while(str_i[i].isalpha() or str_i[i].isspace()):
                i=i+1
            while(str_i[i]!='<'):
                ISO=ISO+str_i[i]
                i=i+1
        if(str_i[i]=='S' and str_i[i+1]=='h' and str_i[i+2]=='u' and str_i[i+3]=='t' and str_i[i+4]=='t' and str_i[i+5]=='e' and str_i[i+6]=='r'):
            i=i+12
            while(str_i[i].isalpha() or str_i[i].isspace()):
                i=i+1
            while(str_i[i]!='<'):
                shutter=shutter+str_i[i]
                i=i+1
        i=i+1
    print aperture,shutter,ISO
    store(image_id,shutter,ISO,aperture)
    return
def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
def get_id(imgUrl):
    j=len(imgUrl)-5
    image_id=0
    while(RepresentsInt(imgUrl[j])):
        j=j-1
    j=j+1
    while(j<len(imgUrl)and RepresentsInt(imgUrl[j])):
        image_id=image_id*10+int(imgUrl[j])
        j=j+1
    return image_id 
def collect(url):
    print url
    print "called"
    print "called"
    page_id=get_id(url)
    print page_id
    content = urllib2.urlopen(url).read()
    output1=open("website1.html",'wb')
    output1.write(content)
    print "called"
    content_size=len(content)
    i=0    
    while(i!=content_size):
        if(content[i]=='i'):
           if(content[i+1]=='m'):
               if(content[i+2]=='g'):
                    if(content[i+4]=='s'):
                       if(content[i+5]=='r'):
                           if(content[i+6]=='c'):
                                imgUrl=""
                                print "called img src"
                                i=i+9
                                width=0;
                                while(content[i]!='"'):
                                    imgUrl=imgUrl+content[i]
                                    i=i+1
                                image_id=get_id(imgUrl)
                                if(page_id==image_id):
                                    print image_id
                                    download(imgUrl,image_id)
                                    getdata(url,image_id)
                                    print imgUrl
                           
        i=i+1                            
def download(imgUrl,image_id):
        print imgUrl       
        print "download"
        try:
                x=urllib2.urlopen(imgUrl)
                print "readed"
                imgData = x.read()
                print "readed"
                filename=str(image_id)+".jpg"
                output = open(filename,'wb')
                print "filename"
                output.write(imgData)
                print "written"
                output.close()
        except:
                print "access denied"
                print imgUrl
        
        print "ho gaya mera"
print len(str_)
link_str=[]
i=0
while i!=size:
    if str_[i] == 'a':
        if str_[i+1] == ' ':
            if str_[i+2] == 'h':
                if str_[i+3] == 'r':
                    if str_[i+4] == 'e':
                        if str_[i+5] == 'f':
                            if str_[i+6] == '=':
                                j=i+8
                                if str_[j+1]=='i':
                                    while str_[j]!='"':
                                        link_str.append(str_[j])
                                        j=j+1
                                    link_str.append('\n')

    i=i+1                                
link_str.append('$')
#for k in link_str:
 #   print k,
size=len(link_str)
part="http://www.dpchallenge.com"
i=0;
while i!=size:
    if link_str[i] == '\n':
        print part
        collect(part)        
        part="http://www.dpchallenge.com"
    else:
        part=part+link_str[i]
    i=i+1
f.close()
