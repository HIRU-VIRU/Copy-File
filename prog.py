with open("file1.txt","r") as f1:
    with open("copy.txt","w") as f2:
        line=f1.read()
        f2.write(line)