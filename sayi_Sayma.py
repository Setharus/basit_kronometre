import tkinter as tk
import time

def say():
    for i in range(101):
        etiket.config(text=i)
        pencere.update()
        time.sleep(1)

pencere = tk.Tk()
pencere.title("Sayma Programı")
pencere.geometry("300x300")  # Pencere boyutu 300x300 olarak ayarlandı

etiket = tk.Label(pencere, font=("Helvetica", 48))
etiket.pack(pady=20)

basla_butonu = tk.Button(pencere, text="Başla", command=say)
basla_butonu.pack(pady=10)

pencere.mainloop()
