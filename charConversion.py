def char_conversion(message):
    
    length=len(message)
    x=length%5
    if(x):
        for i in range(0,5-x):
            message.append(36)
    
    array_sum=[]
    sum=0
    for i in range(0,len(message),5):
        k=4
        sum=0
        for j in range(i,i+5):
            sum+=message[j]*(37**(k))
            k-=1
        array_sum.append(sum)

    print(array_sum)  
char_conversion([17, 18, 36, 28, 7,8, 5, 25, 16, 35])          
