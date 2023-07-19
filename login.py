from tkinter import *
import tkinter.messagebox
import mysql.connector
import csv
import random
import sign_up


connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="quizdb2")
cursordb = connectiondb.cursor()


class Login(sign_up.SignUp):
    def __init__(self):
        self.gui=Tk()
        self.gui.geometry("800x450")
        self.gui.title("Quiz")    
        self.display_title()
        self.login()
        
        self.gui.mainloop()

    

    def login(self):
        
        global username_verification
        global password_verification
        global T1,T2
        Label(self.gui, text="").pack()
        Label(self.gui, text='Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
        username_verification = StringVar()
        password_verification = StringVar()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
        T1=Entry(self.gui, textvariable=username_verification)
        T1.pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
        T2=Entry(self.gui, textvariable=password_verification, show="*")
        T2.pack()
        Label(self.gui, text="").pack()
        Button(self.gui, text="Login", bg="white", fg='blue', relief="solid", font=('arial', 12, 'bold'),command=self.login_verification).pack()
        Label(self.gui, text="").pack()
        
        signup_button = Button(self.gui, text="Sign up", command=self.signup_form,
		width=10,bg="blue", fg="white",font=("arial",12," bold"))
        signup_button.place(x=600,y=300)
        quit_button = Button(self.gui, text="Quit", command=self.gui.destroy,
		width=5,bg="black", fg="white",font=("arial",12," bold"))
        quit_button.place(x=720,y=300)
 

    def login_verification(self):
        user_verification = username_verification.get()
        pass_verification = password_verification.get()
        sql = "select * from users where username = %s and password = %s"
        cursordb.execute(sql,[(user_verification),(pass_verification)])
        results = cursordb.fetchall()
        if results:
            for i in results:
                self.logged()
                break
        else:
            self.failed()
    def logged_destroy(self):
        #self.gui.destroy()
        self.gui2.destroy()
        cursordb.execute("update users set status='INACTIVE'")
        connectiondb.commit()
        self.gui.deiconify()
        T1.delete(0,tkinter.END)
        T2.delete(0,tkinter.END)
      

    def failed_destroy(self):
        self.gui2.destroy()

    def logged(self):
        #self.logged_destroy()
        self.gui.withdraw()
        self.gui2=Tk()
        self.gui2.geometry("800x450")
        self.gui2.title("Login")
        Label(self.gui2, text='Quiz', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
        active_user=username_verification.get()
        Label(self.gui2, text="").pack()
        Label(self.gui2, text="Login Successfully!... Welcome {} ".format(active_user), fg="green", font="bold").pack()
        Label(self.gui2, text="").pack()
        
        value='ACTIVE'
        sql="update users set status=%s where username=%s"
        cursordb.execute(sql,(value,active_user))
        connectiondb.commit()
      
        Button(self.gui2, text="Play Quiz", bg="blue", fg='white',bd=8,width=12, relief="groove", font=('arial', 12, 'bold'), command=self.play_quiz).pack(ipadx=10,ipady=10,padx=10,pady=10)
        Button(self.gui2, text="Logout", bg="blue",fg='white',bd=8,width=12, relief="groove", font=('arial', 12, 'bold'), command=self.logged_destroy).pack(ipadx=10,ipady=10,padx=10,pady=10)
        cursordb.execute("SELECT * FROM users where status='ACTIVE'")
        db_result = cursordb.fetchall()
        utype=db_result[0][5]
        if utype=="ADMIN":
            Button(self.gui2, text="Add Questions", bg="blue", fg='white',bd=8,width=12, relief="groove", font=('arial', 12, 'bold'), command=self.add_questions_form).pack(ipadx=10,ipady=10,padx=10,pady=10)
        Button(self.gui2, text="View History ", bg="blue", fg='white',bd=8,width=12, relief="groove", font=('arial', 12, 'bold'), command=self.view_report).pack(ipadx=10,ipady=10,padx=10,pady=10)
                    

            

    def failed(self):
        
        self.gui2=Tk()
        self.gui2.geometry("800x450")
        self.gui2.title("Invalid")
        Label(self.gui2, text="Invalid Username or Password", fg="red", font="bold").pack()
        Label(self.gui2, text="").pack()
        Button(self.gui2,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=self.failed_destroy).pack()
    
    
    def play_quiz(self):
        import play_quiz
        playquiz=play_quiz.PlayQuiz()

    def signup_form(self):
        signup=sign_up.SignUp()   
        
    def add_questions_form(self):
        import add_questions
        addques=add_questions.Add_questions()
    def view_report(self):
        import view_score
        viewreport=view_score.CreateReport()
        
player=Login()




