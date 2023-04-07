# space->32 0:9->48:57 a:z->97:122
def alphabet(message):
    new_message=[]
    for i in range(0,len(message)):
        x=ord(message[i])
        if(ord(message[i])>=48 and ord(message[i])<=57):
            x-=48
        elif(ord(message[i])>=97 and ord(message[i])<=122):
            x-=87
        else:
            x=36
        new_message.append(x)
    return(new_message)
# print(alphabet('hi s7'))


def dealphabet(message):
    new_message=[]
    for i in range(0,len(message)):
        x=message[i]
        if(message[i]>=0 and message[i]<=9):
            x+=48
        elif(message[i]>=10 and message[i]<=35):
            x+=87
        else:
            x=32
        new_message.append(chr(x))
    return(new_message)
# print(dealphabet([17, 18, 36, 28, 7])) 