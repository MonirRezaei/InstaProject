
from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen

from PIL import Image,ImageTk
import io

window = Tk()
window.geometry("400x430")
window.maxsize(800 , 800)
window.minsize(200 , 200)
window.title('instagram profile downloader')

def get_image():

    L= instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, my_input.get())
    a = urlopen(profile.get_profile_pic_url())
    data = a.read()
    a.close()
    image = Image.open(io.BytesIO(data))
    pic = ImageTk.PhotoImage(image)
    mlable.config(image=pic)
    mlable.Image = pic
    mlable.pack()

# labels
my_label = Label(window, text='Enter your instagram account')
my_label.pack()

mlable = Label(window)

# buttons
button = Button(window, text='Start Downloading',fg='white',bg='black')
button.pack()
button.config(command=get_image)

# inputs
my_input = Entry(window)
my_input.pack()

window.mainloop()