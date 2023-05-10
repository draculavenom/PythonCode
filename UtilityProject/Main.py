from ReadFiles import ReadFiles

readFiles = ReadFiles()
readFiles.setPath("D:\\Fotos\\Fotos\\Photos from 2022")
#readFiles.setPath("D:\\Fotos\\Fotos\\Photos from 2021")
#readFiles.setPath("D:\\Juan\\images\\nature")
#readFiles.setPath("C:\\Users\\paqui\\eclipse-workspace")
readFiles.readfiles()
readFiles.getFileList()
#readFiles.checkFileByFile()
readFiles.checkFiles()