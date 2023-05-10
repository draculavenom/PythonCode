import os
import hashlib
import shutil

class ReadFiles:
    
    def __init__(self):
        self.path = ""
        self.fileList = []
        self.checkedFiles = {}
    
    def setPath(self, path):
        self.path = path
        print("path set to: " + self.path)
    
    def readfiles(self):
        self.fileList = os.listdir(self.path)
    
    def getFileList(self):
        print(self.fileList)
    
    def checkFileByFile(self):
        for fileName in self.fileList:
            if fileName == "duplicados" or "batch" in fileName:
                print("duplicados no")
            else:
                tempHash = self.hash_file(self.path + "\\" + fileName)
                if tempHash in self.checkedFiles.values():
                    shutil.move(self.path + "\\" + fileName, self.path + "\\duplicados\\" + fileName)
                    print("duplicado encontrado: " + fileName)
                self.checkedFiles[fileName] = tempHash
    
    def checkFiles(self):
        for fileName in self.fileList:
            if fileName == "duplicados" or "batch" in fileName:
                print("duplicados no")
            else:
                # print(os.path.getsize(self.path + "\\" + fileName))
                # print(os.path.getmtime(self.path + "\\" + fileName))
                tempHash = os.path.getctime(self.path + "\\" + fileName)
                # tempHash = self.hash_file(self.path + "\\" + fileName)
                print(tempHash)
                if tempHash in self.checkedFiles.values():
                    shutil.move(self.path + "\\" + fileName, self.path + "\\duplicados\\" + fileName)
                    print("duplicado encontrado: " + fileName)
                self.checkedFiles[fileName] = tempHash
    
    def hash_file(self, filename):
        """"This function returns the SHA-1 hash
        of the file passed into it"""
        
        # make a hash object
        h = hashlib.sha1()
        
        # open file for reading in binary mode
        with open(filename,'rb') as file:
        
            # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)
        
        # return the hex representation of digest
        return h.hexdigest()