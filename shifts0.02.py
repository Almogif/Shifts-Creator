import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x580")
app.title("Shifts creator")

val = ""
alyona = ""
alex = ""
ofir = ""
yair = ""
almog = ""
pavel = ""
ran = ""
sahar = ""
shifts = " "


def button_callback():
    global val
    val = (" " + val + (optionmenu_1.get()) + " " + (combobox_1.get()) + " ")
    print(val)
    label_2 = customtkinter.CTkLabel(master=frame_1,
                                     text=" " + (optionmenu_1.get()) + " can not work on " + (combobox_1.get()) + " ")
    label_2.pack(pady=1, padx=1)


def button_callback2():
    global val
    global alyona
    global alex
    global ofir
    global almog
    global yair
    global pavel
    global ran
    global sahar

    global shifts
    # Alyona check
    if "Alyona Sun-Morning" in val:
        alyona = alyona + "ABCD"
    if "Alyona Mon-Morning" in val:
        alyona = alyona + "ABCDG"
    if "Alyona Tue-Morning" in val:
        alyona = alyona + "ABGI"
    if "Alyona Wed-Morning" in val:
        alyona = alyona + "BEFI"
    if "Alyona Thu-Morning" in val:
        alyona = alyona + "EFH"
    if "Alyona Fri-Morning " in val:
        alyona = alyona + "EFH"
    if "Alyona Sun-Night" in val:
        alyona = alyona + "EFHI"
    if "Alyona Mon-Night" in val:
        alyona = alyona + "EFH"
    if "Alyona Tue-Night" in val:
        alyona = alyona + "CDH"
    if "Alyona Wed-Night" in val:
        alyona = alyona + "ACDG"
    if "Alyona Thu-Night" in val:
        alyona = alyona + "ABDGI"
    if "Alyona Sat-Night " in val:
        alyona = alyona + "CGI"
    # alex cheack
    if "alex Sun-Morning" in val:
        alex = alex + "ABCD"
    if "alex Mon-Morning" in val:
        alex = alex + "ABCDG"
    if "alex Tue-Morning" in val:
        alex = alex + "ABGI"
    if "alex Wed-Morning" in val:
        alex = alex + "BEFI"
    if "alex Thu-Morning" in val:
        alex = alex + "EFH"
    if "alex Fri-Morning " in val:
        alex = alex + "EFH"
    if "alex Sun-Night" in val:
        alex = alex + "EFHI"
    if "alex Mon-Night" in val:
        alex = alex + "EFH"
    if "alex Tue-Night" in val:
        alex = alex + "CDH"
    if "alex Wed-Night" in val:
        alex = alex + "ACDG"
    if "alex Thu-Night" in val:
        alex = alex + "ABDGI"
    if "alex Sat-Night " in val:
        alex = alex + "CGI"
    # ofir check
    if "ofir Sun-Morning" in val:
        ofir = ofir + "ABCD"
    if "ofir Mon-Morning" in val:
        ofir = ofir + "ABCDG"
    if "ofir Tue-Morning" in val:
        ofir = ofir + "ABGI"
    if "ofir Wed-Morning" in val:
        ofir = ofir + "BEFI"
    if "ofir Thu-Morning" in val:
        ofir = ofir + "EFH"
    if "ofir Fri-Morning " in val:
        ofir = ofir + "EFH"
    if "ofir Sun-Night" in val:
        ofir = ofir + "EFHI"
    if "ofir Mon-Night" in val:
        ofir = ofir + "EFH"
    if "ofir Tue-Night" in val:
        ofir = ofir + "CDH"
    if "ofir Wed-Night" in val:
        ofir = ofir + "ACDG"
    if "ofir Thu-Night" in val:
        ofir = ofir + "ABDGI"
    if "ofir Sat-Night " in val:
        ofir = ofir + "CGI"
    # yair check
    if "yair Sun-Morning" in val:
        yair = yair + "ABCD"
    if "yair Mon-Morning" in val:
        yair = yair + "ABCDG"
    if "yair Tue-Morning" in val:
        yair = yair + "ABGI"
    if "yair Wed-Morning" in val:
        yair = yair + "BEFI"
    if "yair Thu-Morning" in val:
        yair = yair + "EFH"
    if "yair Fri-Morning " in val:
        yair = yair + "EFH"
    if "yair Sun-Night" in val:
        yair = yair + "EFHI"
    if "yair Mon-Night" in val:
        yair = yair + "EFH"
    if "yair Tue-Night" in val:
        yair = yair + "CDH"
    if "yair Wed-Night" in val:
        yair = yair + "ACDG"
    if "yair Thu-Night" in val:
        yair = yair + "ABDGI"
    if "yair Sat-Night " in val:
        yair = yair + "CGI"
    # pavel check
    if "pavel Sun-Morning" in val:
        pavel = pavel + "ABCD"
    if "pavel Mon-Morning" in val:
        pavel = pavel + "ABCDG"
    if "pavel Tue-Morning" in val:
        pavel = pavel + "ABGI"
    if "pavel Wed-Morning" in val:
        pavel = pavel + "BEFI"
    if "pavel Thu-Morning" in val:
        pavel = pavel + "EFH"
    if "pavel Fri-Morning " in val:
        pavel = pavel + "EFH"
    if "pavel Sun-Night" in val:
        pavel = pavel + "EFHI"
    if "pavel Mon-Night" in val:
        pavel = pavel + "EFH"
    if "pavel Tue-Night" in val:
        pavel = pavel + "CDH"
    if "pavel Wed-Night" in val:
        pavel = pavel + "ACDG"
    if "pavel Thu-Night" in val:
        pavel = pavel + "ABDGI"
    if "pavel Sat-Night " in val:
        pavel = pavel + "CGI"
        # almog check
    if "almog Sun-Morning" in val:
        almog = almog + "ABCD"
    if "almog Mon-Morning" in val:
        almog = almog + "ABCDG"
    if "almog Tue-Morning" in val:
        almog = almog + "ABGI"
    if "almog Wed-Morning" in val:
        almog = almog + "BEFI"
    if "almog Thu-Morning" in val:
        almog = almog + "EFH"
    if "almog Fri-Morning " in val:
        almog = almog + "EFH"
    if "almog Sun-Night" in val:
        almog = almog + "EFHI"
    if "almog Mon-Night" in val:
        almog = almog + "EFH"
    if "almog Tue-Night" in val:
        almog = almog + "CDH"
    if "almog Wed-Night" in val:
        almog = almog + "ACDG"
    if "almog Thu-Night" in val:
        almog = almog + "ABDGI"
    if "almog Sat-Night " in val:
        almog = almog + "CGI"
        # ran check
    if "ran Sun-Morning" in val:
        ran = ran + "ABCD"
    if "ran Mon-Morning" in val:
        ran = ran + "ABCDG"
    if "ran Tue-Morning" in val:
        ran = ran + "ABGI"
    if "ran Wed-Morning" in val:
        ran = ran + "BEFI"
    if "ran Thu-Morning" in val:
        ran = ran + "EFH"
    if "ran Fri-Morning " in val:
        ran = ran + "EFH"
    if "ran Sun-Night" in val:
        ran = ran + "EFHI"
    if "ran Mon-Night" in val:
        ran = ran + "EFH"
    if "ran Tue-Night" in val:
        ran = ran + "CDH"
    if "ran Wed-Night" in val:
        ran = ran + "ACDG"
    if "ran Thu-Night" in val:
        ran = ran + "ABDGI"
    if "ran Sat-Night " in val:
        ran = ran + "CGI"
        # sahar check
    if "sahar Sun-Morning" in val:
        sahar = sahar + "ABCD"
    if "sahar Mon-Morning" in val:
        sahar = sahar + "ABCDG"
    if "sahar Tue-Morning" in val:
        sahar = sahar + "ABGI"
    if "sahar Wed-Morning" in val:
        sahar = sahar + "BEFI"
    if "sahar Thu-Morning" in val:
        sahar = sahar + "EFH"
    if "sahar Fri-Morning " in val:
        sahar = sahar + "EFH"
    if "sahar Sun-Night" in val:
        sahar = sahar + "EFHI"
    if "sahar Mon-Night" in val:
        sahar = sahar + "EFH"
    if "sahar Tue-Night" in val:
        sahar = sahar + "CDH"
    if "sahar Wed-Night" in val:
        sahar = sahar + "ACDG"
    if "sahar Thu-Night" in val:
        sahar = sahar + "ABDGI"
    if "sahar Sat-Night " in val:
        sahar = sahar + "CGI"

        print("Sta-Night")
    if (("A" in alyona) and ("B" in alyona) and ("C" in alyona) and ("D" in alyona) and ("E" in alyona) and ("F" in alyona) and (
            "G" in alyona) and ("H" in alyona) and (not "I" in alyona)):
        print("alyona must work I")
        shifts = shifts + "AlyonaI"
    elif (("A" in alyona) and ("B" in alyona) and ("C" in alyona) and ("D" in alyona) and ("E" in alyona) and ("F" in alyona) and (
            "G" in alyona) and ("I" in alyona) and (not "H" in alyona)):
        print("alyona must work H")
        shifts = shifts + "AlyonaH"
    elif (("A" in alyona) and ("B" in alyona) and ("C" in alyona) and ("D" in alyona) and ("E" in alyona) and ("F" in alyona) and (
            "H" in alyona) and ("I" in alyona) and (not "G" in alyona)):
        print("alyona must work G")
        shifts = shifts + "AlyonaG"
    elif (("A" in alyona) and ("B" in alyona) and ("C" in alyona) and ("D" in alyona) and ("E" in alyona) and ("G" in alyona) and (
            "H" in alyona) and ("I" in alyona) and (not "F" in alyona)):
        print("alyona must work F")
        shifts = shifts + "AlyonaF"
    elif (("A" in alyona) and ("B" in alyona) and ("C" in alyona) and ("D" in alyona) and ("F" in alyona) and ("G" in alyona) and (
            "H" in alyona) and ("I" in alyona) and (not "E" in alyona)):
        print("alyona must work E")
        shifts = shifts + "AlyonaE"
    elif (("A" in alyona) and ("B" in alyona) and ("C" in alyona) and ("E" in alyona) and ("F" in alyona) and ("G" in alyona) and (
            "H" in alyona) and ("I" in alyona) and (not "D" in alyona)):
        print("alyona must work D")
        shifts = shifts + "AlyonaD"
    elif (("A" in alyona) and ("B" in alyona) and ("D" in alyona) and ("E" in alyona) and ("F" in alyona) and ("G" in alyona) and (
            "H" in alyona) and ("I" in alyona) and (not "C" in alyona)):
        print("alyona must work C")
        shifts = shifts + "AlyonaC"
    elif (("A" in alyona) and ("C" in alyona) and ("D" in alyona) and ("E" in alyona) and ("F" in alyona) and ("G" in alyona) and (
            "H" in alyona) and ("I" in alyona) and (not "B" in alyona)):
        print("alyona must work B")
        shifts = shifts + "AlyonaB"
    elif (("B" in alyona) and ("C" in alyona) and ("D" in alyona) and ("E" in alyona) and ("F" in alyona) and ("G" in alyona) and (
            "H" in alyona) and ("I" in alyona) and (not "A" in alyona)):
        print("alyona must work A")
        shifts = shifts + "AlyonaA"

    # must work on A
    if (("A" in alyona) and ("A" in alex) and ("A" in ofir) and ("A" in yair) and ("A" in almog) and ("A" in pavel) and (
            "A" in sahar) and (not "A" in ran)):
        shifts = shifts + "ranA"
        print("hey")
    elif (("A" in alyona) and ("A" in alex) and ("A" in ofir) and ("A" in yair) and ("A" in almog) and ("A" in pavel) and (
            "A" in ran) and (not "A" in sahar)):
        shifts = shifts + "saharA"
        print("hey")
    elif (("A" in alyona) and ("A" in alex) and ("A" in ofir) and ("A" in yair) and ("A" in almog) and ("A" in sahar) and (
            "A" in ran) and (not "A" in pavel)):
        shifts = shifts + "pavelA"
        print("hey")
    elif (("A" in alyona) and ("A" in alex) and ("A" in ofir) and ("A" in yair) and ("A" in pavel) and ("A" in sahar) and (
            "A" in ran) and (not "A" in almog)):
        shifts = shifts + "almogA"
        print("hey")
    elif (("A" in alyona) and ("A" in alex) and ("A" in ofir) and ("A" in almog) and ("A" in pavel) and ("A" in sahar) and (
            "A" in ran) and (not "A" in yair)):
        shifts = shifts + "yairA"
        print("hey")
    elif (("A" in alyona) and ("A" in alex) and ("A" in yair) and ("A" in almog) and ("A" in pavel) and ("A" in sahar) and (
            "A" in ran) and (not "A" in ofir)):
        shifts = shifts + "ofirA"
        print("hey")
    elif (("A" in alyona) and ("A" in ofir) and ("A" in yair) and ("A" in almog) and ("A" in pavel) and ("A" in sahar) and (
            "A" in ran) and (not "A" in alex)):
        shifts = shifts + "alexA"
        print("hey")
    elif (("A" in alex) and ("A" in ofir) and ("A" in yair) and ("A" in almog) and ("A" in pavel) and ("A" in sahar) and (
            "A" in ran) and (not "A" in alyona)):
        shifts = shifts + "alyonaA"
        print("hey")

    shifts = shifts + "shifts:"

    print(shifts)


