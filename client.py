import socket
import threading
from tkinter import *
import pickle
import rsa
import charConversion
import alphabet
import pandas as pd
name=input("enter your name : ")
key_size=input("enter the key size : ")
public, private = rsa.generate_keypair(int(key_size))
msg=pickle.dumps(public)
#print(public[0])
def set_ip():
    # ip = edit_text_ip.get()
    # port = edit_text_port.get()

    # Define Client and connect to server:
    global client
    client = socket.socket()
    client.connect((socket.gethostname(), 1234))

    # distryo input root
    input_root.destroy()
    # end of input root:
    input_root.quit()


def send():
    if str(edit_text.get()).strip() != "":
        #print(str(edit_text.get()))
        #print(sizeof(str(edit_text.get())))
        text=str(edit_text.get())
        message=alphabet.alphabet(text)
        message_arr=charConversion.char_conversion(message)
        #plain_text=int("".join(map(str,charConversion.char_conversion(message))))
        #plain_text=int(charConversion.char_conversion(message))
        #print(plain_text)
        plain_text=[]
        for i in range(0,len(message_arr)):

            ctt=rsa.encrypt(message_arr[i],pkey)
            #print(ctt)
            client.send(str(ctt).encode())
            plain_text.append(ctt)
        # scrollbar:
        client.send(('ack').encode())
        plain_text=int("".join(map(str,charConversion.char_conversion(plain_text))))
        # scrollbar:
        listbox.insert(END,text)
        edit_text.delete(0, END)
        arr_data=[]
        arr_data.append(str(public[0]))
        arr_data.append(str(plain_text))
        arr_data.append(str(ctt))
        arr_data.append(str(public[1]))
        arr_data.append(str(name))
        my_df = pd.DataFrame(arr_data)
        my_df.to_csv('alice.csv',header = False, index= False)

def recv():
    while True:
        dec=[]
        response_message =client.recv(1024).decode()
        while(response_message != 'ack'):
            decrypted_msg = rsa.decrypt(int(float(response_message)), private)
            dec.append(decrypted_msg)
            response_message =client.recv(1024).decode()
        #print(response_message)
        #decrypted_msg = rsa.decrypt(response_message, private)
        # scrollbar:
        #print(decrypted_msg)
        print(dec)
        decrypted_msg=charConversion.char_decoding(dec)
        decrypted_msg=alphabet.dealphabet(decrypted_msg)
        #print(decrypted_msg)
        listbox.insert(END, name1 +" : "+ str("".join(decrypted_msg)))
        edit_text.delete(0, END)


# Client GUI
# 1: Input Root GUI
input_root = Tk()
bgimage = PhotoImage(file ="wow.png")
Label(input_root,image=bgimage).place(relwidth=1,relheight=1)
# edit_text_ip = Entry()
# edit_text_port = Entry()
# ip_label = Label(input_root, text="Enter Server IP")
# port_label = Label(input_root, text="Enter Server Port")
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
#sending details
name1=client.recv(1024).decode()
client.send(str.encode(name))
rmsg=client.recv(1024)
pkey=pickle.loads(rmsg)
#print("public key of other is :",pkey[0])
client.send(msg)
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

button = Button(root, text="Send Message", command=send, bg='#4040bf', fg="white")
button.pack(fill=X, side=BOTTOM)
edit_text = Entry(root)
edit_text.pack(fill=X, side=BOTTOM)

root.title(name)
root.geometry("400x700")
root.resizable(width=True, height=True)

threading.Thread(target=recv).start()

root.mainloop()
