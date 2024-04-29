import os

directory = "Templates"
fileList = os.listdir(directory)

def menu(files):
    counter = 1
    
    print("+++++++++++++++++++OSLABS+++++++++++++++++++")
    for file in files:
        print(counter,". ",file)
        counter += 1    
    print("+++++++++++++++++++OSLABS+++++++++++++++++++")
    try:
        choice = int(input("Enter A Choice(-1 To Exit): "))
    except:
        print("SEGMENTATION FAULT")
    
    return choice,len(files)

def getFile(path):
    
    try:
        buff = ""
        with open("Templates/"+path,"r") as inputFile:
            buff = inputFile.read()
        with open("Outputs/"+path, "w+") as outputFile:
            outputFile.write(buff)
    except:
        print("FileNotFound!!!")
    
    print("File Generated!Thank You!")
    

while True:
    choice,n = menu(fileList)
    
    if(choice == -1):
        print("EXITED")
        break
    elif choice not in list(range(1,n+1)):
        print("INVALID CHOICE!")
    else:
        getFile(fileList[choice-1])    
