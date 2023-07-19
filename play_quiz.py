import mysql.connector
from tkinter import *
from tkinter import messagebox as mb
import csv
import random
import login
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="quizdb2")
cursordb = connectiondb.cursor()
class PlayQuiz(login.Login):
	
	def __init__(self):
		
		self.i=0
		self.j=0
		self.k=0
		self.gui=Toplevel()
		self.gui.geometry("800x450")
		self.gui.title("Quiz")
		self.q_no=0
		self.display_title()
		self.display_question()
		self.opt_selected=IntVar()
		self.opts=self.radio_buttons()
		self.display_options()
		self.buttons()
		self.data_size=len(L)
		self.correct=0
		self.gui.mainloop()
		
	
	def display_question(self):
		question=L[self.i][0]
		# setting the Question properties
		q_no = Label(self.gui, text=question,width=60,
		font=( 'arial' ,12, 'bold' ), anchor= 'w' )
		
		#placing the option on the screen
		q_no.place(x=70, y=100)
		self.i=self.i+1

	def display_options(self): 
	    val=0 
	    options=(L[self.j][1],L[self.j][2],L[self.j][3],L[self.j][4])
	    self.j=self.j+1
		
		# deselecting the options
	    self.opt_selected.set(0)
		
		# looping over the options to be displayed for the
		# text of the radio buttons.
	    for option in options:
		    self.opts[val]['text']=option
		    val+=1
		    		    
	def buttons(self):
		# The first button is the Next button to move to the
		# next Question
		next_button = Button(self.gui, text="Submit",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("arial",12,"bold"))
		
		# palcing the button on the screen
		next_button.place(x=350,y=380)
		
		# This is the second button which is used to Quit the GUI
		quit_button = Button(self.gui, text="Quit", command=self.gui.destroy,
		width=5,bg="black", fg="white",font=("arial",12," bold"))
		
		# placing the Quit button on the screen
		quit_button.place(x=700,y=50)
   

	def radio_buttons(self):
		# initialize the list with an empty list of options
		q_list = []
		
		# position of the first option
		y_pos = 150
		
		# adding the options to the list
		while len(q_list) < 4:
			
			# setting the radio button properties
			radio_btn = Radiobutton(self.gui,text=" ",variable=self.opt_selected,
			value = len(q_list)+1,font = ("arial",12))
			
			# adding the button to the list
			q_list.append(radio_btn)
			
			# placing the button
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementing the y-axis position by 40
			y_pos += 40
		
		# return the radio buttons
		return q_list
	def next_btn(self):
                
		# Check if the answer is correct
		if self.check_ans()==True:
			mb.showinfo("Congratulations..!","Your answer is correct") 
			# if the answer is correct it increments the correct by 1
			self.correct += 1
		else: 
			y=int(L[(self.k)-1][5])
			x="The correct answer is\n "+L[(self.k)-1][y]
			mb.showinfo("Oops..Wrong answer!",x)
			
			# if the answer is correct it increments the correct by 1
			
		
		# Moves to next Question by incrementing the q_no counter
		self.q_no += 1
		
		# checks if the q_no size is equal to the data size
		if self.q_no==self.data_size:
			
			# if it is correct then it displays the score
			self.display_result()
			
			# destroys the GUI
			self.gui.destroy()
		else:
			# shows the next question
			
			
			self.display_question()
			self.display_options()
	
	def check_ans(self):
		
		# checks for if the selected option is correct
		x=L[self.k][5]
		self.k=self.k+1
				
		if self.opt_selected.get() == int(x):
			# if the option is correct it return true
			
			return True
	def display_result(self):
		
		# calculates the wrong count
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calcultaes the percentage of correct answers
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		cursordb.execute("SELECT * FROM users where status='ACTIVE'")
		db_result = cursordb.fetchall()
		active_user=db_result[0][1]
		utype=db_result[0][5]
		x=[(active_user,score,utype)]
		sql_score= "INSERT INTO user_score(username,score,usertype) VALUES(%s,%s,%s)"
		cursordb.executemany(sql_score,x)
		connectiondb.commit()
		
		# Shows a message box to display the result
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
	             
		

workbook_file=open('quiz_sheet.csv','r')
workbook_reader=csv.reader(workbook_file)
L=[]
for row in workbook_reader:
        if row==[]:
                continue
        else:
                L.append(tuple(row))
workbook_file.close()
random.shuffle(L)


# create an object of the Quiz Class.
#quiz = PlayQuiz()



