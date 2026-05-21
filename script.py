import tkinter as tk
import time

def update_clock():
    hora = time.strftime("%H")
    minuto = time.strftime("%M")
    segundo = time.strftime("%S")
    ceas.config(text=f"{hora}:{minuto}:{segundo}")
    ceas.after(1000, update_clock)

app = tk.Tk() #cria a janela
app.title("Time") #titulo da janela

ceas = tk.Label(app, text="", font=("Helvetica", 48), fg='#978F66', bg="#622B14") #cria um label para exibir a hora
ceas.pack()

update_clock()
app.mainloop()