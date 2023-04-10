
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
    return  array_sum
    
# char_conversion([17, 18, 36, 28, 7,8, 5, 25, 16, 35])          
#print(char_conversion([17, 14, 21, 21, 24, 36, 17, 24, 32, 36, 10, 27, 14, 36, 34, 24, 30]) )
def char_decoding(message):
     decode=[]
     for i in range(0,len(message)):
        for j in range(4,-1,-1):
            # print(j)
            x=(message[i]//(37**(j)))%37
            decode.append(x)
     return decode

#print(char_decoding([32822818, 15281405]))
#print(char_decoding(3282281815281405))

#print(char_decoding([32822818, 15281405]))
#print(char_decoding(char_conversion([5,5, 5, 5, 5,5, 5]) ))
#print(char_decoding(char_conversion([5,5, 5, 5, 5,5, 5])))