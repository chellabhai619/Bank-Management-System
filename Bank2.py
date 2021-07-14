import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import mysql.connector as mysql
from tkinter import messagebox
from time import gmtime, strftime
from pickle import *


def is_number(s):
    try:
        float(s)
        return 1
    except ValueError:
        return 0


def check_acc_nmb(num):
    try:
        fpin = open(num + ".txt", 'r')
    except FileNotFoundError:
        messagebox.showinfo("Error", "Invalid Credentials!\nTry Again!")
        return 0
    fpin.close()
    return


def home_return(master):
    master.destroy()
    Main_Menu()


'''def write(master, name,  aadhar, addr, gen, dob, pin, oc):
    aa = str(aadhar)
    pi = str(pin)

    if not (len(aa) == 12 and len(pi) == 4):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    if ((is_number(name)) or (is_number(pin) == 0) or name == "" or gen == "" or addr == ""):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1 = open("Accnt_Record.txt", 'r')
    accnt_no = int(f1.readline())
    accnt_no += 1
    f1.close()

    f1 = open("Accnt_Record.txt", 'w')
    f1.write(str(accnt_no))
    f1.close()

    ad = "A" + str(accnt_no)
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("create table "+ad+" (amount VARCHAR(100), balance VARCHAR(100), fromq VARCHAR(100), date VARCHAR(100), time VARCHAR(100),upi VARCHAR(100))")
    cursor.execute("commit")
    print("Executed")
    con.close()
    x = strftime("%d/%m/%Y")
    y = strftime("%H-%M-%S")

    upi = str(accnt_no) + "@UNION"
    ab = "CREATED"
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    oc= str(oc)
    cursor.execute("insert into account values('" + str(accnt_no) + "','" + str(name) + "','" + str(aadhar) + "','" + str(addr) + "','" + str(gen) + "','" + str(dob) + "','" + str(pin) + "','" + str(oc) + "','" + str(upi) + "')")
    cursor.execute("commit")
    print("Executed")
    con.close()

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    # cursor.execute("insert into A%d values('" + str(oc) + "','" + str(oc) + "','" + str(ab) + "','" + str(x) + "','" + str(y) + "')"%(accnt_no))
    cursor.execute("insert into "+ad+" values('"+ str(oc) +"','"+ str(oc) +"','"+ str(ab) +"','"+ str(x) +"','"+ str(y) +"','"+ str(ab)+"')")
    cursor.execute("commit")
    print("Executed")
    con.close()


    frec = open(str(accnt_no) + "-rec.txt", 'w')
    frec.write("Date                             Credit      Debit     Balance\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + oc + "              " + oc + "\n")
    frec.close()
    messagebox.showinfo("Details", "Your Account Number is:" + str(accnt_no))
    master.destroy()
    return'''


def write2(master, fname, lname, aadhar, addr, gen, dob, pin):  # zero balance
    aa = str(aadhar)
    pi = str(pin)
    name = str(fname + ' ' + lname)

    if not (len(aa) == 12 and len(pi) == 4):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return
    if ((is_number(name)) or (is_number(pin) == 0) or name == "" or gen == "" or addr == ""):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    f1 = open("Accnt_Record.txt", 'r')
    accnt_no = int(f1.readline())
    accnt_no += 1
    f1.close()

    f1 = open("Accnt_Record.txt", 'w')
    f1.write(str(accnt_no))
    f1.close()

    ad = "A" + str(accnt_no)
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    oc = '0'
    cursor.execute(
        "create table " + ad + " (amount VARCHAR(100), balance VARCHAR(100), fromq VARCHAR(100), date VARCHAR(100), time VARCHAR(100),upi VARCHAR(100))")
    cursor.execute("commit")
    print("Executed")
    con.close()
    x = strftime("%d/%m/%Y")
    y = strftime("%H-%M-%S")

    upi = str(accnt_no) + "@UNION"
    ab = "CREATED"
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute(
        "insert into account values('" + str(accnt_no) + "','" + str(name) + "','" + str(aadhar) + "','" + str(
            addr) + "','" + str(gen) + "','" + str(dob) + "','" + str(pin) + "','" + str(oc) + "','" + str(upi) + "')")
    cursor.execute("commit")
    con.close()

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    # cursor.execute("insert into A%d values('" + str(oc) + "','" + str(oc) + "','" + str(ab) + "','" + str(x) + "','" + str(y) + "')"%(accnt_no))
    cursor.execute(
        "insert into " + ad + " values('" + str(oc) + "','" + str(oc) + "','" + str(ab) + "','" + str(x) + "','" + str(
            y) + "','" + str(ab) + "')")
    cursor.execute("commit")
    print("Executed")
    con.close()

    frec = open(str(accnt_no) + "-rec.txt", 'w')
    frec.write("Date                             Credit      Debit     Balance\n")
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + oc + "                  " + oc + "\n")
    frec.close()
    messagebox.showinfo("Details", "Your Account Number is:" + str(accnt_no))
    master.destroy()
    return


