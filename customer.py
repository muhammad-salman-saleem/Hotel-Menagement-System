from tkinter import *
from PIL import Image,ImageTk


class Customer_Window:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1140x490+207+207')
        self.root.title('CUSTOMER DETAILS')
        root.resizable(False, False)
        # ===================== Color Tage========================
        title_bg = 'black'
        title_fg = 'gold'
#================ Title============================
        title_lbl=Label(self.root, text="Add Customer Details", bd=4, relief=RIDGE, bg=title_bg,fg=title_fg, font=("times new roman", 30, "bold"), )
        title_lbl.place(x=0,y=0,width=1140,height=50)


if __name__ == '__main__':
    root = Tk()
    obj = Customer_Window(root)
    root.mainloop()