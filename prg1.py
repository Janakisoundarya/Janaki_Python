import os.path
while True:
    source = raw_input("enter the source file name")
    target = raw_input("enter the target file name")
    if os.path.exists(source) == False:
        print "source file does not exists. Please enter a new file "
        continue
    elif os.path.exists(target) == True:
        print "target file already exists"
        text = raw_input("enter moveon if you want to continue with the same file or give another file")
        if text == "moveon":
            f = open(source,"r")
            f1 = open(target,"w")
            data = f.read()
            for i in data:
                f1.write(i)
            f1.close()
            f.close()
            break
        else:
            continue
