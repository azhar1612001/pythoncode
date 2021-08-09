f=open('file.txt')
lines=f.readlines()
racialslurs=[]
sen=1
for line in lines:
    words=line.split()
    count=0
    for word in words:
        if word in racialslurs:
            count+=1
    profanity=(count/len(words))*100
    print("profanity of sentence number {} is {}".format(sen,profanity))
    sen+=1