import tkinter as tk
from tkinter import ttk
from tkcalendar import *
import mysql.connector as mysql
from tkinter import messagebox
from time import gmtime, strftime

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


def write2(master, fname, lname, aadhar, pan , addr, gen, dob, type1 , pin):  # zero balance
    aa = str(aadhar)
    pi = str(pin)
    name = str(fname + ' ' + lname)
    fname=fname[:5]
    print(type1)
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

    ifs="UNIB"
    f2 = open("Ifsc_Record.txt", 'r')
    ifsc = int(f2.readline())
    ifsc += 1
    f2.close()
    f2 = open("Ifsc_Record.txt", 'w')
    f2.write(str(ifsc))
    f2.close()


    ifs=ifs+str(ifsc)
    ad = "A" + str(accnt_no)
    oc = '0'
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute(
        "create table " + ad + " (ifsc INT(100), amount VARCHAR(100), balance VARCHAR(100), fromq VARCHAR(100), date VARCHAR(100), time VARCHAR(100),upi VARCHAR(100),day INT,month INT)")
    cursor.execute("commit")
    print("Executed")
    con.close()
    x = strftime("%d/%m/%Y")
    y = strftime("%H-%M-%S")

    upi = str(fname) + "@UNION"
    ab = "CREATED"
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute(
        "insert into account values('" + str(accnt_no) + "','"+ str(ifs) +"','" + str(name) + "','" + str(aadhar) + "','" +str(pan)+ "','"+ str(
            addr) + "','" + str(gen) + "','" + str(dob) + "','"+str(type1)+"','"+ str(pin) + "','" + str(oc) + "','" + str(upi) + "')")
    cursor.execute("commit")
    con.close()

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute(
        "insert into " + ad + " values('" +str(ifs)+ "','" +str(oc)+ "','" +str(oc)+ "','" + str(ab) + "','" + str(x) + "','" + str(
            y) + "','"+ str(ab) +"','0','0')")
    cursor.execute("commit")
    print("Executed")
    con.close()

    messagebox.showinfo("Details", "Your Account Number is:" + str(accnt_no)+"\n Your IFSC Code is:"+str(ifs))
    master.destroy()
    return

def change(upi, amti, bal22, acc):
    ad2 = "A" + str(upi)
    print(ad2)
    c = "CREDIT"
    x = strftime("%d/%m/%Y")
    y = strftime("%H-%M-%S")

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select ifsc from " + str(ad2) + " ORDER BY ifsc DESC LIMIT 1;")
    ii = cursor.fetchall()
    for row2 in ii:
        i1 = row2[0]
    i1=int(i1)+1
    cursor.execute("select day from " + str(ad2) + " ORDER BY ifsc DESC LIMIT 1;")
    ii = cursor.fetchall()
    for row2 in ii:
        day1 = row2[0]
    cursor.execute("select month from " + str(ad2) + " ORDER BY ifsc DESC LIMIT 1;")
    i2 = cursor.fetchall()
    for row2 in i2:
        mon1 = row2[0]
    i1=int(i1)+1
    cursor.execute("insert into " + ad2 + " values('" +str(i1)+ "','" +str(amti)+ "','" + str(bal22) + "','" + str(c) + "','" + str(
        x) + "','" + str(y) + "','" + str(acc) + "','"+str(day1)+"','"+str(mon1)+"')")
    cursor.execute("commit")
    print("Executed")
    con.close()


