import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x580")
app.title("Shifts creator")


#txt = "The best things in life are free!"
#if "free" in txt:
# print("Yes, 'free' is present.")

def button_callback():
    val = " "
    val.append((optionmenu_1.get()) + (combobox_1.get()))

    print(val)


def button_callback2():
    print("Worked")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1,text="Shifts Creator", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)






#entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
#entry_1.pack(pady=12, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Alyona", "Alex", "Ofir"])
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("Name")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Sunday morning", "Monday morning", "Tuesday morning","Sunday night", "Monday night", "Tuesday night"])
combobox_1.pack(pady=12, padx=10)
optionmenu_1.set("Name")

button_1 = customtkinter.CTkButton(master=frame_1,text="save", command=button_callback)
button_1.pack(pady=12, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1,text="finished", command=button_callback2)
button_2.pack(pady=12, padx=10)




app.mainloop()
