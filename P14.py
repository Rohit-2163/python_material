import time
try: 
    file = open("file12.txt","r")
    file2 = open("file2.txt","w")
    data = file.readlines()
    # print(data)
    print("sucessfully readed file1 ...")
    time.sleep(1)
    print("copying alternative lines initiated..")

    for i in range(len(data)):
        if i%2==0 : 
            file2.write(data[i])
    time.sleep(2)
    print("odd number lines are copied to file2 sucessfully....")

    print("\n---------------------------------")
    print("printing contents in file2 ...")
    
    file.close()
    file2.close()
    file2=open("file2.txt","r")
    data=file2.readlines()
    for line in data:
        print(line)
    file2.close()
    
except FileNotFoundError:
    print("Exception handled..")
    print("Given source file and destination file may not avialble..")
except:
    print("Something went wrong..\nprogram closed..")
