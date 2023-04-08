import rsa
# def attak(n,c,M,p1,p2):
def attack(C,M, n, e):
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
        print("attacked hahahahahahahahahah")
    return d
print(attack(14,5, 33, 7))