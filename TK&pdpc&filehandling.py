import csv
import tkinter as tk
from tkinter import messagebox,filedialog
import mysql.connector

#----------------------------------------
root=tk.Tk()
root.title("student manage flow")
root.geometry('550x550')
#----------------------------------------
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='Vamshi@19',
    database='student_db'
)
curser=conn.cursor()
#-------------------functions--------------------------------
def file_handling():
    path_file=filedialog.askopenfilename(filetypes=[('CSV FILE','*.CSV')])
    with open (path_file,'r') as file:
        redar=csv.reader(file)
        next(redar)
        for row in redar:
            curser.execute('insert into student (name,age,grade) values(%s,%s,%s)',(row[0],row[1],row[2]))
        conn.commit()
        messagebox.showinfo('done','inserted data')
            
def text_area_upload():
    text_box.config(state=tk.NORMAL)
    text_box.delete('1.0',tk.END)
    curser.execute('select*from student')
    rows=curser.fetchall()
    for row in rows:
        text_box.insert(tk.END,f'ID:{row[0]} NAME:{row[1]} age{row[2]} grade:{row[3]}\n')


def add_entry():
    name = entry_name.get()
    age = entry_age.get()
    grade = entry_grade.get()

    if name and age and grade:
        curser.execute(
            'INSERT INTO STUDENT (name, age, grade) values (%s, %s, %s)', (name, age, grade)
        )
        conn.commit()
        messagebox.showinfo('Success', 'Added entry')
        text_area_upload()
    else:
        messagebox.showwarning('Warning', 'Wrong Inputs')

# def update_entry():
#     id=entry_id.get()
#     name = entry_name.get()
#     age = entry_age.get()
#     grade = entry_grade.get()
#     if id:
#         curser.execute('UPDATE student SET name = '%s', age = %s, grade = '%s' WHERE id = %s',(name,age,grade,id))
#         conn.commit()
#         messagebox.showinfo('sucessfully completed the updation')
def update_entry():
    student_id = entry_id.get().strip()
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    grade = entry_grade.get().strip()

    if not student_id.isdigit():
        messagebox.showwarning('Warning', 'Enter a valid numeric ID')
        return

    if name and age.isdigit() and grade:
        curser.execute(
            'UPDATE student SET name=%s, age=%s, grade=%s WHERE id=%s',
            (name, int(age), grade, int(student_id))
        )
        conn.commit()

        if curser.rowcount > 0:
            messagebox.showinfo('Success', f'Student ID {student_id} updated successfully')
        else:
            messagebox.showwarning('Not Found', f'No student found with ID {student_id}')
    else:
        messagebox.showwarning('Warning', 'Invalid inputs')



def delete_entry():
    id=entry_id.get()
    if id:
        curser.execute('delete from student where id=%s',(id,))
        conn.commit()
        messagebox.showinfo("deleted the row")
        text_area_upload()
    else:
        messagebox.showwarning("incorrect data")

#---------------------------UI-------------------------------

tk.Button(root,text='upload csv',command=file_handling).pack()
text_box=tk.Text(root,height=10,width=40)
text_box.pack(pady=10)
text_box.config(state=tk.DISABLED)
input_frame=tk.Frame(root)
input_frame.pack()
#-----------------------------------------------------------------------
#id
label_id=tk.Label(input_frame,text='ID')
label_id.grid(row=0,column=0)

entry_id=tk.Entry(input_frame)
entry_id.grid(row=0,column=3)


#name
label_name=tk.Label(input_frame,text='name')
label_name.grid(row=0,column=4)

entry_name=tk.Entry(input_frame)
entry_name.grid(row=0,column=5)

#age
label_age=tk.Label(input_frame,text='age')
label_age.grid(row=0,column=6)

entry_age=tk.Entry(input_frame)
entry_age.grid(row=0,column=7)

#grade
label_grade=tk.Label(input_frame,text='grade')
label_grade.grid(row=0,column=8)

entry_grade=tk.Entry(input_frame)
entry_grade.grid(row=0,column=9)

#--------------------------------------------------------------

buttons_frame=tk.Frame(root)
buttons_frame.pack()
tk.Button(buttons_frame,text='ADD',command=add_entry).grid(row=0,column=0,padx=10)
tk.Button(buttons_frame,text='UPDATE',command=update_entry).grid(row=0,column=1,padx=10)
tk.Button(buttons_frame,text='DELETE',command=delete_entry).grid(row=0,column=2,padx=10)


text_area_upload()


root.mainloop()
