from tkinter import *
from tkinter import messagebox
import ast

root=Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#FFFFFF")
root.resizable(False,False)
img=PhotoImage(file="login01.png")
Label(root,image=img,bg="white").place(x=50,y=50)

def signin():
    username=user.get()
    password=code.get()
    if username=="admin" and password=="admin":
        messagebox.showinfo("Aviso","Inicio de Sesión Exitoso.")
        window2()
    elif username!="admin" and password!="admin":
        messagebox.showerror("Error","Clave o Contraseña incorrectos")
    elif password!="admin":
        messagebox.showerror("Error","Contraseña incorrecta")
    elif username!="admin":
        messagebox.showerror("Error","Usuario incorrecto")

def signup_command():
    root.destroy()

frame=Frame(root,width=360,height=350,bg="White")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign In",fg="#57A1F8",font=("Arial",23,"bold"))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,"end")

def on_leave(e):
    name=user.get()
    if name=="":
        user.insert(0,"Username")

user=Entry(frame,width=25,fg="Black",border=0,bg="White",font=("Arial",11))
user.place(x=30,y=80)
user.insert(0,"Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="Black").place(x=25,y=107)

def on_enter(e):
    code.delete(0,"end")

def on_leave(e):
    name=code.get()
    if name=="":
        code.insert(0,"Password")
        
code=Entry(frame,width=25,fg="Black",border=0,bg="White",font=("Arial",11))
code.place(x=30,y=150)
code.insert(0,"Password")
code.bind("<FocusIn>", on_enter)
code.bind("<FocusOut>", on_leave)

Frame(frame,width=295,height=2,bg="Black").place(x=25,y=177)

Button(frame,width=39,pady=7,text="Sign In",bg="#57A1F8",fg="White",border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don´t have an account?",fg="Black",bg="White",font=("Arial",11))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text="Sign Up",font=("Arial",9),border=0,bg="White",cursor="hand2",fg="#57A1F8",command=signup_command)
sign_up.place(x=240,y=271)

def window2():
    screen=Toplevel(root)
    screen.title("App")
    screen.geometry("925x500+300+200")
    screen.config(bg="white")
    Label(screen,text="Hello", bg="#FFFFFF",font=("Calibri(Body)",50,"bold")).pack(expand=True)
    screen.mainloop()

root.mainloop()
