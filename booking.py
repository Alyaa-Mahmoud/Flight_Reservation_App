
from tkinter import *
from tkcalendar import *
import sqlite3

class BookingPage(Frame):
    def __init__(self, master,Home_Func,View_Res_Func):
        Frame.__init__(self, master)
        self.Home_Func = Home_Func
        self.View_Res_Func = View_Res_Func

        self.lbl1 = Label(self, text="Book a Flight", padx=10, pady=10,bg="#DEEBF7", fg="#00264D",font=('Arial', 25, 'bold'))
        self.lbl1.place(x = 450 , y = 70)

        self.frame1 = Frame(self, bg="white", width=500, height=500, pady=25, padx=30)
        self.frame1.grid(row=0, column=1, padx=460, pady=(140,400),sticky="nsew")
        self.frame1.grid_columnconfigure(0, weight=1)

        self.btn1 = Button(self.frame1 , text="Book Flight",width=10, height=2, relief="flat", bg="#427AA1", fg="white",
                      font=('Arial', 10, 'bold'),command=lambda:self.combined_function())

        self.btn2 = Button(self.frame1 , text="Cancel",width=10, height=2, relief="flat", bg="#DEEBF7", fg="black",
                      font=('Arial', 10, 'bold'),command=lambda:self.cancel_button())

        self.fullname = Label(self.frame1,text="Full Name",bg="white", fg="black",font=('Arial', 11, 'bold'))
        self.flightnumber = Label(self.frame1,text="Flight Number",bg="white", fg="black",font=('Arial', 11, 'bold'))
        self.Departure = Label(self.frame1,text="Departure",bg="white", fg="black",font=('Arial', 11, 'bold'))
        self.Destination = Label(self.frame1,text="Destination",bg="white", fg="black",font=('Arial', 11, 'bold'))
        self.Date = Label(self.frame1,text="Date",bg="white", fg="black",font=('Arial', 12, 'bold'))
        self.Seatnumber = Label(self.frame1,text="Seat Number",bg="white", fg="black",font=('Arial', 11, 'bold'))

        self.name = Entry(self.frame1,font=('Arial', 12),fg='gray',width=60,highlightcolor="black",highlightthickness=1)
        self.name.grid(row=1, column=0, pady=(10,20),sticky="ew",ipady=4)
        self.FlightNum = Entry(self.frame1, font=('Arial', 12),fg='gray',width=60,highlightcolor="black",highlightthickness=1)
        self.FlightNum.grid(row=4, column=0, pady=(10,20), sticky="ew",ipady=4)
        self.Dep = Entry(self.frame1, font=('Arial', 12), fg='gray',width=30,highlightcolor="black",highlightthickness=1)
        self.Dep.grid(row=7, column=0, pady=(10,20),sticky="w",ipady=4)
        self.Des = Entry(self.frame1, font=('Arial', 12),fg='gray', width=30,highlightcolor="black",highlightthickness=1)
        self.Des.grid(row=7, column=0, pady=(10,20),padx=(300,0),sticky="e",ipady=4)
        self.date = DateEntry(self.frame1,selectmode='day',width=42,ipady=4)
        self.date.delete(0, END)
        self.date.grid(row=10, column=0, pady=(10,20), sticky="w",ipady=4)
        self.SeatNum = Entry(self.frame1, font=('Arial', 12),fg='gray', width=30,highlightcolor="black",highlightthickness=1)
        self.SeatNum.grid(row=10, column=0, pady=(10,20),padx=(300,0), sticky="e",ipady=4)

        self.fullname.grid(row=0, column=0,sticky="w")
        self.flightnumber.grid(row=3, column=0,sticky="w")
        self.Departure.grid(row=6, column=0,sticky="w")
        self.Destination.grid(row=6, column=0,padx=(120,0))
        self.Date.grid(row=9, column=0 ,sticky="w")
        self.Seatnumber.grid(row=9, column=0,padx=(120,0))

        self.name_error = Label(self.frame1, text="*Required", bg="white", fg="red", font=('Arial', 11, 'bold'))
        self.flightnumber_error = Label(self.frame1, text="*Required", bg="white", fg="red", font=('Arial', 11, 'bold'))
        self.Departure_error = Label(self.frame1, text="*Required", bg="white", fg="red", font=('Arial', 11, 'bold'))
        self.Destination_error = Label(self.frame1, text="*Required", bg="white", fg="red", font=('Arial', 11, 'bold'))
        self.Date_error = Label(self.frame1, text="*Required", bg="white", fg="red", font=('Arial', 11, 'bold'))
        self.Seatnumber_error = Label(self.frame1, text="*Required", bg="white", fg="red", font=('Arial', 11, 'bold'))

        for entry in (self.name, self.FlightNum, self.Dep, self.Des ,self.SeatNum):
            entry.bind("<KeyRelease>", lambda e: self.clear_label())

        self.date.bind("<KeyRelease>", lambda e: self.Check_EmptyField())
        self.date.bind("<FocusIn>", lambda e: self.clear_label())
        self.date.bind("<FocusOut>", lambda e: self.clear_label())

        self.btn1.grid(row=12, column=0,pady=(20,0),sticky="e")
        self.btn2.grid(row=12, column=0 , padx=(0,100),pady=(20,0),sticky="e")

        self.name.insert(0, 'Enter Your Name')
        self.name.bind('<FocusIn>', lambda e: self.name_focus_in())
        self.name.bind('<FocusOut>', lambda e: self.on_name_focus_out())

        self.FlightNum.insert(0, 'e.g. 123')
        self.FlightNum.bind('<FocusIn>', lambda e: self.FlightNum_focus_in())
        self.FlightNum.bind('<FocusOut>', lambda e: self.on_FlightNum_focus_out())

        self.Dep.insert(0, 'e.g. Egypt')
        self.Dep.bind('<FocusIn>', lambda e: self.Dep_focus_in())
        self.Dep.bind('<FocusOut>', lambda e: self.on_Dep_focus_out())

        self.Des.insert(0, 'e.g. London')
        self.Des.bind('<FocusIn>', lambda e: self.Des_focus_in())
        self.Des.bind('<FocusOut>', lambda e: self.on_Des_focus_out())

        self.SeatNum.insert(0, 'e.g. 12A')
        self.SeatNum.bind('<FocusIn>', lambda e: self.SeatNum_focus_in())
        self.SeatNum.bind('<FocusOut>', lambda e: self.on_SeatNum_focus_out())

    def name_focus_in(self):
        if self.name.get() == 'Enter Your Name':
            self.name.delete(0, END)
            self.name.config(fg="black")

    def name_focus_out(self):
        if self.name.get().strip() == '':
            self.name.insert(0, 'Enter Your Name')
            self.name.config(fg="gray")

    def on_name_focus_out(self):
        self.name_focus_out()
        self.Check_EmptyField()

    def FlightNum_focus_in(self):
        if self.FlightNum.get() == 'e.g. 123':
            self.FlightNum.delete(0, END)
            self.FlightNum.config(fg="black")

    def FlightNum_focus_out(self):
        if self.FlightNum.get().strip() == '':
            self.FlightNum.insert(0, 'e.g. 123')
            self.FlightNum.config(fg="gray")

    def on_FlightNum_focus_out(self):
        self.FlightNum_focus_out()
        self.Check_EmptyField()

    def Dep_focus_in(self):
        if self.Dep.get() == 'e.g. Egypt':
            self.Dep.delete(0, END)
            self.Dep.config(fg="black")

    def Dep_focus_out(self):
        if self.Dep.get().strip() == '':
            self.Dep.insert(0, 'e.g. Egypt')
            self.Dep.config(fg="gray")

    def on_Dep_focus_out(self):
        self.Dep_focus_out()
        self.Check_EmptyField()

    def Des_focus_in(self):
        if self.Des.get() == 'e.g. London':
            self.Des.delete(0, END)
            self.Des.config(fg="black")

    def Des_focus_out(self):
        if self.Des.get().strip() == '':
            self.Des.insert(0, 'e.g. London')
            self.Des.config(fg="gray")

    def on_Des_focus_out(self):
        self.Des_focus_out()
        self.Check_EmptyField()

    def SeatNum_focus_in(self):
        if self.SeatNum.get() == 'e.g. 12A':
            self.SeatNum.delete(0, END)
            self.SeatNum.config(fg="black")

    def SeatNum_focus_out(self):
        if self.SeatNum.get().strip() == '':
            self.SeatNum.insert(0, 'e.g. 12A')
            self.SeatNum.config(fg="gray")

    def on_SeatNum_focus_out(self):
        self.SeatNum_focus_out()
        self.Check_EmptyField()

    def Check_EmptyField(self):
        if not self.name.get().strip() or self.name.get() == 'Enter Your Name':
            self.name_error.grid(row=2, column=0, pady=(0, 10), sticky="w")
            self.name.grid_configure(pady=10)
        if not self.FlightNum.get().strip() or self.FlightNum.get() == 'e.g. 123':
            self.flightnumber_error.grid(row=5, column=0, pady=(0, 10), sticky="w")
            self.FlightNum.grid_configure(pady=10)
        if not self.Dep.get().strip() or self.Dep.get() == 'e.g. Egypt':
            self.Departure_error.grid(row=8, column=0, pady=(0, 10), sticky="w")
            self.Dep.grid_configure(pady=10)
        if not self.Des.get().strip() or self.Des.get() == 'e.g. London':
            self.Destination_error.grid(row=8, column=0, pady=(0, 10), padx=(0, 200), sticky="e")
            self.Des.grid_configure(pady=10)
        if not self.date.get():
            self.Date_error.grid(row=11, column=0, pady=(0, 10), sticky="w")
            self.date.grid_configure(pady=10)
        if not self.SeatNum.get().strip() or self.SeatNum.get() == 'e.g. 12A':
            self.Seatnumber_error.grid(row=11, column=0, pady=(0, 10), padx=(0, 200), sticky="e")
            self.SeatNum.grid_configure(pady=10)

    def clear_label(self):
        if self.name.get().strip():
            self.name_error.grid_remove()
        if self.FlightNum.get().strip():
            self.flightnumber_error.grid_remove()
        if self.Dep.get().strip():
            self.Departure_error.grid_remove()
        if self.Des.get().strip():
            self.Destination_error.grid_remove()
        if self.date.get():
            self.Date_error.grid_remove()
        if self.SeatNum.get().strip():
            self.Seatnumber_error.grid_remove()

    def clear_data(self):
        self.FlightNum.delete(0, END)
        self.FlightNum.insert(0, 'e.g. 123')
        self.name.delete(0, END)
        self.name.focus_set()
        self.Dep.delete(0, END)
        self.Dep.insert(0, 'e.g. Egypt')
        self.Des.delete(0, END)
        self.Des.insert(0, 'e.g. London')
        self.date.delete(0, END)
        self.SeatNum.delete(0, END)
        self.SeatNum.insert(0, 'e.g. 12A')
        self.FlightNum.config(fg="gray")
        self.name.config(fg="black")
        self.Dep.config(fg="gray")
        self.Des.config(fg="gray")
        self.SeatNum.config(fg="gray")
        self.name_error.grid_remove()
        self.flightnumber_error.grid_remove()
        self.Departure_error.grid_remove()
        self.Destination_error.grid_remove()
        self.Date_error.grid_remove()
        self.Seatnumber_error.grid_remove()
            


    def add_database(self,_flightnumber, _name, _departure, _destination, _date, _seatnumber):
        if (
                self.name.get().strip() and self.name.get() != 'Enter Your Name' and
                self.FlightNum.get().strip() and self.FlightNum.get() != 'e.g. 123' and
                self.Dep.get().strip() and self.Dep.get() != 'e.g. Egypt' and
                self.Des.get().strip() and self.Des.get() != 'e.g. London' and
                self.date.get() and
                self.SeatNum.get().strip() and self.SeatNum.get() != 'e.g. 12A'
            ):
            db = sqlite3.connect('flights.db')
            cr = db.cursor()
            cr.execute("INSERT INTO reservations VALUES (?, ?, ?, ?, ?, ?)"
                       , (_flightnumber, _name, _departure, _destination, _date, _seatnumber))
            db.commit()
            cr.execute(f"""
            SELECT * FROM reservations 
            """)
            db.commit()
            db.close()
            self.View_Res_Func()
            self.clear_data()

    def combined_function(self):
        self.Check_EmptyField()
        self.add_database(_flightnumber=self.FlightNum.get(),_name=self.name.get(),_departure=self.Dep.get(),_destination=self.Des.get(),_date=self.date.get(),_seatnumber=self.SeatNum.get())

    def cancel_button(self):
        self.clear_data()
        self.Home_Func()


        








