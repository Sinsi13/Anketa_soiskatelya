import tkinter as tk
from tkinter import ttk #модуль с  улучшеными виждетами
from tkinter import messagebox #модуль сообщений

def submit_form():
    "Функция сбора данных из формы"
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    job = combo_job.get()
    is_subscribed = "Да" if subscribe_var.get() else "Нет"

    if name and age:
        summary = (f"Имя: {name}\nВозраст: {age}\nПол: {gender}\n"
                   f"Профессия: {job}\nПодписка на новости: {is_subscribed}")
        messagebox.showinfo("Анкета получена", summary)
    else:
        messagebox.showwarning("Внимание", "Пожалуйста, заполните имя и возраст!")
    
#создаем окно
root = tk.Tk()
root.title("Анкета пользователя v1.0")
root.geometry("400x450")

#общий контейнер с отступами
main_frame = tk.Frame(root, padx = 20, pady = 20)
main_frame.pack(expand = True, fill = "both")

#секция 1 личные данные
personal_info = tk.LabelFrame(main_frame, text = "Личная информация", padx = 10, pady = 10)
personal_info.pack(fill = "x", pady = 10)

tk.Label(personal_info, text = "ФИО: ").grid(row = 0, column = 0, sticky = "w")
entry_name = tk.Entry(personal_info)
entry_name.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = "ew")

tk.Label(personal_info, text = "Возраст: ").grid(row = 1, column = 0, sticky = "w")
entry_age = tk.Entry(personal_info, width = 5)
entry_age.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = "w")

#секция 2 выбор
gender_frame = tk.LabelFrame(main_frame, text = "Пол", padx = 10, pady = 10)
gender_frame.pack(fill = "x", pady = 10)
gender_var = tk.StringVar(value = "Мужской")
tk.Radiobutton(gender_frame, text = "Мужской", variable = gender_var, value = "Мужской").pack(side = "left")
tk.Radiobutton(gender_frame, text = "Женский", variable = gender_var, value = "Женский").pack(side = "left")

#Секция 3 дополнительно
extra_frame = tk.Frame(main_frame)
extra_frame.pack(fill = "x", pady = 10)
tk.Label(extra_frame, text = "Профессия:").pack(side = "left")
combo_job = ttk.Combobox(extra_frame, values = ["Программист", "Дизайнер", "Менеджер", "Студент"])
combo_job.pack(side = "left", padx = 10)
combo_job.current(0)

#Секция 4 ЧекБокс
subscribe_var = tk.BooleanVar()
check_sub = tk.Checkbutton(main_frame, text = "Подписаться на рассылку", variable = subscribe_var)
check_sub.pack(pady = 10)

#кнопка отправки
btn_submit = tk.Button(main_frame, text = "Отправить анкету", bg = "#4CAF50", fg = "white", font = ("Arial", 12, "bold"), command = submit_form)
btn_submit.pack(fill= "x", pady = 20)

root.mainloop()
