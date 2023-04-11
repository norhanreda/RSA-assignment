import socket
import threading
from tkinter import *
import pickle
import rsa
import charConversion
import alphabet
import pandas as pd
import time
name=input("enter your name : ")
key_size=input("enter the key size : ")
public, private = rsa.generate_keypair(int(key_size))
msg=pickle.dumps(public)
#print(public[0])
def set_ip():
    # ip = edit_text_ip.get()
    # port = edit_text_port.get()
    
    # Define Server:
    server = socket.socket()
    server.bind((socket.gethostname(), 1234))
    server.listen()

    global conn
    conn, addr = server.accept()

    # distryo input root
    input_root.destroy()
    # end of input root
    input_root.quit()


def send():
    if str(edit_text.get()).strip() != "":
        #print(str(edit_text.get()))
        text=str(edit_text.get())
        message=alphabet.alphabet(text)
        message_arr=charConversion.char_conversion(message)
        plain_text=int("".join(map(str,charConversion.char_conversion(message))))
        #plain_text=int(charConversion.char_conversion(message))
        #print(plain_text)
        cipher_text=[]
        print("alphaped",message)
        print("conversion",message_arr)
        time_enc=[]
        for i in range(0,len(message_arr)):
            start = time.time()
            ctt=rsa.encrypt(message_arr[i],pkey)
            end = time.time()
            time_enc.append(end - start)
            cipher_text.append(ctt)
            # print("cipher",ctt)
            conn.send(str(ctt).encode())
            time.sleep(1)
        print("time for encryption",time_enc[0])   
        # scrollbar:
        conn.send(('ack').encode())
        time.sleep(1)
        cipher_text=int("".join(map(str,(cipher_text))))
        listbox.insert(END,  text)
        edit_text.delete(0, END)
        arr_data=[]
        arr_data.append(str(public[0]))
        arr_data.append(str(plain_text))
        arr_data.append(str(cipher_text))
        arr_data.append(str(public[1]))
        arr_data.append(str(name))
        my_df = pd.DataFrame(arr_data)
        my_df.to_csv('bob.csv',header = False, index= False)
        # f = open("bob.txt", "w")
        # f.write(arr_data)
        # f.close()


    # after sent message
    edit_text.delete(0, END)


def recv():
    while True:

        dec=[]
        time_dec=[]
        response_message =conn.recv(1024).decode()
        while(response_message != 'ack'):
            # print(response_message)
            start = time.time()
            decrypted_msg = rsa.decrypt(int((response_message)), private)
            end = time.time()
            time_dec.append(end - start)
            dec.append(decrypted_msg)
            response_message =conn.recv(1024).decode()
        #print(response_message)
        #decrypted_msg = rsa.decrypt(response_message, private)
        # scrollbar:
        #print(decrypted_msg)
        print(dec)
        print("time for decryption",time_dec[0])   
        decrypted_msg=charConversion.char_decoding(dec)
        decrypted_msg=alphabet.dealphabet(decrypted_msg)
        #print(decrypted_msg)
        # scrollbar:
        listbox.insert(END, name1 +" : "+ str("".join(decrypted_msg)))
        edit_text.delete(0, END)


# Server GUI:

# 1: Input Root GUI
input_root = Tk()
bgimage = PhotoImage(file ="wow.png")
Label(input_root,image=bgimage).place(relwidth=1,relheight=1)
# edit_text_ip = Entry()
# edit_text_port = Entry()
# ip_label = Label(input_root, text="Enter IP:")
# port_label = Label(input_root, text="Enter Port:")
connect_btn = Button(input_root, text="Connect To Server", command=set_ip, bg='#668cff', fg="white")

# show elements:
# ip_label.pack(fill=X, side=TOP)
# edit_text_ip.pack(fill=X, side=TOP)
# port_label.pack(fill=X, side=TOP)
# edit_text_port.pack(fill=X, side=TOP)
connect_btn.pack(fill=X, side=BOTTOM)

input_root.title(name)
input_root.geometry("400x700")
input_root.resizable(width=False, height=False)

input_root.mainloop()
#sending details-----------
conn.send(str.encode(name))
name1=conn.recv(1024).decode()
conn.send(msg)#sending public key
rmsg=conn.recv(1024)#recv pub key
pkey=pickle.loads(rmsg)
#print("public key of other is :",pkey[0])
# 2: Main Root GUI
root = Tk()
bgimage2 = PhotoImage(file ="wow.png")
Label(root,image=bgimage2).place(relwidth=1,relheight=1)
# Scrollbar:
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)
listbox.pack(fill=BOTH, side=TOP)
scrollbar.config(command=listbox.yview)

button = Button(root, text="Send Message", command=send, bg='#29a329', fg="white")
edit_text = Entry(root)

button.pack(fill=X, side=BOTTOM)
edit_text.pack(fill=X, side=BOTTOM)

root.title(name)
root.geometry("400x700")
root.resizable(width=True, height=True)

threading.Thread(target=recv).start()

root.mainloop()
