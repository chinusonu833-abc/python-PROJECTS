
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk


def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries", "Aries.jpg"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus", "images/taurus.jpg"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini", "images/gemini.jpg"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer", "cancer.jpg"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo", "leo.jpg"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo", "images/virgo.jpg"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra", "images/libra.jpg"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio", "images/scorpio.jpg"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius", "images/sagittarius.jpg"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn", "images/capricorn.jpg"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius", "images/aquarius.jpg"
    else:
        return "Pisces", "images/pisces.jpg"


def find_zodiac():
    try:
        dob = entry.get()  # Format: DD-MM-YYYY
        date = datetime.strptime(dob, "%d-%m-%Y")
        day = date.day
        month = date.month

        sign, image_path = get_zodiac_sign(day, month)

        # Show zodiac name
        result_label.config(text=f"✨ {sign}")

        # Load and show image
        img = Image.open(image_path)
        img = img.resize((250, 250))
        photo = ImageTk.PhotoImage(img)

        image_label.config(image=photo)
        image_label.image = photo  # Keep reference

    except ValueError:
        messagebox.showerror("Invalid Input", "Enter date in DD-MM-YYYY format.")
    except FileNotFoundError:
        messagebox.showerror("Image Not Found", "Check if the image exists in the images folder.")


# Main Window
root = tk.Tk()
root.title("Zodiac Sign Finder")
root.geometry("500x600")
root.configure(bg="#203a43")

# Title
title = tk.Label(
    root,
    text="🔮 Zodiac Sign Finder",
    font=("Arial", 24, "bold"),
    fg="white",
    bg="#203a43"
)
title.pack(pady=20)

# Input Label
label = tk.Label(
    root,
    text="Enter Date of Birth (DD-MM-YYYY)",
    font=("Arial", 14),
    fg="white",
    bg="#203a43"
)
label.pack()

# Entry Box
entry = tk.Entry(root, font=("Arial", 16), justify="center")
entry.pack(pady=10)

# Button
button = tk.Button(
    root,
    text="Find My Zodiac Sign",
    font=("Arial", 14, "bold"),
    bg="gold",
    fg="black",
    command=find_zodiac
)
button.pack(pady=20)

# Result Label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 24, "bold"),
    fg="gold",
    bg="#203a43"
)
result_label.pack(pady=10)

# Image Label
image_label = tk.Label(root, bg="#203a43")
image_label.pack(pady=10)

# Run Application
root.mainloop()