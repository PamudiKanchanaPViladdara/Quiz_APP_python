import tkinter as tk
import mysql.connector
import login
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="quizdb2")
cursordb = connectiondb.cursor()

class CreateReport(login.Login):
    def __init__(self):
        self.gui=tk.Toplevel()
        self.gui.geometry("800x450")
        self.gui.title("Quiz")
        self.display_title()
        self.report_window()
        self.gui.mainloop()
    
    def report_window(self):
        tk.Label(self.gui, text="").pack()
        
        tk.Label(self.gui, text='You can view user scores', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=50).pack()
        tk.Label(self.gui, text="").pack()
        show_button = tk.Button(self.gui, text="Show", command=self.show_records,
		width=10,bg="blue", fg="white",font=("arial",12," bold"))
        show_button.place(x=500,y=100)
        
        quit_button = tk.Button(self.gui, text="Quit", command=self.gui.destroy,
		width=10,bg="black", fg="white",font=("arial",12," bold"))
        quit_button.place(x=750,y=100)

    def show_records(self):
        tk.Label(self.gui, text="").pack()
        tk.Label(self.gui, text="").pack()
        T = tk.Text(self.gui, height = 5, width = 52)
        cursordb.execute("SELECT * FROM users where status='ACTIVE'")
        db_result = cursordb.fetchall()
        utype=db_result[0][5]
        if utype=="ADMIN":
            cursordb.execute("SELECT username ,score  FROM user_score")
            result = cursordb.fetchall()
        else:
            cursordb.execute("SELECT username ,score FROM user_score where username in (select username from users where status='ACTIVE')")
            result = cursordb.fetchall()
            
        s=""
        for i in range(len(result)):
            s=s+str(result[i])+"\n"
        T.pack()
        T.insert(tk.END, s)
    

    
        
#r=CreateReport()


