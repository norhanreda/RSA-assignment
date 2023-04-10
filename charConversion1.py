def char_conversion_encoding(message):
    
    new_message=''
    length=len(message)
    x=length%5
    if(x):
        for i in range(0,5-x):
            message.append(36)
    sum=0
    for i in range(0,len(message),5):
        k=4
        sum=0
        for j in range(i,i+5):
            sum+=message[j]*(37**(k))
            k-=1

        formatted_sum = "{:0>{}}".format(sum, 8)
        
        new_message+=str(formatted_sum)

    return int(new_message)

def char_conversion_decoding(number):

    nearest_multiple_of_8 = (len(str(number)) + 7) & ~7

    number = "{:0>{}}".format(number, nearest_multiple_of_8)

    number=str(number)

    array_numbers=[]

    for i in range (len(number),1,-8):#len=8 [0,7][0:8]
        print(i)
        sub_number=int(number[i-8:i])
        temp_array=[]
        for i in range(0,5):
            
            temp_array.insert(0,int(sub_number%37))
            sub_number/=37
        array_numbers=temp_array+array_numbers

    return array_numbers

print(char_conversion_encoding([5, 5, 5, 5, 5,5, 5, 5, 5, 5,5, 5, 5, 5, 5]))
# print(char_conversion_decoding(char_conversion_encoding([5, 5, 5, 5, 5,3, 3, 3, 3, 3,1,1,1,1,1])))
# print(char_conversion_decoding(32822818))  