def button_clear():
    global val
    global alyona
    alyona = ""
    val = ""
    label_5 = customtkinter.CTkLabel(master=frame_1, text=("You have clear all request"))
    label_5.pack(pady=1, padx=1)


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=60, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text="Shifts Creator", justify=tkinter.LEFT)
label_1.pack(pady=12, padx=10)

# set the text


# entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
# entry_1.pack(pady=12, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1,
                                           values=["Alyona", "Alex", "Ofir", "Yair", "Almog", "Pavel", "Ran", "Sahar"])
optionmenu_1.pack(pady=12, padx=10)
optionmenu_1.set("Alyona")

combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Sun-Morning", "Mon-Morning", "Tue-Morning", "Wed-Morning",
                                                        "Thu-Morning", "Fri-Morning", "Sun-Night", "Mon-Night",
                                                        "Tue-Night", "Wed-Night", "Thu-Night", "Sat-Night"])
combobox_1.pack(pady=12, padx=10)
combobox_1.set("Sun-Morning")

button_1 = customtkinter.CTkButton(master=frame_1, text="save", command=button_callback)
button_1.pack(pady=12, padx=10)

button_2 = customtkinter.CTkButton(master=frame_1, text="finished", command=button_callback2)
button_2.pack(pady=12, padx=10)

button_3 = customtkinter.CTkButton(master=frame_1, text="Clear all", command=button_clear)
button_3.pack(pady=10, padx=8)

label_3 = customtkinter.CTkLabel(master=frame_1, text="Shifts blocked:", justify=tkinter.LEFT)
label_3.pack(pady=5, padx=3)

app.mainloop()
