from datetime import date
from tkinter import *
from tkinter import ttk
import sqlite3

class Reservations(Frame):
    def __init__(self,master,Book_Func,edit_page,Edit_Page,book_page):
        Frame.__init__(self,master)
        self.Book_Func = Book_Func
        self.edit_page = edit_page
        self.Edit_Page = Edit_Page
        self.book_page = book_page

        db = sqlite3.connect('flights.db')
        cr = db.cursor()
        cr.execute("SELECT * FROM reservations")
        reservations = cr.fetchall()
        db.close()

        style = ttk.Style()
        self.frame1 = Frame(self ,bg="white", pady=30, padx=30)
        self.frame1.grid(row=0, column=0, padx=250, pady=(140, 400), sticky="nsew")
        self.lbl1 = Label(self, text="Your Reservations", bg="#DEEBF7", fg="#00264D",
                     font=('Arial', 25, 'bold'))
        self.lbl1.place(x=245, y=80)

        self.btn1 = Button(self, text="Book New Flight",width=15,height=2, relief="flat", bg="#427AA1", fg="white",
                      font=('Arial', 10, 'bold'),command=lambda:self.book_button())

        self.btn1.grid(row=0, column=0, padx=(0,250),pady=80,sticky="ne")

        self.search = Entry(self, fg="gray", font=('Arial', 12), width=27, highlightcolor="black", highlightthickness=1)
        self.search.grid(row=0, column=0, padx=(0, 390), pady=82, sticky="ne", ipady=8)
        self.search.insert(0, 'search by flight number')
        self.search.bind('<FocusIn>',self.search_focus_in)
        self.search.bind('<FocusOut>', self.search_focus_out)
        self.search.bind('<KeyRelease>',lambda e:self.search_by_FlightNumber(self.search.get()))

        self.btn3 = Button(self, text="Update", width=15, height=2, relief="flat", bg="#427AA1", fg="white",
                           font=('Arial', 10, 'bold'), command=lambda: self.put_data())
        self.btn4 = Button(self, text="Delete", width=15, height=2, relief="flat", bg="#427AA1", fg="white",
                           font=('Arial', 10, 'bold'), command=lambda: self.delete_data())

        self.tree = ttk.Treeview(self, columns=("Flight Number", "Name", "Departure", "Destination", "Date", "Seat"),
                                 show="headings")

        style.configure("Treeview.Heading", font=("Arial", 11, 'bold'))
        style.configure("Treeview", font=("Arial", 10))
        self.load_database()
    def search_focus_in(self,event):
        if self.search.get() == 'search by flight number':
            self.search.delete(0, END)
            self.search.config(fg="black")

    def search_focus_out(self,event):
        if self.search.get() == '':
            self.search.insert(0,'search by flight number')
            self.search.config(fg="gray")

    def load_database(self):
        db = sqlite3.connect('flights.db')
        cr = db.cursor()
        cr.execute("SELECT * FROM reservations")
        reservations = cr.fetchall()
        db.close()
        if reservations:
            for item in self.tree.get_children():
                self.tree.delete(item)
            print(reservations[0][0:6])

            for r in range(len(reservations)):
                self.tree.insert(parent='', iid=r, index='end', values=reservations[r][0:6])
        else:
            for item in self.tree.get_children():
                self.tree.delete(item)

        if (len(reservations) == 0):
            self.tree.grid_forget()
            self.btn3.grid_forget()
            self.btn4.grid_forget()
            self.btn2 = Button(self.frame1, text="Book Your First Flight", width=20, height=2, relief="flat",
                               bg="#427AA1",
                               fg="white", font=('Arial', 10, 'bold'), command=lambda: self.book_button())
            self.lbl2 = Label(self.frame1, text='No Reservations Found', bg="white", fg="black",
                              font=('Times new roman', 16, 'bold'))
            self.lbl3 = Label(self.frame1, text="You haven't booked any flights yet", bg="white", fg="#326aa3",
                              font=('Times new roman', 14))

            self.btn2.grid(row=0, column=0, padx=(400, 400), pady=(110, 10), sticky='nsew')
            self.lbl2.grid(row=0, column=0, pady=(10, 0), sticky="n")
            self.lbl3.grid(row=0, column=0, pady=(50, 0), sticky="n")

        else:
            self.tree.column("Flight Number", width=170, anchor="center")
            self.tree.column("Name", width=170, anchor="center")
            self.tree.column("Departure", width=170, anchor="center")
            self.tree.column("Destination", width=170, anchor="center")
            self.tree.column("Date", width=170, anchor="center")
            self.tree.column("Seat", width=170, anchor="center")

            self.tree.heading("Flight Number", text="Flight Number")
            self.tree.heading("Name", text="Name")
            self.tree.heading("Departure", text="Departure")
            self.tree.heading("Destination", text="Destination")
            self.tree.heading("Date", text="Date")
            self.tree.heading("Seat", text="Seat")
            self.tree.grid(row=0, column=0, pady=(140, 400), padx=250, sticky="nsew")
            self.btn3.grid(row=0, column=0, padx=(0, 250), sticky="e", pady=(50, 0))
            self.btn4.grid(row=0, column=0, padx=(0, 400), sticky="e", pady=(50, 0))

    def put_data(self):
        if self.tree.selection():
            index = int(self.tree.selection()[0])
            reservations = self.tree.item(index, 'values')
            self.edit_page.clear_data()
            self.edit_page.FlightNum.insert(END, reservations[0])
            self.edit_page.name.insert(END, reservations[1])
            self.edit_page.Dep.insert(END, reservations[2])
            self.edit_page.Des.insert(END, reservations[3])
            self.edit_page.date.insert(END, reservations[4])
            self.edit_page.SeatNum.insert(END, reservations[5])
            self.Edit_Page()

    def delete_data(self):
        if self.tree.selection():
            index = int(self.tree.selection()[0])
            selected_reservation = self.tree.item(index, 'values')[0]
            db = sqlite3.connect('flights.db')
            cr = db.cursor()
            cr.execute("DELETE FROM reservations WHERE flight_number=?", (selected_reservation,)
                       )
            db.commit()
            db.close()
            self.edit_page.clear_data()
        self.load_database()

    def search_by_FlightNumber(self,_flightnumber):
        if _flightnumber !='':
            db = sqlite3.connect('flights.db')
            cr = db.cursor()

            search_by_flightnumber = """SELECT flight_number , name ,departure ,destination,date,seat FROM reservations WHERE flight_number LIKE ?"""

            cr.execute(search_by_flightnumber, (_flightnumber + '%',))

            db.commit()
            response = cr.fetchall()
            db.close()
            if response:
                for item in self.tree.get_children():
                    self.tree.delete(item)

                for r in range(len(response)):
                    self.tree.insert(parent='', iid=r, index='end', values=response[r])
            else:
                for item in self.tree.get_children():
                    self.tree.delete(item)

        else:
            self.load_database()

    def book_button(self):
        self.book_page.clear_data()
        self.Book_Func()




















