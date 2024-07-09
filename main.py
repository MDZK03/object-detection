import tkinter as tk
from tkinter import messagebox
import cv2
from image_object_detection import image
from video_detection import video

def option_selected(option):
    if option == "image":
        image()
    elif option == "video":
        video()
    else:
        messagebox.showinfo("Option Selected", "No image or video chosen")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Create the main window
    root = tk.Tk()
    w = 300 # width for the Tk root
    h = 200 # height for the Tk root

    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    root.title("Object Detection Tool")

    # Function to handle option selection
    def choose_option(option):
        option_selected(option)

    # Create and configure buttons for options
    option1_btn = tk.Button(root, text="Image Object Detection", command=lambda: choose_option("image"))
    option1_btn.pack(pady=30)

    option2_btn = tk.Button(root, text="Video Object Detection", command=lambda: choose_option("video"))
    option2_btn.pack(pady=30)

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()