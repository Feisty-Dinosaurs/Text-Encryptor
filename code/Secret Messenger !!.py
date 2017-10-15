# Project Title : Secret Messenger !! 

#importing required packages

import tkinter
from tkinter import *

from tkinter import messagebox

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import webbrowser

alphabet="abcdefghijklmnopqrstuvwxyz"
Alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


#function for sending message using gmail

def mail_sent():
    fromaddr = s_id.get()
    passwd = p_word.get()
    toaddr = r_id.get()
    temp1 = sub.get()
    temp2 = b.get("1.0",END)
    
    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = temp1
 
    body = temp2

    msg.attach(MIMEText(body, 'plain'))

    filename = "encrypted_file.txt"
    attachment = open('C:\\Users\\DELL\\Desktop\\encrypted_file.txt', 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
    msg.attach(part)
 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, passwd)
    text = msg.as_string()

    try:
        server.sendmail(fromaddr, toaddr, text)
        messagebox.showinfo("EMAIL SENT!","Your email has been sent!")
    except:
        messagebox.showinfo("ERROR!","Error in sending email")

    server.quit()


#Function for fetching email details from sender
    
def send_mail_window():
    child3 = tkinter.Tk()
    child3.title("Fill the details!")
    child3.minsize(width=600,height=600)
    child3.configure(background="SkyBlue1")

    global s_id
    s_id = tkinter.Entry(child3,width=67)
    s_id.place(x=150,y=70)
    label3 = tkinter.Label(child3,text="Email-id :")
    label3.place(x=20,y=70)

    global p_word
    p_word = tkinter.Entry(child3,show="*",width=67)
    p_word.place(x=150,y=100)
    label4 = tkinter.Label(child3,text="Password : ")
    label4.place(x=20,y=100)

    global r_id
    r_id = tkinter.Entry(child3,width=67)
    r_id.place(x=150,y=130)
    label5 = tkinter.Label(child3,text="Receiver's email-id :")
    label5.place(x=20,y=130)

    global sub
    sub = tkinter.Entry(child3,width=67)
    sub.place(x=150,y=160)
    label6 = tkinter.Label(child3,text="Subject : ")
    label6.place(x=20,y=160)

    global b
    b = tkinter.Text(child3,width=50,height=8,wrap=WORD)
    b.place(x=150,y=190)
    label7 = tkinter.Label(child3,text="Body : ")
    label7.place(x=20,y=190)
    
    scroll2 = tkinter.Scrollbar(child3,bd=4,orient=VERTICAL)
    scroll2.place(x=557,y=190)
    scroll2.config(command=b.yview)
    b.config(yscrollcommand=scroll2.set)

    send_button = tkinter.Button(child3,width=10,text="Send",bd=4,bg="LightSteelBlue3",command=mail_sent)
    send_button.place(x=150,y=370)

    cancel2 = tkinter.Button(child3,width=10,text="Cancel",bd=4,bg="LightSteelBlue3",command=child3.destroy)
    cancel2.place(x=310,y=370)

    
    
#Function for encrypting the message using a key
    
def encrypt_text():
    k = entry1.get()
    key = int(k)
    temp = msg1.get("1.0",END)
    message = temp

    new_message=''

    for character in message:
        if character in alphabet:
            position= alphabet.find(character)
            new_position= (position + key)%26
            new_character= alphabet[new_position]
            new_message= new_message + new_character
        elif character in Alphabet:
            position= Alphabet.find(character)
            new_position= (position + key)%26
            new_character= Alphabet[new_position]
            new_message= new_message + new_character
        else:
            new_message= new_message + character

    f = open('encrypted_file.txt','w')
    f.write(new_message)
    f.close()

    child2 = tkinter.Tk()
    child2.title("Encrypted text")
    child2.minsize(width=400,height=300)
    child2.configure(background="SkyBlue1")

    text5 = tkinter.Text(child2,width=39,height=2,bg="Light Green")
    text5.insert(INSERT,"Your message has been encrypted into a new text file.")
    text5.place(x=40,y=10)

    text6 = tkinter.Text(child2,width=39,height=2,bg="Light Green")
    text6.insert(INSERT,"Do you want to mail this text file?")
    text6.place(x=40,y=150)

    yes = tkinter.Button(child2,width=5,text="Yes",bd=4,bg="LightSteelBlue3",command=send_mail_window)
    yes.place(x=200,y=210)

    no = tkinter.Button(child2,width=5,text="No",bd=4,bg="LightSteelBlue3",command=child2.destroy)
    no.place(x=308,y=210)

        
#Function for fetchinh message and the encryption key from the sender
    
