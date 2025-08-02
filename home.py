from tkinter import *
from PIL import Image,ImageTk

class HomePage(Frame):
    def __init__(self, master,Book_Func,Res_Func,book_page):
        Frame.__init__(self, master)
        frame1 = Frame(self, bg="white", width=500, height=500, highlightcolor="#DEEBF7", pady=20, padx=20,
                       highlightthickness=2)
        frame2 = Frame(self, bg="white", width=500, height=500, highlightcolor="#DEEBF7", pady=20, padx=20,
                       highlightthickness=2)

        lbl1 = Label(frame1, text="Book a Flight", font=('Times new roman', 20, 'bold'), padx=10, bg="white",
                     fg="#427AA1")
        lbl2 = Label(frame1, text="Reserve your next flight by providing your details and \nflight information",
                     padx=10, pady=10, bg="white", font=('Arial', 12))
        lbl3 = Label(frame2, text="View Reservations", font=('Times new roman', 20, 'bold'), padx=10, bg="white",
                     fg="#427AA1")
        lbl4 = Label(frame2, text="Manage your existing reservations, view details, edit \nor cancel if needed.",
                     padx=10, pady=10, bg="white", font=('Arial', 12))
        lbl5 = Label(self, text="Welcome to FlySky Reservations", bg="#DEEBF7", fg="#00264D",
                     font=('Arial', 40, 'bold'))

        btn1 = Button(frame1, text="Book Flight", width=45, height=2, relief="flat", bg="#427AA1", fg="white",
                      font=('Arial', 10, 'bold'),command=lambda:book_button())
        btn2 = Button(frame2, text="View Reservations", width=45, height=2, relief="flat", bg="#427AA1", fg="white",
                      font=('Arial', 10, 'bold'),command=lambda:Res_Func())

        photo1 = Image.open("images/online-booking.png")
        resized_image1 = photo1.resize((70, 70), Image.Resampling.LANCZOS)
        converted_image1 = ImageTk.PhotoImage(resized_image1)

        img1_lbl = Label(frame1, bg='white',image=converted_image1)
        img1_lbl.image = converted_image1
        img1_lbl.place(x=160, y=5)

        photo2 = Image.open("images/app.png")
        resized_image2 = photo2.resize((70, 70), Image.Resampling.LANCZOS)
        converted_image2 = ImageTk.PhotoImage(resized_image2)

        img1_lbl = Label(frame2, bg='white',image=converted_image2)
        img1_lbl.image = converted_image2
        img1_lbl.place(x=160, y=5)

        frame1.grid(row=0, column=0, padx=(350, 10), pady=300)
        frame2.grid(row=0, column=1, padx=(10, 400), pady=300)
        lbl5.place(x=380, y=150)

        lbl1.pack(pady=(100, 10))
        lbl2.pack()
        lbl3.pack(pady=(100, 10))
        lbl4.pack()

        btn1.pack()
        btn2.pack()

        def book_button():
            book_page.clear_data()
            Book_Func()


