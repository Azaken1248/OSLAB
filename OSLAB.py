import os


def chooseDir():
    print("Select Parent Directory")
    directory = "Templates"
    dirList = os.listdir(directory)
    
    counter = 1
    for dir in dirList:
        print(str(counter)+".",dir,end = "\t")
        counter += 1
    
    choice = int(input("\nEnter Your Choice: "))
    
    return list(os.listdir("Templates/"+dirList[choice-1])),dirList[choice-1]

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

def getFile(path, dir):
    try:
        with open("Templates/"+dir+"/"+path, "r") as inputFile:
            buff = inputFile.read()
        with open("Outputs/"+dir+"/"+path, "w+") as outputFile:
            outputFile.write(buff)
        print("File Generated! Thank You!")
    except FileNotFoundError as e:
        print("FileNotFound:", e)
    except Exception as e:
        print("An error occurred:", e)

    

while True:
    fileList,dir = chooseDir()
    choice,n = menu(fileList)
    
    if(choice == -1):
        print("EXITED")
        break
    elif choice not in list(range(1,n+1)):
        print("INVALID CHOICE!")
    else:
        getFile(fileList[choice-1],dir)
    
        
