import requests
import re

class Downloader :
    
    __url = ""
    __req = None
    __file_name = ""
    __file_size= 0

    def setUrl(self,url):
        self.__url = url
        self.getInfo()

    def printInfo(self):
        print(f"file name : {self.__file_name}\nfile size : {self.__file_size}\nfile url : {self.__url}")


    def getInfo(self):
        self.__req= requests.request(method="get",url=self.__url,stream=True)
        d_content = self.__req.headers['content-disposition']
        self.__file_name = re.findall("filename=\"(.+)\"", d_content)[0]
        self.__file_size = int(self.__req.headers.get("Content-Length"))

    def start(self):
        f = open(self.__file_name, 'wb')
        u = self.__req.raw
        print ("Downloading: %s Bytes: %s" % (self.__file_name, self.__file_size))
        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / self.__file_size)
                status = status + chr(8)*(len(status)+1)
                print (status,end='\n')
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / self.__file_size)
            status = status + chr(8)*(len(status)+1)
            print (status,end='\r')

        f.close()
    

def main():
    egybest_Downloader = Downloader()

    egybest_Downloader.setUrl("https://a4-rq3-s-5qq1.vidstream.to/dl/389bc1ce30000016bp9LnkFeljRnD1V%7Cz.CxRMS7nPvVkll8rtz4HLIA__.Y3pzZGNqOHlHVDhWQTFTQmwvVHBkbU5sRmJ2SDg3dkdIQnNVSGtUam5wSVdvNGRQTzIwMEtoUi91MUJyZkJHMGIydXp3Z1pHQ0x0dkJaTlNhdVg1NWhoaEx4YW05MG1lQ1lQRnJOczZEK2hZeVNocFd4U1JoM3lBSWFEL1VlTnE3RzRqU05Bd0hwakx5T3JYNXNyK1dTRS9lWGlmLy8xR2RoOVhwODFIbms4SnpsL0VSc2xjWkpwWU5WTTJZOFVUQVhMczBzMzc2NlhkQnJBMlBTSUhXYm1scXFPVmdNT2JBc2NrcHRhTTdGVnNWR3hkZlozRVJ6U2VHaC8yVno3N2FVY3FPc1p2aVRwM0tzWDlnOTJjVEFiNkwzbkM5cEp1bTB6S25qWUVEQkRyNHZveTlyN3lCL2ZneHFBelkzNm04NTJySzNsM0xLOTlPWHhVSGZLZXpGVlI2OTdodlZOV3RuTUVTVnl2bUJsOC9DYVVtTkNNbzNVa1NCUEF3aFJiYXIvMTBuRkhkaWdkY29mRFFLYThKbjNpbXd1dElwRk5xK3ZPNmJ5QWtaOD0_")
    egybest_Downloader.printInfo()

if __name__ == '__main__':
        main()
        