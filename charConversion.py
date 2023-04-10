# def char_conversion(message):
#     new_message=''
#     length=len(message)
#     x=length%5
#     if(x):
#         for i in range(0,5-x):
#             message.append(0)
    
#     array_sum=[]
#     sum=0
#     for i in range(0,len(message),5):
#         k=4
#         sum=0
#         for j in range(i,i+5):
#             sum+=message[j]*(37**(k))
#             k-=1
#         formatted_sum = "{:0>{}}".format(sum, 8)
        
#         new_message+=str(formatted_sum)            
#         array_sum.append(int(formatted_sum))
#     #print(array_sum) 
    
#     return  int(new_message)
    
# # char_conversion([17, 18, 36, 28, 7,8, 5, 25, 16, 35])   
# #print(char_conversion([5,5, 5, 5, 5,5, 5]) )         

# def char_decoding(number):
#     #  nearest_multiple_of_8 = (len(str(message)) + 7) & ~7

#     #  number = "{:0>{}}".format(message, nearest_multiple_of_8)

#     #  message=str(number)

#     #  message_arr=[]
#     #  #message=str(message)
#     # #  for k in range(0,len(message),8):
#     # #    x=int(message[k:k+8])
#     # #    #print(x)
#     # #    message_arr.append(x)
#     # #  #print(message_arr)  
#     #  array_numbers=[]
#     # #  decode=[]
#     #  for i in range(len(message),1,-8):
#     #     sub_number=int(message[i-8:i])
#     #     temp_array=[]
#     #     for j in range(0,5):
#     #         # print(j)
#     #         temp_array.insert(0,int(sub_number%37))
#     #         sub_number/=37
#     #         #x=(message_arr[i]//(37**(j)))%37
#     #         #decode.append(x)
#     #     array_numbers=temp_array+array_numbers    
#     #  return  array_numbers
#     nearest_multiple_of_8 = (len(str(number)) + 7) & ~7

#     number = "{:0>{}}".format(number, nearest_multiple_of_8)

#     number=str(number)

#     array_numbers=[]

#     for i in range (len(number),1,-8):#len=8 [0,7][0:8]
#         print(i)
#         sub_number=int(number[i-8:i])
#         temp_array=[]
#         for i in range(0,5):
            
#             temp_array.insert(0,int(sub_number%37))
#             sub_number/=37
#         array_numbers=temp_array+array_numbers

#     return array_numbers
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
    #print(array_sum)      
    return  array_sum
    
# char_conversion([17, 18, 36, 28, 7,8, 5, 25, 16, 35])          
print(char_conversion([17, 14, 21, 21, 24, 36, 17, 24, 32, 36, 10, 27, 14, 36, 34, 24, 30]) )
def char_decoding(message):
    #  message_arr=[]
    #  message=str(message)
    #  for k in range(0,len(message),8):
    #    x=int(message[k:k+8])
    #    #print(x)
    #    message_arr.append(x)
     #print(message_arr)  
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