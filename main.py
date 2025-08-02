from database import init_database
from reservations import Reservations
from tkinter import *
from PIL import Image,ImageTk
from home import HomePage
from booking import BookingPage
from edit_reservation import EditPage

root = Tk()
root.geometry("600x600")
root.configure(bg="#DEEBF7")
init_database()

def switch(indicator_lb,page):
    for child in options_frame.winfo_children():
        if isinstance(child, Label):
            child['bg'] = '#427AA1'
    indicator_lb['bg']='white'

    page()

options_frame = Frame(root,bg="#427AA1")

photo = Image.open("images/airplane.png")
resized_image = photo.resize((40,40), Image.Resampling.LANCZOS)
converted_image = ImageTk.PhotoImage(resized_image)

img_lbl = Label(options_frame,bg="#427AA1",image=converted_image)
img_lbl.place(x=60,y=10)

home_btn = Button(options_frame,text="Home",font=('Arial',13) , bd=0,fg='white',activeforeground='white'
                  ,bg='#427AA1',activebackground='#427AA1'
                  ,command=lambda:switch(indicator_lb=home_indicator_lb,page=Home_Page))
home_btn.place(x=1100,y=20,width=125)
home_indicator_lb = Label(options_frame,bg='white')
home_indicator_lb.place(x=1139,y=43,width=45 , height = 2)

Book_btn = Button(options_frame,text="Book Flight",font=('Arial',13) , bd=0,fg='white',activeforeground='white'
                  ,bg='#427AA1',activebackground='#427AA1',
                  command=lambda:switch(indicator_lb=Book_indicator_lb,page=Book_Page))
Book_btn.place(x=1200,y=20,width=125)
Book_indicator_lb = Label(options_frame,bg='#427AA1')
Book_indicator_lb.place(x=1222,y=43,width=82 , height = 2)

res_btn = Button(options_frame,text="View Reservations",font=('Arial',13) , bd=0,fg='white'
                 ,activeforeground='white',bg='#427AA1',activebackground='#427AA1'
                 ,command=lambda:switch(indicator_lb=res_indicator_lb,page=Res_Page))
res_btn.place(x=1330,y=20,width=135)
res_indicator_lb = Label(options_frame,bg='#427AA1')
res_indicator_lb.place(x=1332,y=43,width=132 , height = 2)

lbl = Label(options_frame,bg='#427AA1',fg='white',font=('Arial',15,'bold'),text='FlySky Reservations')
lbl.place(x=115,y=16)

options_frame.grid()
options_frame.configure(width=2000,height=65)

edit_page = EditPage(root, lambda: switch(res_indicator_lb, Res_Page))
book_page = BookingPage(root,lambda:switch(home_indicator_lb,Home_Page),lambda:switch(res_indicator_lb,Res_Page))
home_page = HomePage(root,lambda:switch(Book_indicator_lb,Book_Page),lambda:switch(res_indicator_lb,Res_Page),book_page)
res_page = Reservations(root, lambda: switch(Book_indicator_lb, Book_Page),edit_page,lambda:Edit_Page(),book_page)
edit_page.tree = res_page.tree


def Home_Page():
    res_page.grid_forget()
    book_page.grid_forget()
    edit_page.grid_forget()
    home_page.configure(bg="#DEEBF7")
    home_page.grid(row=1,column=0,sticky="nsew")

def Res_Page():
    home_page.grid_forget()
    book_page.grid_forget()
    edit_page.grid_forget()
    res_page.configure(bg="#DEEBF7")
    res_page.load_database()
    res_page.grid(row=1,column=0,sticky="nsew")

def Book_Page():
    home_page.grid_forget()
    res_page.grid_forget()
    edit_page.grid_forget()
    book_page.configure(bg="#DEEBF7")
    book_page.grid(row=1,column=0,sticky="nsew")

def Edit_Page():
    home_page.grid_forget()
    res_page.grid_forget()
    book_page.grid_forget()
    edit_page.configure(bg="#DEEBF7")
    edit_page.grid(row=1,column=0,sticky="nsew")

Home_Page()
root.mainloop()
