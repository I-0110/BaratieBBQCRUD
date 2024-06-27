import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to handle saving client information to MySQL database
def save_to_database(name, phone, email):
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='August15,2023!',
            database='client_info'
        )
        
        # Create a cursor object using cursor() method
        cursor = conn.cursor()

        # MySQL query to insert client information into the table
        sql = "INSERT INTO clients (client_name, telephone_number, email) VALUES (%s, %s, %s)"
        values = (name, phone, email)
        
        # Execute the SQL query
        cursor.execute(sql, values)

        # Commit changes to the database
        conn.commit()

        # Close cursor and connection
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Client information saved successfully!")

    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Error saving client information: {error}")

# Function to handle button click event
def submit_form():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    # Validate input (basic validation)
    if name == "" or phone == "" or email == "":
        messagebox.showerror("Error", "Please fill in all fields.")
    else:
        # Call function to save to database
        save_to_database(name, phone, email)

        # Clear input fields
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
        entry_email.delete(0, tk.END)

# Create a Tkinter window
window = tk.Tk()
window.geometry("500x200")
window.title("Client Information")

# Create labels for name, phone, and email
label_name = tk.Label(window, text="Name:", font=("Arial",12))
label_name.place(x=50,y=30)

label_phone = tk.Label(window, text="Phone:", font=("Arial",12))
label_phone.place(x=50,y=60)

label_email = tk.Label(window, text="Email:", font=("Arial",12))
label_email.place(x=50,y=90)

#Create entry field boxes for name, phone, and email

entry_name = tk.Entry(window, width=50)
entry_name.place(x=140,y=30)

entry_phone = tk.Entry(window, width=50)
entry_phone.place(x=140,y=60)

entry_email = tk.Entry(window, width=50)
entry_email.place(x=140,y=90)

# Create a submit button
submit_button = tk.Button(window, text="Submit", font=("Arial",16),command=submit_form)
submit_button.place(x=250,y=130)

# Run the Tkinter event loop
window.mainloop()
