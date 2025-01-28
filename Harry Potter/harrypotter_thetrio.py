import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO

#This function is to fetch character data from the API 
def get_character_data(character_slug):
    url = f"https://api.potterdb.com/v1/characters/{character_slug}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

#This function is to display character details in the Tkinter window
def display_character_details(character_slug):
    # Clear the main page content
    for widget in root.winfo_children():
        widget.destroy()

    #Add the background image
    bg_label = tk.Label(root, image=background_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    character_data = get_character_data(character_slug)

    if character_data:
        #This extracts information from the character data
        character_info = character_data['data']['attributes']
        name = character_info['name']
        image_url = character_info['image']
        blood_status = character_info['blood_status']
        patronus = character_info['patronus']
        house = character_info['house']

        #This is the frame for the character details
        info_frame = tk.Frame(root, bg="#2B2B2B")  
        info_frame.pack(expand=True, pady=30)

        #Thi displays the character information in the window with high contrast white text
        tk.Label(info_frame, text=f"Name: {name}", font=("Arial", 14), bg="#2B2B2B", fg="white").pack(pady=5)
        tk.Label(info_frame, text=f"Blood Status: {blood_status}", font=("Arial", 14), bg="#2B2B2B", fg="white").pack(pady=5)
        tk.Label(info_frame, text=f"Patronus: {patronus}", font=("Arial", 14), bg="#2B2B2B", fg="white").pack(pady=5)
        tk.Label(info_frame, text=f"House: {house}", font=("Arial", 14), bg="#2B2B2B", fg="white").pack(pady=5)

        #Fetch and display the character image
        try:
            img_response = requests.get(image_url)
            img_data = Image.open(BytesIO(img_response.content))
            img_data = img_data.resize((200, 300))  
            img = ImageTk.PhotoImage(img_data)
            image_label = tk.Label(root, image=img, bg="#2B2B2B")
            image_label.image = img  
            image_label.pack(pady=10)
        except:
            messagebox.showerror("Error", "Failed to load image.")

        #Back to home button
        back_button = tk.Button(root, text="Back to Home", command=show_main_page, font=("Harry Potter", 12), bg="#C9A94A", fg="black", relief="solid", bd=0)
        back_button.pack(pady=20)
    else:
        messagebox.showerror("Error", "Failed to retrieve character data.")

#This function creates the character buttons
def show_main_page():
    #This clears the window and display only the character buttons
    for widget in root.winfo_children():
        widget.destroy()

    #Add the background image
    bg_label = tk.Label(root, image=background_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Add first header and second header titles with Harry Potter font
    header_title = tk.Label(root, text="Welcome to the Harry Potter: The Trio", font=("Harry Potter", 26), bg="#0A0A0A", fg="gold")
    header_title.pack(pady=15)

    #Second header title with justified text
    second_header_title = tk.Label(root, text="The trio consisting of Harry Potter, Hermione Granger, and Ron Weasley serves as the central axis of the Harry Potter series. Their unwavering friendship and collective bravery are pivotal to the narrative. Together, they harmoniously balance each other's strengths and weaknesses: Harry’s courageousness and intuition, Hermione’s intellect and resourcefulness, and Ron’s loyalty and strategic acumen. They encounter numerous challenges and adversities, consistently relying on their profound bond and mutual trust to combat the dark forces that threaten the wizarding world.", 
                                   font=("Arial", 14), bg="#0A0A0A", fg="white", wraplength=380, justify="left", anchor="w")
    second_header_title.pack(pady=10)

    #This create buttons for each character with Harry Potter font
    character_buttons_frame = tk.Frame(root, bg="#2B2B2B")  
    character_buttons_frame.pack(expand=True) 

    #Character buttons
    harry_button = tk.Button(character_buttons_frame, text="Harry Potter", command=lambda: display_character_details('harry-potter'), font=("Harry Potter", 13), bd=0, relief="solid", height=2, width=18, bg="#740001", fg="white")  # Gryffindor red
    hermione_button = tk.Button(character_buttons_frame, text="Hermione Granger", command=lambda: display_character_details('hermione-granger'), font=("Harry Potter", 13), bd=0, relief="solid", height=2, width=18, bg="#F1C232", fg="black")  # Hufflepuff yellow
    ron_button = tk.Button(character_buttons_frame, text="Ronald Weasley", command=lambda: display_character_details('ronald-weasley'), font=("Harry Potter", 13), bd=0, relief="solid", height=2, width=18, bg="#4B9F3D", fg="white")  # Slytherin green (to represent Ron's bravery)

    #Pack the buttons with more spacing
    harry_button.grid(row=0, column=0, padx=15, pady=10)
    hermione_button.grid(row=0, column=1, padx=15, pady=10)
    ron_button.grid(row=0, column=2, padx=15, pady=10)

#Tkinter window
root = tk.Tk()
root.geometry("400x600")  

#Background image
background_image = Image.open(r"C:\harrypotter\Harry Potter\hogwarts.jpg")
background_image = background_image.resize((1380, 780))  
background_photo = ImageTk.PhotoImage(background_image)

#Display the main page initially
show_main_page()

#Start the Tkinter event loop
root.mainloop()
