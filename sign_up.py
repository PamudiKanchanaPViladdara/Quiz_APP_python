from tkinter import *
import tkinter.messagebox
import mysql.connector


connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="quizdb2")
cursordb = connectiondb.cursor()

class SignUp(object):
    def __init__(self):
        self.gui=Toplevel()
        self.gui.geometry("800x450")
        self.gui.title("Quiz")
        self.display_title()
        self.signup_form()
        self.gui.mainloop()
    def display_title(self):
        title = Label(self.gui, text="QUIZ MASTER 2022 ",width=50, bg="blue",fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)
        title.pack()
      
    def signup_form(self):
        Label(self.gui, text="").pack()
        Label(self.gui, text='You can create account', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=50).pack()
        global firstName,T1,lastName,username,password
               
        self.firstName = StringVar()
        self.lastName = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        
        Label(self.gui, text="").pack()
        Label(self.gui, text="First Name :", fg="black", font=('arial', 12, 'bold')).pack()
        T1=Entry(self.gui, textvariable=self.firstName).pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Last Name :", fg="black", font=('arial', 12, 'bold')).pack()
        T2=Entry(self.gui, textvariable=self.lastName).pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
        T3=Entry(self.gui, textvariable=self.username).pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        T4=Entry(self.gui, textvariable=self.password, show="*").pack()
        Label(self.gui, text="").pack()
        
        signup_button = Button(self.gui, text="Sign up", command=self.create_account,
		width=10,bg="blue", fg="white",font=("arial",12," bold"))
        signup_button.place(x=500,y=400)
        
        quit_button = Button(self.gui, text="Quit", command=self.gui.destroy,
		width=10,bg="black", fg="white",font=("arial",12," bold"))
        quit_button.place(x=620,y=400)
        
        
    
    def create_account(self):
        first= self.firstName.get()
        last= self.lastName.get()
        user = self.username.get()
        pw= self.password.get()
        y=False
        cursordb.execute("SELECT * FROM users")
        db_result = cursordb.fetchall()
        for i in range(len(db_result)):
            
            if user == db_result[i][3] :
                tkinter.messagebox.showinfo("Error!","An account of this Username already exists.")
                y=True
                break
                
        if y==False:
            x=[(first,last,user,pw, "PLAYER","INACTIVE")]
            sql_users= "INSERT INTO users(FistName,LastName,username,password,usertype,status) VALUES(%s,%s,%s,%s,%s,%s)"
            cursordb.executemany(sql_users,x)
            connectiondb.commit()
            tkinter.messagebox.showinfo("Greetings!","Account created successfully!")
            self.gui.withdraw()

   
#s=sign()
