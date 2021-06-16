import requests
import re
# input("Enter url : ")

# if(len(url)<0):
#     url  = 

url = "http://download.thinkbroadband.com/10MB.zip"

# هنا بتطلب الملف من الموقع
requ= requests.request(method="get",url=url,stream=True)
# دا كلام بتاع header متشتغل بيهو اسي كلام شبكات وكدا
d = requ.headers['content-disposition']
#---------------------------------------------------
#هنا شلت الاسم بتاع الملف من ال header
file_name = re.findall("filename=\"(.+)\"", d)[0]
#هنا سويت الملف في الكمبيوتر
f = open(file_name, 'wb')
#هنا شلت حجم الملف من ال header
length = int(requ.headers.get("Content-Length"))
#الحاجه دي م مهمه لكن دي عشان اقدر اشيل من الملف حاجه حاجه م اشيلو كلو 
u = requ.raw
#------------------------------------------
file_size = length
print ("Downloading: %s Bytes: %s" % (file_name, file_size))
#هنا الفهم بتاع اشيل من الموقع وانزل في الملف حاجه حاجه 
#واظهر لي النسبه بتاعت التحميل
#----------------------------------------------------------
file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print (status,end='\n')
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print (status,end='\r')
#------------------------------------------------
#واخيرا هنا بقفل الملف 
f.close()