def count():
    filename=input("Enter the file name")
    wordcount=0
    file=open(filename,"r")
    for i in file:
        splitwords=i.split()
        wordcount=wordcount+len(splitwords)
    print(wordcount)
count()        