def crdt_write(master, amt, accnt, name):
    if (is_number(amt) == 0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select Balance from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()

    for row in rows:
        bal = row[0]

    amti = int(amt)
    cb = bal + amti
    cb = str(cb)
    cursor.execute("update account set Balance='" + cb + "' where AccountNo='" + accnt + "'")
    cursor.execute("commit")
    con.close()

    frec = open(str(accnt) + "-rec.txt", 'a+')
    frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime())) + "     " + str(amti) + "                  " + str(
        cb) + "\n")
    frec.close()

    x = strftime("%d/%m/%Y")
    y = strftime("%H-%M-%S")
    ad = "A" + str(accnt)
    upi = str(accnt) + "@UNION"
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("insert into " + ad + " values('" + str(amt) + "','" + str(cb) + "','" + str(upi) + "','" + str(
        x) + "','" + str(y) + "')")
    cursor.execute("commit")
    print("Executed")
    con.close()

    messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
    master.destroy()
    return


def change(upi, amti, bal22, acc):
    ad2 = "A" + str(upi)
    c = "CREDIT"
    x = strftime("%d/%m/%Y")
    y = strftime("%H-%M-%S")

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute(
        "insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\')".format(ad2, str(amti), str(bal22),
                                                                                         str(c), str(x), str(y),
                                                                                         str(acc)))
    cursor.execute("commit")
    print("Executed")
    con.close()


