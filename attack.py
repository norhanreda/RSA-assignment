import rsa
import pandas as pd
import numpy as np
# def attak(n,c,M,p1,p2):
def attack(C,M, n, e,name):
    d=0
    q=0
    p=0
    for p in range(2, int((n**0.5)+1)): # since n is composite then one of its factors is <=sqrt(n)
        if n % p == 0:
            q = n//p
            e = e
            p = p
            break
    phi=(p-1)*(q-1)    
    e_inv=rsa.mod_inverse(e,phi)
    d = e_inv
    if(M==rsa.decrypt(C,(d,n))):
       # if(person==True):
          print(name,"is attacked hahahahahahahahahah and his private key is:",d)
        # else:
        #   print("second person attacked hahahahahahahahahah")   
    return d
person1 = np.asarray(pd.read_csv('bob.csv',header = None))
person2 =  np.asarray(pd.read_csv('alice.csv',header = None))
# print(person1)
# print(person2)
# print(attack(14,5,33,7 ,True))
print(attack(int(person1[2]),int(person1[1]),int(person2[3]),int(person2[0]), str(person2[4])))
print(attack(int(person2[2]),int(person2[1]),int(person1[3]),int(person1[0]),str(person1[4])))