def encryption_screen():
    root.destroy()
    child1 = tkinter.Tk()
    child1.title("Encryption")
    child1.minsize(width=600,height=400)
    child1.configure(background="skyblue1")
    child1.resizable(0,0)

    text3 = tkinter.Text(child1,width=37,height=1,bg="Light Green")
    text3.insert(INSERT,"WELCOME !! TO THE ENCRYPTION WINDOW !")
    text3.place(x=150,y=10)

    global entry1
    entry1 = tkinter.Entry(child1,width=40)
    entry1.place(x=205,y=70)
    label1 = tkinter.Label(child1,text="Key :")
    label1.place(x=75,y=70)

    global msg1
    msg1 = tkinter.Text(child1,width=30,height=5,wrap=WORD)
    msg1.place(x=205,y=100)
    label2 = tkinter.Label(child1,text="Message : ")
    label2.place(x=75,y=100)
    scroll1 = tkinter.Scrollbar(child1,bd=4,orient=VERTICAL)
    scroll1.place(x=455,y=100)
    scroll1.config(command=msg1.yview)
    msg1.config(yscrollcommand=scroll1.set)
    
    en_button = tkinter.Button(child1,width=10,text="Encrypt",bd=4,bg="LightSteelBlue3",command=encrypt_text)
    en_button.place(x=205,y=220)

    cancel1 = tkinter.Button(child1,width=10,text="Cancel",bd=4,bg="LightSteelBlue3",command=child1.destroy)
    cancel1.place(x=365,y=220)

    text4 = tkinter.Text(child1,width=70,height=1,bg="Light Green")
    text4.insert(INSERT,'NOTE : Clicking "Encrypt" will encrypt message into a new text file.')
    text4.place(x=15,y=300)

#Function for displaying the message via a text file
    
def open_window():
    webbrowser.open("decrypted_file.txt")

#Function used for decrypting the message
    
def decrypt_text():
    l = dec_key.get()
    deckey = int(l)
    temp3 = path_of_file.get()
    de_filename = temp3

    rf = open(de_filename,"r")
    enc_message = rf.read()
    rf.close()

    old_message = ''

    for character in enc_message:
        if character in alphabet:
            position= alphabet.find(character)
            old_position= (position - deckey)%26
            old_character= alphabet[old_position]
            old_message= old_message + old_character
        elif character in Alphabet:
            position= Alphabet.find(character)
            old_position= (position - deckey)%26
            old_character= Alphabet[old_position]
            old_message= old_message + old_character
        else:
            old_message= old_message + character

    file_1 = open("decrypted_file.txt","w")
    file_1.write(old_message)
    file_1.close()

    child5 = tkinter.Tk()
    child5.title("Decrypted text")
    child5.minsize(width=400,height=300)
    child5.configure(background="SkyBlue1")

    text8 = tkinter.Text(child5,width=39,height=2,bg="Light Green")
    text8.insert(INSERT,"Your message has been decrypted into a new text file.")
    text8.place(x=40,y=10)

    text9 = tkinter.Text(child5,width=39,height=2,bg="Light Green")
    text9.insert(INSERT,"Do you want to open this text file?")
    text9.place(x=40,y=150)

    yes1 = tkinter.Button(child5,width=5,text="Open",bd=4,bg="LightSteelBlue3",command=open_window)
    yes1.place(x=200,y=210)

    no1 = tkinter.Button(child5,width=5,text="Cancel",bd=4,bg="LightSteelBlue3",command=child5.destroy)
    no1.place(x=308,y=210)
    
#Function for fetching decrypted text file and the key from reciever
    
def decryption_screen():
    root.destroy()
    child4 = tkinter.Tk()
    child4.title("Decryption")
    child4.minsize(width=600,height=400)
    child4.configure(background="SkyBlue1")

    text7 = tkinter.Text(child4,width=37,height=1,bg="Light Green")
    text7.insert(INSERT,"WELCOME !! TO THE DECRYPTION WINDOW !")
    text7.place(x=150,y=10)

    global path_of_file
    path_of_file = tkinter.Entry(child4,width=50)
    path_of_file.place(x=205,y=70)
    label8 = tkinter.Label(child4,text="Path of file :")
    label8.place(x=75,y=70)

    global dec_key
    dec_key = tkinter.Entry(child4,width=50)
    dec_key.place(x=205,y=100)
    label9 = tkinter.Label(child4,text="Key :")
    label9.place(x=75,y=100)

    dec_button = tkinter.Button(child4,width=10,text="Decrypt",bd=4,bg="LightSteelBlue3",command=decrypt_text)
    dec_button.place(x=205,y=220)

    cancel3 = tkinter.Button(child4,width=10,text="Cancel",bd=4,bg="LightSteelBlue3",command=child4.destroy)
    cancel3.place(x=421,y=220)

#Quiting verification popup window
    
def quit_window():
    var = messagebox.askyesno("Verify!","Do you really want to quit?")
    if var == True:
        root.destroy()

#Main window of the desktop application
        
root = tkinter.Tk()
frame = Frame(root)
root.title("Secret Messenger !!")
root.minsize(width=600, height= 400)
root.configure(background="Sky Blue")
root.resizable(0,0)

text1 = tkinter.Text(root,width=47,height=2,bg="Light Green")
text1.insert(INSERT,"   Which operation would you like to perform?")
text1.place(x=100,y=150)

text2 = tkinter.Text(root,width=10,height=1,bg="Light Green")
text2.insert(INSERT,"WELCOME !!")
text2.place(x=255,y=10)
    
close_quit = tkinter.Button(root,width=10,text="Quit!",bd=4,bg="LightSteelBlue3",command=quit_window)
close_quit.place(x=400,y=300)

encrypt = tkinter.Button(root,width=10,text="Send",bd=4,bg="LightSteelBlue3",command=encryption_screen)
encrypt.place(x=100,y=200)

decrypt = tkinter.Button(root,width=10,text="Receive",bd=4,bg="LightSteelBlue3",command=decryption_screen)
decrypt.place(x=400,y=200)



    

root.mainloop()
