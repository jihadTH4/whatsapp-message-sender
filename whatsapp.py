import pywhatkit as kit
from tkinter import *
import pyautogui as pt
from win10toast import ToastNotifier


FONT = "Arial"
FONT_SIZE = 12
WIN_WIDTH = 600
WIN_HEIGHT = 200
ENTRY_BG = "#13baac"
message_sent = False
phone = False

def send_whatsapp():
    try:
        phone_number = PH_NUM.get()      
        message = MSG.get("1.0", "end-1c")  # Get the message from the Text widget
        hour = int(HR.get())
        minute = int(MIN.get())
        kit.sendwhatmsg(phone_number, message, hour, minute)
        message_sent = True
        if message_sent:
            toaster = ToastNotifier()
            toaster.show_toast("Done !",
            "The message was sent sucssefully",
            icon_path=None,
            duration=5,
            threaded=True)
        else:
            pt.alert(text="Something went wrong!..please try again")
    except Exception:
        pt.alert(text="Something went wrong!..please try again")

window = Tk()
window.title("Send WhatsApp Message")
window.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")
window.iconbitmap("C:\\Users\\HP\\Downloads\\send_qsM_icon.ico")
# To center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

phone_label = Label(window, text="Enter phone number here", font=(FONT, FONT_SIZE))
phone_label.grid(row=0, column=0)
msg_label = Label(window, text="Enter message here", font=(FONT, FONT_SIZE))
msg_label.grid(row=1, column=0)
hour_label = Label(window, text="Enter the hour here", font=(FONT, FONT_SIZE))
hour_label.grid(row=2, column=0)
min_label = Label(window, text="Enter minutes here", font=(FONT, FONT_SIZE))
min_label.grid(row=3, column=0)

PH_NUM = Entry(window, font=(FONT, FONT_SIZE), bg=ENTRY_BG)
PH_NUM.grid(row=0, column=1)
MSG = Text(window, font=(FONT, FONT_SIZE), width=20, height=2, bg=ENTRY_BG)
MSG.grid(row=1, column=1)
HR = Entry(window, font=(FONT, FONT_SIZE), bg=ENTRY_BG)
HR.grid(row=2, column=1)  # 24 hours format
MIN = Entry(window, font=(FONT, FONT_SIZE), bg=ENTRY_BG)
MIN.grid(row=3, column=1)

send_button = Button(window, text="Send", font=(FONT, FONT_SIZE), command=send_whatsapp, bg="#25bd11")
send_button.grid(row=4, column=0, columnspan=1, sticky="e")


window.mainloop()
