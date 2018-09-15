# 2018.09.15
# by Serg Root
# gmail: serg.kuz375@gmail.com
# VK: vk.com/serg3911

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

file_name = NONE

def new_file(): # Новый файл
    global file_name
    file_name = "Без названия"
    text.delete('1.0', END)

def save_as():  # Сохранить файл
    out = asksaveasfile(mode='w', defaultextension='.text')  # Формат
    data = text.get('1.0', END)

    try:  # Обработчик ошибок
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Упс!", "Нельзя сохранить файл!")

def open_file():  # Открыть файл
    global file_name
    inp = asksaveasfile(mode='r')

    if inp is None:
        return
        file_name = inp.name

    data = inp.read()
    text.delete('1.0', END)
    assert isinstance(data, object)
    text.insert('1.0', data)


root = Tk()  # Системные настройки программы
root.title("Заметки")  # Надпись
root.geometry("700x700")  # Размер окна

text = Text(root, width=700, height=700)  # Текстовое поле
text.pack()

menu_bar = Menu(root)  # Меню
file_menu = Menu(menu_bar)

# Настройки меню
menu_bar.add_cascade(label="Файл", menu=file_menu) # Кнопочка под названием "Файл"
file_menu.add_command(label="Новый", command=new_file) # Кнопочка под названием "Новый"
file_menu.add_command(label="Открыть", command=open_file) # Кнопочка под названием "Открыть"
file_menu.add_command(label="Сохранить", command=save_as) # Кнопочка под названием "Сохранить"

root.config(menu=menu_bar)  # Чтобы менюшка работала :)
root.mainloop()