def debit_write(master, amt, accnt, upi, ifsc, name):
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    try:
        cursor.execute("select ifsc from account where Accountno='" + str(upi) + "'")
        rows = cursor.fetchall()
        for row in rows:
            t2 = row[0]
        if t2!=ifsc:
            print(ifsc)
            messagebox.showinfo("Error", "Enter Correct Details\nPlease try again.")
            master.destroy()
            return
    except:
        pass

    cursor.execute("select type from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()

    for row in rows:
        tt = row[0]
    if (tt == "Savings"):
        print("SAVINGS")
        Savings(master, amt, accnt, upi)
    else:
        print("CURRENT")
        Current(master, amt, accnt, upi)


def Current(master, amt, accnt, upi):
    print("CURRENT")
    if (is_number(amt) == 0):
        messagebox.showinfo("Error", "Enter Details\nPlease try again.")
        master.destroy()
        return

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select Balance from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()

    for row in rows:
        bal = row[0]
    con.close()

    if (int(amt) > bal):
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        ad = "A" + str(accnt)
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select date from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
        d = cursor.fetchall()

        for row in d:
            day = row[0]
            print(day)
        con.close()

        mon = day[3:]
        x1 = strftime("%d/%m/%Y")
        # x1 = "26-05-2021"
        y1 = strftime("%m/%Y")

        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select month from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
        d = cursor.fetchall()
        for rows in d:
            mon1 = rows[0]
            print(mon1)
        con.close()

        mon1 = int(mon1) + int(amt)
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select day from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
        d = cursor.fetchall()
        for row1 in d:
            day1 = row1[0]
        con.close()
        day1 = int(day1) + int(amt)
        if str(mon) == str(y1):
            print(mon)
            if mon1 > 1000000:
                messagebox.showinfo("WARNING!!", "Monthly transaction limit Reached!!")
                master.destroy()
            elif str(day) == str(x1):
                if day1 > 100000:
                    messagebox.showinfo("WARNING!!", "Daily transaction limit Reached!!")
                    master.destroy()
                else:
                    print(mon)
                    send(master, amt, accnt, upi, day1, mon1)
            else:
                day1 = amt
                send(master, amt, accnt, upi, day1, mon1)

        else:
            mon1 = amt
            day1 = amt
            send(master, amt, accnt, upi, day1, mon1)

def Savings(master, amt, accnt, upi):
    print("CURRENT")
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
    con.close()

    if (int(amt) > bal):
        messagebox.showinfo("Error!!", "You dont have that amount left in your account\nPlease try again.")
    else:
        ad = "A" + str(accnt)
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select date from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
        d = cursor.fetchall()

        for row in d:
            day = row[0]
            print(day)
        con.close()

        mon = day[3:]
        x1 = strftime("%d/%m/%Y")
        #x1 = "26-05-2021"
        y1 = strftime("%m/%Y")

        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select month from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
        d = cursor.fetchall()
        for rows in d:
            mon1 = rows[0]
            print(mon1)
        con.close()

        mon1 = int(mon1) + int(amt)
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select day from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
        d = cursor.fetchall()
        for row1 in d:
            day1 = row1[0]
        con.close()
        day1 = int(day1) + int(amt)
        if str(mon) == str(y1):
            print(mon)
            if mon1 > 100000:
                messagebox.showinfo("WARNING!!", "Monthly transaction limit Reached!!")
                master.destroy()
            elif str(day) == str(x1):
                if day1 > 20000:
                    messagebox.showinfo("WARNING!!", "Daily transaction limit Reached!!")
                    master.destroy()
                else:
                    print(mon)
                    send(master, amt, accnt, upi, day1, mon1)
            else:
                day1=0
                send(master, amt, accnt, upi, day1, mon1)

        else:
            mon1=0
            day1=0
            send(master, amt, accnt, upi, day1, mon1)

def send(master, amt, accnt, upi, day1, mon1):
    print("SEND")
    bal55=0
    acc1=""
    ac=[]
    c = "DEBIT"
    ad = "A" + str(accnt)
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select date from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
    d = cursor.fetchall()
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select Balance from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()
    for row in rows:
        bal = row[0]


    for row in d:
        day = row[0]
    con.close()
    if len(upi)==12 and upi[:3]=="950":
        print(len(upi))
        z=1
    elif upi[6:]=="UNION":
        print(upi[6:])
        z=2
    else:
        print(upi[6:])
        messagebox.showinfo("Error!!", "Account Not Found!!")
        return
    if z==1:
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select AccountNo from account ")
        rr = cursor.fetchall()
        for row in rr:
            ac.append(row[0])
        con.close()
        for at in ac:
            if str(at)==str(upi):
                x=True
                break
            else:
                print(at)
                x = False
    if z==2:
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select UPI from account ")
        rr = cursor.fetchall()
        for row in rr:
            ac.append(row[0])
        con.close()
        for at in ac:
            if str(at) == str(upi):
                x = True
                break
            else:
                print(at)
                x = False
    if x==False:
        messagebox.showinfo("Error!!", "Account Not Found!!")
        return

    mon = day[3:]
    x1 = strftime("%d/%m/%Y")
    y1 = strftime("%m/%Y")
    amti = int(amt)
    cb = bal - amti
    cb = str(cb)
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("update account set Balance='" + cb + "' where AccountNo='" + accnt + "'")
    cursor.execute("commit")
    con.close()
    x = strftime("%d/%m/%Y")
    y = strftime("%H-%M-%S")
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    '''cursor.execute(
         "insert into {0} values(\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\')".format(ad, str(amt), str(cb),
                                                                                        str(c), str(x), str(y),
                                                                                            str(upi)))'''
    cursor.execute("select ifsc from " + str(ad) + " ORDER BY ifsc DESC LIMIT 1;")
    ii = cursor.fetchall()
    for row2 in ii:
        i1 = row2[0]
    i1=int(i1)+1
    cursor.execute("insert into " + ad + " values('" +str(i1)+ "','" +str(amt)+ "','" + str(cb) + "','" + str(c) + "','" + str(
        x) + "','" + str(y) + "','" + str(upi) + "','"+str(day1)+"','"+str(mon1)+"')")
    cursor.execute("commit")
    con.close()


    try:
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()

        cursor.execute("select Balance from account where Accountno='" + upi + "'")
        rows = cursor.fetchall()

        for row3 in rows:
            bal2 = row3[0]
        bal22 = bal2 + amti
        cursor.execute("update account set Balance='" + str(bal22) + "' where AccountNo='" + str(upi) + "'")
        cursor.execute("commit")
        con.close()
        print(upi)
        change(upi, amti, bal22, accnt)
    except:
        pass
    try:
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select Balance from account where UPI='" + upi + "'")
        rows = cursor.fetchall()
        for row4 in rows:
            bal55 = row4[0]
        bal22 = bal55 + amti
        cursor.execute("update account set Balance='" + str(bal22) + "' where UPI='" + upi + "'")
        cursor.execute("select Accountno from account where UPI='" + upi + "'")
        rows = cursor.fetchall()
        for row4 in rows:
            acc1 = row4[0]
        cursor.execute("commit")
        cursor.close()
        change(acc1, amti, bal22, accnt)
    except:
        pass



    messagebox.showinfo("Operation Successfull!!", "Amount Debited Successfully!!")
    master.destroy()
    return




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
    l2 = tk.Label(debitwn, bg='orange', text="Enter IFSC Code:")
    e2 = tk.Entry(debitwn)
    l1 = tk.Label(debitwn, bg='orange', text="Enter Amount to be debited: ")
    e1 = tk.Entry(debitwn)
    l.place(x=10, y=100)
    e.place(x=170, y=100)
    l2.place(x=10, y=130)
    e2.place(x=170, y=130)
    l1.place(x=10, y=160)
    e1.place(x=170, y=160)
    b = tk.Button(debitwn, text="Debit", relief="raised",
                  command=lambda: debit_write(debitwn, e1.get(), accnt, e.get(),e2.get(), name))
    b.place(x=280, y=190)
    debitwn.bind("<Return>", lambda x: debit_write(debitwn, e1.get(), accnt, e2.get(), name))


def disp_bal(accnt):
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select Balance from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()

    for row in rows:
        bal = row[0]
    messagebox.showinfo("Balance", bal)
    con.close()

def disp(offset,accnt):
    root = tk.Tk()
    root.configure(background='yellow')
    root.title("Transaction History")
    disp_tr_hist(root,offset, accnt)

def disp_tr_hist(root,offset,accnt):

    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    accnt1 = "a" + str(accnt)
    #cursor.execute("SELECT * FROM " + str(accnt1) + " order by date limit 0,100")
    cursor.execute("SELECT count(*) as no from " + str(accnt1))
    data_row = cursor.fetchone()
    no_rec = data_row[0]
    limit = 7

    q = "SELECT * FROM " + str(accnt1) + " order by date limit  "+ str(offset) +","+str(limit)
    cursor.execute(q)
    e = tk.Label(root, width=10, text='Sr.No.', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = tk.Label(root, width=10, text='Amount', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = tk.Label(root, width=10, text='Balance', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = tk.Label(root, width=10, text='Credit/Debit', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = tk.Label(root, width=10, text='Date', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = tk.Label(root, width=10, text='Time', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    e = tk.Label(root, width=10, text='From/To', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=6)
    i = 1
    for student in cursor:
        for j in range(len(student)):
            if j == 7:
                break
            e = tk.Entry(root, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(tk.END, student[j])
        i = i + 1
    while (i <= limit):
        for j in range(len(student)):
            if j == 7:
                break
            e = tk.Entry(root, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(tk.END, "")
        i = i + 1
    back = offset - limit
    next = offset + limit
    b1 = tk.Button(root, text='Next >', command=lambda: disp_tr_hist(root,next,accnt))
    b1.grid(row=12, column=4)
    b2 = tk.Button(root, text='< Prev', command=lambda: disp_tr_hist(root,back,accnt))
    b2.grid(row=12, column=1)
    if (int(no_rec) <= next):
        b1["state"] = "disabled"
    else:
        b1["state"] = "active"

    if (back >= 0):
        b2["state"] = "active"
    else:
        b2["state"] = "disabled"

    root.mainloop()

def View(accnt):
    crwn = tk.Tk()
    crwn.geometry("720x400")
    crwn.title("View Account")
    crwn.configure(bg="orange")
    l_title = tk.Message(crwn, text="View Account", relief="raised", width=2000, padx=600, pady=0, fg="white",
                         bg="black", justify="center", anchor="center")
    l_title.pack(side="top")
    l_title.config(font=("Courier", "50", "bold"))
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("select * from account where Accountno='" + accnt + "'")
    rows = cursor.fetchall()
    for r2 in rows:
        name = r2[2]
        aadhar = r2[3]
        pan = r2[4]
        addr = r2[5]
        gender = r2[6]
        dob = r2[7]
        type = r2[8]
        upi = r2[11]
        ifsc=r2[1]
        acc=r2[0]
    l1 = tk.Label(crwn, text="Name:", bg='orange',font='10')
    l1.place(x=10, y=100)
    e1 = tk.Label(crwn, text=str(name), bg='orange',font='10')
    e1.place(x=170, y=100)

    l11 = tk.Label(crwn, text="Account No.", bg='orange', font='10')
    l11.place(x=400, y=100)
    e11 = tk.Label(crwn, text=str(acc), bg='orange', font='10')
    e11.place(x=560, y=100)

    l12 = tk.Label(crwn, text="IFSC:", bg='orange', font='10')
    l12.place(x=400, y=140)
    e12 = tk.Label(crwn, text=str(ifsc), bg='orange', font='10')
    e12.place(x=560, y=140)

    l11 = tk.Label(crwn, text="Aadhar No.:", bg='orange',font='10')
    l11.place(x=10, y=140)
    e11 = tk.Label(crwn, text=str(aadhar), bg='orange',font='10')
    e11.place(x=170, y=140)

    l6 = tk.Label(crwn, text="Pan card No.:", bg='orange',font='10')
    e6 = tk.Label(crwn, text=str(pan), bg='orange',font='10')
    l6.place(x=10, y=180)
    e6.place(x=170, y=180)

    l61 = tk.Label(crwn, text="Address:", bg='orange',font='10')
    e61 = tk.Label(crwn, text=addr, bg='orange',font='10')
    l61.place(x=10, y=220)
    e61.place(x=170, y=220)

    l2 = tk.Label(crwn, text="Gender:", bg='orange',font='10')
    l2.place(x=10, y=260)
    e2 = tk.Label(crwn, text=str(gender), bg='orange',font='10')
    e2.place(x=170, y=260)

    l3 = tk.Label(crwn, text="Date of Birth:", bg='orange',font='10')
    l3.place(x=10, y=300)
    combo = tk.Label(crwn, text=str(dob), bg='orange',font='10')
    combo.place(x=170, y=300)

    l4 = tk.Label(crwn, text="Type of Account:", bg='orange',font='10')
    l4.place(x=10, y=340)
    ent = tk.Label(crwn, text=str(type), bg='orange',font='10')
    ent.place(x=170, y=340)

    l4 = tk.Label(crwn, text="UPI:", bg='orange',font='10')
    l4.place(x=400, y=180)
    e4 = tk.Label(crwn, text=str(upi), bg='orange',font='10')
    e4.place(x=560, y=180)


def logged_in_menu(accnt, name):
    rootwn = tk.Tk()
    rootwn.geometry("1600x500")
    rootwn.title("UNITED BANK-" + name)
    rootwn.configure(background='orange')
    offset = 0
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
                   height=2, command=lambda: disp(0,accnt))
    b7 = tk.Button(text='View Account', bg='black', fg='white', font=("Courier", "15", "bold"), width=20,
                   height=2, command=lambda: View(accnt))
    b6 = tk.Button(text='Log Out', bg='red', fg='white', font=("Courier", "10", "bold"), width=20, height=2,
                   command=lambda: logout(rootwn))

    # b2.place(x=100,y=175)
    b3.place(x=100, y=170)
    b4.place(x=100, y=260)
    b5.place(x=1200, y=260)
    b6.place(x=670, y=400)
    b7.place(x=1200,y=170)


def logout(master):
    messagebox.showinfo("Logged Out", "You Have Been Successfully Logged Out!!")
    master.destroy()
    Main_Menu()

def admin(offset):
    root = tk.Tk()
    root.configure(background='yellow')
    root.title("Transaction History")
    adminview(root,offset)

def adminview(root,offset):
    con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
    cursor = con.cursor()
    cursor.execute("SELECT count(*) as no from account")
    data_row = cursor.fetchone()
    no_rec = data_row[0]
    limit = 7

    q = "SELECT * FROM account order by AccountNo limit  " + str(offset) + "," + str(limit)
    cursor.execute(q)
    e = tk.Label(root, width=10, text='Account No.', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=0)
    e = tk.Label(root, width=10, text='IFSC Code:', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=1)
    e = tk.Label(root, width=10, text='Name', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=2)
    e = tk.Label(root, width=10, text='Aadhar No.', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=3)
    e = tk.Label(root, width=10, text='Pan No.', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=4)
    e = tk.Label(root, width=10, text='Address', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=5)
    e = tk.Label(root, width=10, text='Gender', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=6)
    e = tk.Label(root, width=10, text='Date of Birth', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=7)
    e = tk.Label(root, width=10, text='Account Type', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=8)
    '''e = tk.Label(root, width=10, text='UPI', borderwidth=1, anchor='w', bg='yellow')
    e.grid(row=0, column=9)'''

    i = 1
    for student in cursor:
        for j in range(len(student)):
            if j == 9:
                break
            if j == 5:
                e = tk.Entry(root, width=25, fg='blue')
            else:
                e = tk.Entry(root, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(tk.END, student[j])
        i = i + 1
    while (i <= limit):
        for j in range(len(student)):
            if j == 9:
                break
            if j==5:
                e = tk.Entry(root, width=25, fg='blue')
            else:
                e = tk.Entry(root, width=15, fg='blue')
            e.grid(row=i, column=j)
            e.insert(tk.END, "")
        i = i + 1
    back = offset - limit
    next = offset + limit
    b1 = tk.Button(root, text='Next >', command=lambda: adminview(root, next))
    b1.grid(row=12, column=4)
    b2 = tk.Button(root, text='< Prev', command=lambda: adminview(root, back))
    b2.grid(row=12, column=1)
    if (int(no_rec) <= next):
        b1["state"] = "disabled"
    else:
        b1["state"] = "active"

    if (back >= 0):
        b2["state"] = "active"
    else:
        b2["state"] = "disabled"

    root.mainloop()

def check_log_in(master, acc_num, pin):
    l=0
    if is_number(pin) == 0:
        if acc_num == "admin" and pin == "password":
            offset = 0
            admin(offset)
            log_in(master)
            l=1
            print("Executed")
            master.destroy()
        else:
            messagebox.showinfo("Error", "Invalid Credentials \nPlease try again.")
            log_in(master)
            master.destroy()


    try:
        con = mysql.connect(host="localhost", user="root", passwd="", database="bank")
        cursor = con.cursor()
        cursor.execute("select Pin from account where Accountno='" + acc_num + "'")
        rows = cursor.fetchall()
        for row in rows:
            gpin = row[0]
        if gpin!=pin:
            messagebox.showinfo("Error", "Wrong account or pin\nPlease try again.")
        cursor.execute("select Name from account where Accountno='" + acc_num + "'")
        rows1 = cursor.fetchall()
        for row1 in rows1:
            name = row1[0]
    except:
        if l==0 :
            messagebox.showinfo("Error", "Data not Found\nPlease try again.")


    try:
        if gpin == pin:
            master.destroy()
            logged_in_menu(acc_num, name)
            print("Executed")
            con.close()


    except:
        '''messagebox.showinfo("Error", "Invalid Credentials\nPlease try again.")
        log_in(master)'''
        return



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
    l2 = tk.Label(loginwn, text="Enter account number:", bg='orange')
    l2.place(x=10, y=100)
    e2 = tk.Entry(loginwn)
    e2.place(x=150, y=100)
    l3 = tk.Label(loginwn, text="Enter your PIN:", bg='orange')
    l3.place(x=10, y=130)
    e3 = tk.Entry(loginwn, show="*")
    e3.place(x=150, y=130)
    b = tk.Button(loginwn, text="Submit",
                  command=lambda: check_log_in(loginwn, e2.get().strip(), e3.get().strip()))
    b.place(x=120, y=200)
    b1 = tk.Button(text="HOME", relief="raised", bg="black", fg="white", command=lambda: home_return(loginwn))
    b1.place(x=420, y=200)

    loginwn.bind("<Return>", lambda x: check_log_in(loginwn,  e2.get().strip(), e3.get().strip()))


def Create():
    crwn = tk.Tk()
    crwn.geometry("800x400")
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

    l61 = tk.Label(crwn, text="Enter Pan card No.:", bg='orange')
    e61 = tk.Entry(crwn, width="40")
    l61.place(x=10, y=190)
    e61.place(x=150, y=190)

    l2 = tk.Label(crwn, text="Enter Address:", bg='orange')
    l2.place(x=10, y=220)
    e2 = tk.Entry(crwn, width="40")
    e2.place(x=150, y=220)

    l3 = tk.Label(crwn, text="Gender:", bg='orange')
    l3.place(x=10, y=250)
    combo = tk.ttk.Combobox(crwn, value=option, width="37")
    combo.set("----Select Gender----")
    combo.place(x=150, y=250)

    l4 = tk.Label(crwn, text="Date of Birth:", bg='orange')
    l4.place(x=10, y=280)
    ent = DateEntry(crwn, width=15, bg='blue', fg='red', borderwidth=3, date_pattern='dd/mm/yy')
    ent.place(x=150, y=280)

    l4 = tk.Label(crwn, text="Type of Account:", bg='orange')
    l4.place(x=10, y=310)
    rq = tk.StringVar(crwn)
    q1 = tk.Radiobutton(crwn, text="Savings Account",variable=rq,value="Savings", bg='orange')
    q1.place(x=150, y=310)
    q2 = tk.Radiobutton(crwn, text="Current Account",variable=rq,value="Current", bg='orange')
    q2.place(x=300, y=310)

    l5 = tk.Label(crwn, text="Enter desired 4-digit PIN:", bg='orange')
    e5 = tk.Entry(crwn, show="*", width="40")
    l5.place(x=10, y=340)
    e5.place(x=150, y=340)
    b1 = tk.Button(crwn, text="Create Account", height=2,
                   command=lambda: write2(crwn, e1.get().strip(), e11.get().strip(), e6.get().strip(),e61.get().strip(), e2.get().strip(),
                                          combo.get().strip(), ent.get().strip(), rq.get(), e5.get().strip()))
    b1.place(x=500, y=200)
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
