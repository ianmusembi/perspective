# Photomanipulator
# Author : Ian Musembi


# filebrowser.py

'''
Contains function that enables user to select the image to be drawn
'''

from tkinter import filedialog


def selectImage () -> str :

    filename = filedialog.askopenfilename(initialdir="", title= "Choose an image",
                                                filetypes=(("png files", "*.png"), ("jpg files", "*.jpg"),
                                                        ("jpeg files", "*.jpeg") ), 
                                                multiple= False)

    return filename


if __name__ == "__main__":
    print(selectImage())