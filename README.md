✈️ Flight Reservation App

A user-friendly desktop GUI application for booking and managing flight reservations. Built with **Python**, **Tkinter**, and **SQLite**, the app provides a complete workflow from booking a flight to editing and viewing all reservations.

## 📌 Features

### 🏠 Home Page
- Two main options:
  - **Book Flight** – Navigate to the booking form.
  - **View Reservations** – Display all existing bookings.

### 📝 Book Flight Page
- Input fields:
  - Passenger Name
  - Flight Number
  - Departure
  - Destination
  - Date (via Calendar Picker)
  - Seat Number
- Buttons:
  - **Book Flight** – Save the reservation to the database.
  - **Cancel** – Cancel the process and return to the home page.

### 📋 View Reservations Page
- Displays all booked flights in a table format.
- Actions per reservation:
  - **Edit** – Modify any reservation details on a dedicated update page.
  - **Delete** – Remove the selected reservation.
- **Search** – Filter reservations by flight number (useful for large tables).

## 💼 Tech Stack

- **Language**: Python
- **GUI**: Tkinter
- **Database**: SQLite
- **Calendar Widget**: tkcalendar
- **Image Handling**: Pillow (PIL)

---

## 📦 Required Packages

Install the required Python packages using pip:  
pip install babel==2.17.0  
pip install pillow==11.3.0  
pip install pip==25.1.1  
pip install tkcalendar==1.6.1  

or all at once using  
pip install -r requirements.txt


## 🛠️ Building the .exe File

You can package the application as a standalone Windows executable using **PyInstaller**.

### ✅ Step-by-step:

#### 1. Install PyInstaller
pip install pyinstaller

#### 2. Build the Executable
From the root directory of your project, run:  
pyinstaller --onefile --add-data "images:images" main.py

This command tells PyInstaller to:  
Package everything into one .exe file  
Include the images/ folder so image assets (like images/airplane.png) are bundled correctly  

#### 3. Locate the Executable
After the build completes, your executable will be located in the following folder:  
dist/main.exe  

You can now share or run this .exe file on any Windows machine without needing Python installed.


