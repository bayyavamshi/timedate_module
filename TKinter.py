# import tkinter as tk
# from tkinter import messagebox
# # def sayhello():
# #     print("hii avery one")
# # def check_box():
# #     if var.get()==0:
# #         messagebox.showwarning("plz select the box")
# #     else:
# #         messagebox.showinfo("sucessfully completed")
# # def radio_btn():
# #     print(choice.get())

# root=tk.Tk()
# root.title("first app")
# root.geometry('500x500')
# # tk.Label(root,text="hello vamshi",font=('arial',16)).pack(pady=20)
# # tk.Button(root,text='click me',command=sayhello).pack()
# # tk.Entry(root).pack()
# # tk.Entry(root,show='*',background='green').pack()
# # tk.Text(root,height='3',width='89').pack()
# # var=tk.IntVar()
# # tk.Checkbutton(root,text='option a',variable=var,command=check_box).pack()
# # # tk.Checkbutton(root,text='option a',variable=var,command=check_box).pack()
# # choice=tk.StringVar()
# # tk.Radiobutton(root,text='option a',variable=var,value='A',command=radio_btn).pack()
# # tk.Radiobutton(root,text='option b',variable=var,value='B',command=radio_btn).pack()
# # tk.Radiobutton(root,text='option c',variable=var,value='c',command=radio_btn).pack()
# # listiteams=tk.Listbox(root)
# # listiteams.insert(1,'python')
# # listiteams.insert(2,'java')
# # listiteams.insert(3,'html')
# # listiteams.pack()
# tk.Button(root,text='click1').grid(row=0,column=0)
# tk.Button(root,text='click2').grid(row=0,column=1)
# tk.Button(root,text='click3').grid(row=1,column=0)
# tk.Button(root,text='click4').grid(row=1,column=1)
# frame=tk.Frame(root,bd=5,height=340,width=466,relief='groove')
# frame.grid()
# tk.Label(frame,text='inside a frame').pack()
# tk.Button(frame,text="click me").pack()
# root.mainloop()



import tkinter as tk
from tkinter import messagebox
# root = tk.Tk()
# root.geometry("400x200")

# buttonframe = tk.Frame(root, bg="lightgray")
# buttonframe.pack(fill="both", expand=True)

# # Configure how columns expand
# buttonframe.columnconfigure(0, weight=1)   # column 0 expands
# buttonframe.columnconfigure(1, weight=3)   # column 1 expands more
# buttonframe.columnconfigure(2, weight=4) 

# # Add buttons in grid
# tk.Button(buttonframe, text="Button 1").grid(row=0, column=0)
# tk.Button(buttonframe, text="Button 2").grid(row=0, column=1 )
# tk.Button(buttonframe, text="Button 3").grid(row=0, column=2 )


# tk.Button(buttonframe, text="Button 4").grid(row=1, column=0, sticky="nsew")
# tk.Button(buttonframe, text="Button 4").grid(row=1, column=1, sticky="nsew")
# tk.Button(buttonframe, text="Button 4").grid(row=1, column=2, sticky="nsew")

# root.mainloop()
root=tk.Tk()
root.title('this is vamshi')
root.geometry('500x500')
tk.Label(root,text="enter your details",font=('arial',28)).pack()
username=tk.Entry(root,width=20)
username.pack()
usrepassword=tk.Entry(root,show='.')
usrepassword.pack()
def submit():
    if(username.get()=='vamshi'):
        if(usrepassword.get()=='12345'):
            try:
                with open('text_file.txt','r') as f:
                    r=f.read()
                    print(r)
                    print("commond sucessfully excuted")
            except FileNotFoundError as e:
                print(e)
        else:
            messagebox.showwarning("incorrect password")
    else:
        messagebox.showerror("incorrect username")


tk.Button(root,text='submit',command=submit).pack()
root.mainloop()