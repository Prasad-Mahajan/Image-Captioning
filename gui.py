from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

# Load environment variables
load_dotenv(find_dotenv())

# Image-to-text pipeline
def img2text(file_path):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
    text = image_to_text(file_path)
    return text[0]['generated_text']

# Function to open file dialog and process image
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        # Display the selected image
        img = Image.open(file_path)
        img.thumbnail((300, 300))  # Resize for display
        img = ImageTk.PhotoImage(img)
        img_label.config(image=img)
        img_label.image = img

        # Get and display the caption
        caption = img2text(file_path)
        caption_label.config(text=f"Caption: {caption}")

# Create the GUI window
root = Tk()
root.title("Image to Text")

# GUI layout
img_label = Label(root)
img_label.pack(pady=10)

caption_label = Label(root, text="Caption will appear here", wraplength=400, justify="center")
caption_label.pack(pady=10)

upload_button = Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

# Run the GUI loop
root.mainloop()
