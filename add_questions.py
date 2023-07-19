from tkinter import *
import tkinter as tk
import tkinter.messagebox
import mysql.connector
import csv
import login

connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="quizdb2")
cursordb = connectiondb.cursor()

class Add_questions(login.Login):
    
    def __init__(self):
        
        self.gui=Toplevel()
        self.gui.geometry("800x450")
        self.gui.title("Quiz")
        self.display_title()
        self.questions_form()
        self.gui.mainloop()

    
    def questions_form(self):
        Label(self.gui, text="").pack()
        Label(self.gui, text='You can add questions', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=50).pack()
        global question,option1,option2,option3,option4,answer,T1,T2,T3,T4,T5,T6
                        
        self.question = StringVar()
        self.option1 = StringVar()
        self.option2 = StringVar()
        self.option3 = StringVar()
        self.option4 = StringVar()
        self.answer=StringVar()
        
        Label(self.gui, text="").pack()
        Label(self.gui, text="Question :", fg="black", font=('arial', 12, 'bold')).pack()
        T1=Entry(self.gui, textvariable=self.question,width=100)
        T1.pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Option 1 :", fg="black", font=('arial', 12, 'bold')).pack()
        T2=Entry(self.gui, textvariable=self.option1,width=100)
        T2.pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Option 2 :", fg="black", font=('arial', 12, 'bold')).pack()
        T3=Entry(self.gui, textvariable=self.option2,width=100)
        T3.pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Option 3 :", fg="black", font=('arial', 12, 'bold')).pack()
        T4=Entry(self.gui, textvariable=self.option3,width=100)
        T4.pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Option 4 :", fg="black", font=('arial', 12, 'bold')).pack()
        T5=Entry(self.gui, textvariable=self.option4,width=100)
        T5.pack()
        Label(self.gui, text="").pack()
        Label(self.gui, text="Answer as 1,2,3,4 :", fg="black", font=('arial', 12, 'bold')).pack()
        T6=Entry(self.gui, textvariable=self.answer,width=100)
        T6.pack()
        Label(self.gui, text="").pack()
        
        add_button = Button(self.gui, text="Add", command=self.add_ques,
		width=10,bg="blue", fg="white",font=("arial",12," bold"))
        add_button.place(x=575,y=500)
        clear_button = Button(self.gui, text="Clear", command=self.clear,
		width=10,bg="blue", fg="white",font=("arial",12," bold"))
        clear_button.place(x=700,y=500)
        quit_button = Button(self.gui, text="Quit", command=self.gui.destroy,
		width=5,bg="black", fg="white",font=("arial",12," bold"))
        quit_button.place(x=670,y=550)
        
    
    def add_ques(self):
        ques= self.question.get()
        op1 = self.option1.get()
        op2 = self.option2.get()
        op3 = self.option3.get()
        op4 = self.option4.get()
        ans = self.answer.get()
        y=False
        cursordb.execute("SELECT * FROM quiz")
        db_result = cursordb.fetchall()
        for i in range(len(db_result)):
            
            if ques == db_result[i][1] :
                tkinter.messagebox.showinfo("Error!","This question is already exists.")
                y=True
                break
                
        if y==False:
            x=[(ques,op1,op2,op3,op4,ans)]
            sql_ques= "INSERT INTO quiz(Question,option1,option2,option3,option4,answer) VALUES(%s,%s,%s,%s,%s,%s)"
            cursordb.executemany(sql_ques,x)
            connectiondb.commit()
            tkinter.messagebox.showinfo("Greetings!","Question added successfully!")

            question_row=[ques]+[op1]+[op2]+[op3]+[op4]+[ans]
            newbook_file=open("quiz_sheet.csv",'a',newline="")
            newbook_writer=csv.writer(newbook_file)
            newbook_writer.writerow(question_row)
            newbook_file.close()
    def clear(self):
        T1.delete(0,tk.END)
        T2.delete(0,tk.END)
        T3.delete(0,tk.END)
        T4.delete(0,tk.END)
        T5.delete(0,tk.END)
        T6.delete(0,tk.END)
        

#s=Add_questions()
