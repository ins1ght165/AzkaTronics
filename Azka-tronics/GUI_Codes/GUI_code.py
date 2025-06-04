from tkinter import *
from tkinter.scrolledtext import *
from main_for_GUI import *

class Azkabot:
    def __init__(self):
            
        self.window = Tk()
        self.customizeWindow()
        self.add_widgets()


            


    def run(self):
        self.window.mainloop()

    def customizeWindow(self):
        self.window.title("Azkabot")
        self.window.geometry('500x700+500+50')
        self.window.resizable(False,False)
        self.window.attributes('-alpha',1)
        self.window.iconbitmap('./bot.ico')
        self.window.configure(bg="white")


    def add_widgets(self):
        BG_GRAY = "#ABB2B9"
        BG_COLOR = "#17202A"
        TEXT_COLOR = "#EAECEE"
        FONT = "Helvetica 13"
        FONT_BOLD = "Helvetica 13 bold"
        title = Label(self.window, bg = "#2C3E50", fg= "white", text="You are now chating with Azkabot!", font="Calibri", padx="25", pady="25")
        title.place(x=250,y=30,anchor="center")

        self.text_widget = ScrolledText(self.window, height='600', width='45',font="Calibri 13",wrap=WORD)
        self.text_widget = Text(self.window, width=2, height=2, bg=BG_COLOR, fg="white",font="Calibri 13", padx=5, pady=5)
        self.text_widget.place(relheight=0.9, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)


        self.msg_entry = Entry(self.window, bg="#2C3E50", fg="white", font="Calibri", width=75)
        self.msg_entry.place(relwidth=1, relheight=0.06, x=0, y=659)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)


        e = Entry(self.window, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
        send_button = Button(self.window, text="Send", font=FONT_BOLD, width=10, bg=BG_GRAY,command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.85, y=660, relheight=0.06, relwidth=0.16)

    def _on_enter_pressed(self, event):
        if (len(prev_selections)!=0 and prev_selections[-1]=="View selected"): 
            self.windowTable = Tk()
            self.Table_window()
            self.iphone_Table()
        if (len(prev_selections)!=0 and prev_selections[-1]=="Compare Selected"):
            compare_devices(compare_lists[0],compare_lists[1],compare_lists[2],compare_lists[3],compare_lists[4])
            self.windowTable = Tk()
            self.Table_window()
            self.iphone_Table()
        msg  = self.msg_entry.get()
        if not msg:
            return
        self._insert_message(msg,"You")
        prev_selections.append(msg)
        self.bot_reply(m_chatbot(msg, prev_selections))


    def _insert_message(self, msg, sender):
        if not msg:
            return         
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.yview(END)

    def bot_reply(self,msg):         
        self.msg_entry.delete(0, END)
        msg1 = f"{'Azkabot'}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        self.text_widget.yview(END)

    def Table_window(self):
        self.windowTable.title("Viewing You Product Specs")
        self.windowTable.geometry('')
        self.windowTable.resizable(False,False)
        self.windowTable.attributes('-alpha',1)
        self.windowTable.configure(bg="Grey")
        

    def iphone_Table(self):
        
        total_rows = len(view_specs_L)
        total_columns = len(view_specs_L[0])
        for i in range(total_rows):
            for j in range(total_columns):    
                self.e = Entry(self.windowTable, width=50, fg='black',font=('Arial',12))               
                self.e.grid(row=i, column=j)
                self.e.insert(END, view_specs_L[i][j])
                self.e.configure(state=DISABLED)
        


if __name__ == "__main__":

    app = Azkabot()

    app.run()