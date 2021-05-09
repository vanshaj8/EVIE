from tkinter import *
from chatgui import getResponse,chatbot_response,bot_name

BG_GRAY = "#ABB2B9"
BG_COLOR = "#404AA0"
TEXT_COLOR = "#EAECEE"

FONT = "Montserrat 14"
FONT_BOLD = "Montserrat 15"

class ChatApplication:

    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title("LOIE")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=800, height=500, bg=BG_COLOR)

        # head label
        head_label = Label(self.window, bg=TEXT_COLOR, fg=BG_COLOR,
                           text="Chatting with Evie", font=FONT_BOLD, anchor='w')
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.window, width=800, bg=TEXT_COLOR)
        line.place(relwidth=1,rely=0.06, relheight=0.3)

        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label = Label(self.window, bg=BG_COLOR, height=40)
        bottom_label.place(relwidth=1, rely=0.822)

        # message entry box
        self.msg_entry = Entry(bottom_label, bg=TEXT_COLOR, fg="black", font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)

        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")

    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"{bot_name}: {chatbot_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)


if __name__ == "__main__":
    app = ChatApplication()
    app.run()
