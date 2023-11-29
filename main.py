import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk  
import random

class ZarAtmaOyunu:
    def __init__(self, master):
        self.master = master
        self.master.title("Zar Atma Oyunu")

        
        self.zar_resmi = ImageTk.PhotoImage(Image.open("zar_resmi.png"))  #
        self.zar_etiket = Label(self.master, image=self.zar_resmi)
        self.zar_etiket.pack(pady=20)

       
        self.zar_atma_dugme = Button(self.master, text="Zar At", command=self.zar_at)
        self.zar_atma_dugme.pack()

    def zar_at(self):
        donme = random.randint(1,32)
        for i in range(donme):
            zar_sayisi = random.randint(1, 6)
            zar_resmi_adi = f"zar{zar_sayisi}.png"
            self.zar_resmi = ImageTk.PhotoImage(Image.open(zar_resmi_adi))
            self.zar_etiket.configure(image=self.zar_resmi)
            self.master.update()
            self.master.after(120)

        
       
        self.zar_resmi = ImageTk.PhotoImage(Image.open(zar_resmi_adi))

        
        self.zar_etiket.configure(image=self.zar_resmi)


root = tk.Tk()


zar_oyunu = ZarAtmaOyunu(root)


root.mainloop()
