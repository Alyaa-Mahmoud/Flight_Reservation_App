import reservations
from reservations import Reservations
from tkinter import *
from tkcalendar import *
import sqlite3

class EditPage(Frame):
    def __init__(self, master,View_Res_Func,tree=None):
        Frame.__init__(self, master)
        self.View_Res_Func = View_Res_Func
        self.tree = tree

        lbl1 = Label(self, text="Edit Reservation", padx=10, pady=10,bg="#DEEBF7", fg="#00264D",font=('Arial', 25, 'bold'))
        lbl1.place(x = 450 , y = 70)

        frame1 = Frame(self, bg="white", width=500, height=500, pady=25, padx=30)
        frame1.grid(row=0, column=1, padx=460, pady=(140,400),sticky="nsew")
        frame1.grid_columnconfigure(0, weight=1)

        btn1 = Button(frame1 , text="Update Reservation",width=16, height=2, relief="flat", bg="#427AA1", fg="white",
                      font=('Arial', 10, 'bold'),command=lambda:self.combined_function())

        btn2 = Button(frame1 , text="Cancel",width=10, height=2, relief="flat", bg="#DEEBF7", fg="black",
                      font=('Arial', 10, 'bold'),command=lambda:self.View_Res_Func())

        fullname = Label(frame1,text="Full Name",bg="white", fg="black",font=('Arial', 11, 'bold'))
        flightnumber = Label(frame1,text="Flight Number",bg="white", fg="black",font=('Arial', 11, 'bold'))
        Departure = Label(frame1,text="Departure",bg="white", fg="black",font=('Arial', 11, 'bold'))
        Destination = Label(frame1,text="Destination",bg="white", fg="black",font=('Arial', 11, 'bold'))
        Date = Label(frame1,text="Date",bg="white", fg="black",font=('Arial', 12, 'bold'))
        Seatnumber = Label(frame1,text="Seat Number",bg="white", fg="black",font=('Arial', 11, 'bold'))

        self.name = Entry(frame1,font=('Arial', 12),width=60,highlightcolor="black",highlightthickness=1)
        self.name.grid(row=1, column=0, pady=(10,20),sticky="ew",ipady=4)
        self.FlightNum = Entry(frame1, font=('Arial', 12),width=60,highlightcolor="black",highlightthickness=1)
        self.FlightNum.grid(row=4, column=0, pady=(10,20), sticky="ew",ipady=4)
        self.Dep = Entry(frame1, font=('Arial', 12), width=30,highlightcolor="black",highlightthickness=1)
        self.Dep.grid(row=7, column=0, pady=(10,20),sticky="w",ipady=4)
        self.Des = Entry(frame1, font=('Arial', 12), width=30,highlightcolor="black",highlightthickness=1)
        self.Des.grid(row=7, column=0, pady=(10,20),padx=(300,0),sticky="e",ipady=4)
        self.date = DateEntry(frame1,selectmode='day',width=42,ipady=4,)
        self.date.grid(row=10, column=0, pady=(10,20), sticky="w",ipady=4)
        self.date.delete(0, END)
        self.SeatNum = Entry(frame1, font=('Arial', 12), width=30,highlightcolor="black",highlightthickness=1)
        self.SeatNum.grid(row=10, column=0, pady=(10,20),padx=(300,0), sticky="e",ipady=4)

        fullname.grid(row=0, column=0,sticky="w")
        flightnumber.grid(row=3, column=0,sticky="w")
        Departure.grid(row=6, column=0,sticky="w")
        Destination.grid(row=6, column=0,padx=(120,0))
        Date.grid(row=9, column=0 ,sticky="w")
        Seatnumber.grid(row=9, column=0,padx=(120,0))

        btn1.grid(row=12, column=0,pady=(20,0),sticky="e")
        btn2.grid(row=12, column=0 , padx=(0,150),pady=(20,0),sticky="e")

    def clear_data(self):
        self.FlightNum.delete(0, END)
        self.name.delete(0, END)
        self.Dep.delete(0, END)
        self.Des.delete(0, END)
        self.date.delete(0, END)
        self.SeatNum.delete(0, END)

    def update_data(self, _flightnumber, _name, _departure, _destination, _date, _seatnumber):
        if self.tree.selection():
            index = int(self.tree.selection()[0])
            selected_data = self.tree.item(index, 'values')[0]
            db = sqlite3.connect('flights.db')
            cr = db.cursor()
            cr.execute("""
                       UPDATE reservations
                       SET flight_number = ?,
                           name          = ?,
                           departure     = ?,
                           destination   = ?,
                           date          = ?,
                           seat          = ?
                       WHERE flight_number = ?
                       """,
                       (_flightnumber, _name, _departure, _destination, _date, _seatnumber, selected_data))

            db.commit()
            if _flightnumber != selected_data:
                cr.execute("""UPDATE reservations
                              SET flight_number = ? WHERE flight_number = ?""", (_flightnumber, selected_data))
                db.commit()

            db.close()
            self.clear_data()

    def combined_function(self):
        self.update_data(_flightnumber=self.FlightNum.get(),_name=self.name.get(),_departure=self.Dep.get(),_destination=self.Des.get(),_date=self.date.get(),_seatnumber=self.SeatNum.get())
        self.View_Res_Func()