def debit_write(master, amt, accnt, upi, name):
    c = "DEBIT"
    if (is_number(amt) == 0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        return

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select Balance from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()

    for row in rows:
        bal = row[0]

    if (int(amt) > bal):
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        amti = int(amt)
        cb = bal - amti
        cb = str(cb)
        cursor.execute("update account set Balance='" + cb + "' where AccountNo='" + accnt + "'")
        cursor.execute("commit")
        con.close()
        frec = open(str(accnt) + "-rec.txt", 'a+')
        frec.write(str(strftime("[%Y-%m-%d] [%H:%M:%S]  ", gmtime()) + "                  " + str(amti) + "     " + str(
            cb) + "\n"))
        frec.close()

        x = strftime("%d/%m/%Y")
        y = strftime("%H-%M-%S")
        ad = "A" + str(accnt)
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        '''cursor.execute(
            "insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\')".format(ad, str(amt), str(cb),
                                                                                             str(c), str(x), str(y),
                                                                                             str(upi)))'''
        cursor.execute("insert into "+ad+" values('"+str(amt)+"','"+str(cb)+"','"+str(c)+"','"+str(x)+"','"+str(y)+"','"+str(upi)+"')")
        cursor.execute("commit")
        print("Executed")
        con.close()

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
            cursor = con.cursor()

            cursor.execute("select Balance from account where Accountno='" + upi + "'")
            rows = cursor.fetchall()

            for row in rows:
                bal2 = row[0]
            bal22 = bal2 + amti
            cursor.execute("update account set Balance='" + str(bal22) + "' where AccountNo='" + str(upi) + "'")
            cursor.execute("commit")
            con.close()
            change(upi, amti, bal22, accnt)
        except:
            pass

        try:
            con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
            cursor = con.cursor()
            cursor.execute("update account set Balance='" + cb + "' where UPI='" + upi + "'")
            cursor.execute("select Accountno from account where UPI='" + upi + "'")
            rows = cursor.fetchall()
            for row in rows:
                acc = row[0]
            cursor.execute("commit")
            print("Executed")
            cursor.close()
            change(acc, amt, accnt)

        except:
            pass

        messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
        master.destroy()
        return


def Cr_Amt(accnt, name):
    creditwn = tk.Tk()
    creditwn.geometry("600x300")
    creditwn.title("Credit Amount")
    creditwn.configure(bg="orange")
    fr1 = tk.Frame(creditwn, bg="blue")
    l_title = tk.Message(creditwn, text="UNITED BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    l = tk.Label(creditwn, bg='orange', text="User's UPI: ")
    l.place(x=10, y=100)
    lp = tk.Label(creditwn, bg='orange', text=name + "@UNION" + accnt)
    lp.place(x=150, y=100)
    l1 = tk.Label(creditwn, bg='orange', text="Enter Amount credited: ")
    e1 = tk.Entry(creditwn)
    l1.place(x=10, y=130)
    e1.place(x=150, y=130)
    b = tk.Button(creditwn, text="Credit", relief="raised", command=lambda: crdt_write(creditwn, e1.get(), accnt, name))
    b.place(x=280, y=170)
    creditwn.bind("<Return>", lambda x: crdt_write(creditwn, e1.get(), accnt, name))


def De_Amt(accnt, name):
    debitwn = tk.Tk()
    debitwn.geometry("600x300")
    debitwn.title("Debit Amount")
    debitwn.configure(bg="orange")
    fr1 = tk.Frame(debitwn, bg="blue")
    l_title = tk.Message(debitwn, text="UNITED BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    l = tk.Label(debitwn, bg='orange', text="Enter AccountNo or UPI:")
    e = tk.Entry(debitwn)
    l1 = tk.Label(debitwn, bg='orange', text="Enter Amount to be debited: ")
    e1 = tk.Entry(debitwn)
    l.place(x=10, y=100)
    e.place(x=170, y=100)
    l1.place(x=10, y=130)
    e1.place(x=170, y=130)
    b = tk.Button(debitwn, text="Debit", relief="raised",
                  command=lambda: debit_write(debitwn, e1.get(), accnt, e.get(), name))
    b.place(x=280, y=170)
    debitwn.bind("<Return>", lambda x: debit_write(debitwn, e1.get(), accnt, name))


def disp_bal(accnt):
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select Balance from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()

    for row in rows:
        bal = row[0]
    messagebox.showinfo("Balance", bal)
    con.close()


def disp_tr_hist(accnt):
    disp_wn = tk.Tk()
    disp_wn.geometry("900x600")
    disp_wn.title("Transaction History")
    disp_wn.configure(bg="orange")
    fr1 = tk.Frame(disp_wn, bg="blue")
    l_title = tk.Message(disp_wn, text="UNITED BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    fr1 = tk.Frame(disp_wn)
    fr1.pack(side="top")

    boo = "A" + str(accnt)
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    y = 140

    tk.Label(disp_wn,
             text="%-30s%-10s%-40s%-30s%-20s%-40s" % ('Date', 'Time', 'Credit/Debit', 'Amount', 'Balance', 'To/From'),
             bg='orange', fg='black').place(x=50, y=100)
    tk.Label(disp_wn,
             text="-------------------------------------------------------------------------------------------------------------------------------",
             bg='orange', fg='black').place(x=50, y=120)
    getTrans = "select * from " + boo

    cursor.execute(getTrans)
    row = cursor.fetchall()
    for i in row:
        tk.Label(disp_wn, text="%-20s%-15s%-40s%-30s%-20s%-40s" % (i[3], i[4], i[2], i[0], i[1], i[5]), bg='orange',
                 fg='black').place(x=50, y=y)
        y += 20
    '''except:
        messagebox.showinfo("Failed to fetch files from database")'''

    '''l1=tk.Message(disp_wn,text="Your Transaction History:",padx=100,pady=20,width=1000,bg="blue",fg="orange",relief="raised")
    l1.pack(side="top")
    fr2=tk.Frame(disp_wn)
    fr2.pack(side="top")
    frec=open(accnt+"-rec.txt",'r')
    for line in frec:
        l=tk.Message(disp_wn,anchor="w",text=line,relief="raised",width=2000)
        l.pack(side="top")
    b=tk.Button(disp_wn,text="Quit",relief="raised",command=disp_wn.destroy)
    b.pack(side="top")
    frec.close()'''


def logged_in_menu(accnt, name):
    rootwn = tk.Tk()
    rootwn.geometry("1600x500")
    rootwn.title("UNITED BANK-" + name)
    rootwn.configure(background='orange')
    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")
    l_title = tk.Message(rootwn, text="UNITED BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    label = tk.Label(text="Logged in as: " + name, relief="raised", bg="black", fg="white", anchor="center",
                     justify="center")
    label.pack(side="top")

    # b2=tk.Button(text='Credit Amount',bg='black',fg='white',font=("Courier","15","bold"),width=20,height=2,command=lambda: Cr_Amt(accnt,name))
    b3 = tk.Button(text='Send Amount', bg='black', fg='white', font=("Courier", "15", "bold"), width=20, height=2,
                   command=lambda: De_Amt(accnt, name))
    b4 = tk.Button(text='Display Balance', bg='black', fg='white', font=("Courier", "15", "bold"), width=20, height=2,
                   command=lambda: disp_bal(accnt))
    b5 = tk.Button(text='Transaction History', bg='black', fg='white', font=("Courier", "15", "bold"), width=20,
                   height=2, command=lambda: disp_tr_hist(accnt))
    b6 = tk.Button(text='Log Out', bg='red', fg='white', font=("Courier", "10", "bold"), width=20, height=2,
                   command=lambda: logout(rootwn))

    # b2.place(x=100,y=175)
    b3.place(x=650, y=170)
    b4.place(x=100, y=260)
    b5.place(x=1200, y=260)
    b6.place(x=670, y=400)


def logout(master):
    messagebox.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()


def check_log_in(master, name, acc_num, pin):
    if (is_number(name)) or (is_number(pin) == 0):
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        master.destroy()
        Main_Menu()

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select Pin from account where Accountno='" + acc_num + "'")
    rows = cursor.fetchall()

    for row in rows:
        gpin = row[0]
    try:

        if gpin == pin:
            master.destroy()
            logged_in_menu(acc_num, name)
            print("Executed")
            con.close()

    except:
        master.destroy()
        messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        Main_Menu()
        return
    con.close()


def log_in(master):
    master.destroy()
    loginwn = tk.Tk()
    loginwn.geometry("600x300")
    loginwn.title("Log in")
    loginwn.configure(bg="orange")
    fr1 = tk.Frame(loginwn, bg="blue")
    l_title = tk.Message(loginwn, text="UNITED BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    l1 = tk.Label(loginwn, text="Enter Name:", bg='orange')
    l1.place(x=10, y=100)
    e1 = tk.Entry(loginwn)
    e1.place(x=150, y=100)
    l2 = tk.Label(loginwn, text="Enter account number:", bg='orange')
    l2.place(x=10, y=130)
    e2 = tk.Entry(loginwn)
    e2.place(x=150, y=130)
    l3 = tk.Label(loginwn, text="Enter your PIN:", bg='orange')
    l3.place(x=10, y=160)
    e3 = tk.Entry(loginwn, show="*")
    e3.place(x=150, y=160)
    b = tk.Button(loginwn, text="Submit",
                  command=lambda: check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))
    b.place(x=120, y=200)
    b1 = tk.Button(text="HOME", relief="raised", bg="black", fg="white", command=lambda: home_return(loginwn))
    b1.place(x=420, y=200)
    loginwn.bind("<Return>", lambda x: check_log_in(loginwn, e1.get().strip(), e2.get().strip(), e3.get().strip()))


def Create():
    crwn = tk.Tk()
    crwn.geometry("800x350")
    crwn.title("Create Account")
    crwn.configure(bg="orange")
    fr1 = tk.Frame(crwn, bg="blue")
    option = ["Male", "Female"]
    l_title = tk.Message(crwn, text="UNITED BANK", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")

    l1 = tk.Label(crwn, text="Enter First Name:", bg='orange')
    l1.place(x=10, y=100)
    e1 = tk.Entry(crwn, width="40")
    e1.place(x=150, y=100)

    l11 = tk.Label(crwn, text="Enter Last Name:", bg='orange')
    l11.place(x=10, y=130)
    e11 = tk.Entry(crwn, width="40")
    e11.place(x=150, y=130)

    l6 = tk.Label(crwn, text="Enter Aadhar No.:", bg='orange')
    e6 = tk.Entry(crwn, width="40")
    l6.place(x=10, y=160)
    e6.place(x=150, y=160)

    l2 = tk.Label(crwn, text="Enter Address:", bg='orange')
    l2.place(x=10, y=190)
    e2 = tk.Entry(crwn, width="40")
    e2.place(x=150, y=190)

    l3 = tk.Label(crwn, text="Gender:", bg='orange')
    l3.place(x=10, y=220)
    combo = tk.ttk.Combobox(crwn, value=option, width="37")
    combo.set("----Select Gender----")
    combo.place(x=150, y=220)

    '''gen = tk.StringVar()
    gen.set("Select Gender")
    list=tk.OptionMenu(crwn, gen, "Male", "Female", "Transgender")
    list.place(x=150, y=160)'''
    '''tk.Radiobutton(crwn, text="Male", value="M", bg="orange", variable=i).place(x=150, y=160)
    tk.Radiobutton(crwn, text="Female", value="F", bg="orange", variable=i).place(x=150, y=190)
    tk.Radiobutton(crwn, text="Transgender", value="T", bg="orange", variable=i).place(x=150, y=220)'''

    l4 = tk.Label(crwn, text="Date of Birth:", bg='orange')
    l4.place(x=10, y=250)
    ent = DateEntry(crwn, width=15, bg='blue', fg='red', borderwidth=3, date_pattern='dd/mm/yy')
    ent.place(x=150, y=250)

    l5 = tk.Label(crwn, text="Enter desired 4-digit PIN:", bg='orange')
    e5 = tk.Entry(crwn, show="*", width="40")
    l5.place(x=10, y=280)
    e5.place(x=150, y=280)
    '''
    l4 = tk.Label(crwn, text="Phone No.:", bg='orange')
    l4.place(x=10, y=160)
    e4 = tk.Entry(crwn)
    e4.place(x=150, y=160)

    l5 = tk.Label(crwn, text="Address:", bg='orange')
    l5.place(x=10, y=190)
    e5 = tk.Entry(crwn)
    e5.place(x=150, y=190)'''

    b1 = tk.Button(crwn, text="Create Account", height=2, bg='orange',
                   command=lambda: write2(crwn, e1.get().strip(), e11.get().strip(), e6.get().strip(), e2.get().strip(),
                                          combo.get().strip(), ent.get().strip(), e5.get().strip()))
    b1.place(x=500, y=200)

    '''u1=tk.Label(crwn,text="Enter UPI:",bg='orange')
    u1.place(x=500, y=220)
    u2=tk.Label(crwn,text="Enter Amount:",bg='orange')
    u2.place(x=500, y=250)
    up1 = tk.Entry(crwn)
    up1.place(x=620, y=220)
    up2 = tk.Entry(crwn)
    up2.place(x=620, y=250)
    #b1.place(x=550, y=230)
    
    b = tk.Button(crwn, text="Create Account", command=lambda: write(crwn, e1.get().strip(),e6.get().strip(),e2.get().strip(),combo.get().strip(),ent.get().strip(),e5.get().strip(),up2.get().strip()))
    b.place(x=550, y=290)'''

    return


def Main_Menu():
    rootwn = tk.Tk()
    rootwn.geometry("1600x500")
    rootwn.title("UNITED Bank")
    rootwn.configure(background='orange')
    fr1 = tk.Frame(rootwn)
    fr1.pack(side="top")
    bg_image = tk.PhotoImage(file="pile1.gif")
    x = tk.Label(image=bg_image)
    x.place(y=-400)
    l_title = tk.Message(text="BANKING SYSTEM", relief="raised", width=2000, padx=600, pady=0, fg="white", bg="black",
                         justify="center", anchor="center")
    l_title.config(font=("Courier", "50", "bold"))
    l_title.pack(side="top")
    imgc1 = tk.PhotoImage(file="new.gif")
    imglo = tk.PhotoImage(file="login.gif")
    imgc = imgc1.subsample(2, 2)
    imglog = imglo.subsample(2, 2)

    b1 = tk.Button(image=imgc, command=Create)
    b1.image = imgc
    b2 = tk.Button(image=imglog, command=lambda: log_in(rootwn))
    b2.image = imglog
    img6 = tk.PhotoImage(file="quit.gif")
    myimg6 = img6.subsample(2, 2)

    b6 = tk.Button(image=myimg6, command=rootwn.destroy)
    b6.image = myimg6
    b1.place(x=800, y=300)
    b2.place(x=800, y=200)
    b6.place(x=920, y=400)

    rootwn.mainloop()


Main_Menu()
