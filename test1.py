import tkinter
import customtkinter
from PIL import Image, ImageTk
import pickle
import json
import numpy as np
from tkinter import messagebox

with open('model1.pickle', 'rb') as f:
    model = pickle.load(f)

with open('columns.json', 'r') as f:
    columns_dict = json.load(f)
columns = columns_dict['data_columns']

def predict():
    location = entry1.get()
    sqft = float(entry2.get())
    bath = int(entry3.get())
    bhk = int(entry4.get())
    
    if not location.isdigit():
        location = location.lower()

    # Get the index of the location
    try:
        index = columns.index(location)
    except ValueError:
        messagebox.showerror("Error", "Location not found")
        return

    # Create the input array for the model
    a = np.zeros(len(columns))
    a[columns.index('total_sqft')] = sqft
    a[columns.index('bath')] = bath
    a[columns.index('bhk')] = bhk
    if index >= 0:
        a[index] = 1

    # Make the prediction
    price = model.predict([a])[0]
    formatted_price = f"{price:.2f} Lakhs" 
    messagebox.showinfo("Prediction", f"Predicted Price: {formatted_price}") 


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app=customtkinter.CTk()
app.geometry("2560x1440")
app.title("ValueVisor.in")


img1 = ImageTk.PhotoImage(Image.open("image2.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1,
                               width=500,
                               height=500)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER) 



l2 = customtkinter.CTkLabel(master=frame, text="Welcome to ValueVisor.in !", font=('Arial', 24, 'bold'))
l2.place(x=95,y=55)

l3 = customtkinter.CTkLabel(master=frame, text="Discover the future value of your dream \n home in Bangalore with just a few clicks!", font=('Arial', 20))
l3.place(x=70,y=105)

entry1= customtkinter.CTkEntry(master=frame, placeholder_text="Enter Location", width=250,height=30,font=('Arial', 14),corner_radius=8)
entry1.place(x=120, y=180)

entry2= customtkinter.CTkEntry(master=frame, placeholder_text="Enter Total Sqft", width=250,font=('Arial', 14),corner_radius=8)
entry2.place(x=120, y=235)

entry3= customtkinter.CTkEntry(master=frame, placeholder_text="Enter No. of Bathroom", width=250,font=('Arial', 14),corner_radius=8)
entry3.place(x=120, y=290)

entry4= customtkinter.CTkEntry(master=frame, placeholder_text="Enter BHK", width=250,font=('Arial', 14),corner_radius=8)
entry4.place(x=120, y=345)

button1 = customtkinter.CTkButton(master=frame, text="Predict", width=250,corner_radius=8,command=predict,font=('Arial', 16))
button1.place(x=120, y=405)
app.mainloop()