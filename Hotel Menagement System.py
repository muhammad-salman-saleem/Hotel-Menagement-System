from tkinter import *
from PIL import Image,ImageTk
from customer import Customer_Window
from rooms import Room_Window
from details import Detail_Window
from reports import Report_Window


class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title('HOTEL MANAGEMENT SYSTEM')
        # root.resizable(False, False)

    #===================== Color Tage========================
        title_bg='black'
        title_fg='gold'

        btn_bg = 'black'
        btn_fg = 'gold'
    #===================== Image 01 Frame=====================
        img1=Image.open(r"hotel images\hotel1.png")
        img1=img1.resize((1350,120),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1350,height=120)

    #===================== Logo Image==============================
        img2 = Image.open(r"hotel images\logohotel.png")
        img2 = img2.resize((230, 120), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=120)

    #================ Title============================
        title_lbl=Label(self.root, text="HOTEL MANAGEMENT SYSTEM", bd=4, relief=RIDGE, bg=title_bg,fg=title_fg, font=("times new roman", 30, "bold"), )
        title_lbl.place(x=0,y=120,width=1350,height=50)

    #===================== Main Frame=========================
        main_frame = Frame(self.root, relief=RIDGE,bd=4)
        main_frame.place(x=0, y=170, width=1350, height=530)

    #====================== Menue============================
        menue_lbl = Label(main_frame, text="MENUE", bd=4, relief=RIDGE, bg=title_bg, fg=title_fg,font=("times new roman", 20, "bold"), )
        menue_lbl.place(x=0,y=0,width=200)
#===================== btn Frame=========================
        btn_frame = Frame(main_frame, relief=RIDGE,bd=4)
        btn_frame.place(x=0, y=35, width=200, height=200)

        cust_btn = Button(btn_frame, text="CUSTOMER",font=("arial", 12, "bold"),command=self.cust_details, width=18, bg=btn_bg, fg=btn_fg, bd=5, relief=RIDGE,cursor='hand2' ).grid(row=0, column=0, )
        room_btn = Button(btn_frame, text="ROOM",font=("arial", 12, "bold"),command=self.room_details, width=18, bg=btn_bg, fg=btn_fg, bd=5, relief=RIDGE,cursor='hand2' ).grid(row=1, column=0, )
        details_btn = Button(btn_frame, text="DETAILS",font=("arial", 12, "bold"),command=self.details, width=18, bg=btn_bg, fg=btn_fg, bd=5, relief=RIDGE,cursor='hand2' ).grid(row=2, column=0, )
        report_btn = Button(btn_frame, text="REPORT",font=("arial", 12, "bold"),command=self.report_details, width=18, bg=btn_bg, fg=btn_fg, bd=5, relief=RIDGE,cursor='hand2' ).grid(row=3, column=0, )
        logout_btn = Button(btn_frame, text="LOG OUT",font=("arial", 12, "bold"), width=18, bg=btn_bg, fg=btn_fg, bd=5, relief=RIDGE,cursor='hand2' ).grid(row=4, column=0, )

#======================== Right Side Image===================================
        img3 = Image.open(r"hotel images\slide3.jpg")
        img3 = img3.resize((1142, 525), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(main_frame, image=self.photoimg3, relief=RIDGE)
        lblimg3.place(x=200, y=0, width=1142, height=525)

        # ======================== down Side Image===================================
        img4 = Image.open(r"hotel images\coffee-quotes.jpg")
        img4 = img4.resize((200, 150), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        down_img1 = Label(main_frame, image=self.photoimg4, relief=RIDGE)
        down_img1.place(x=0, y=225, width=200, height=150)
                    #===================================================#
        img5 = Image.open(r"hotel images\myh.jpg")
        img5 = img5.resize((200, 150), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        down_img2 = Label(main_frame, image=self.photoimg5, relief=RIDGE)
        down_img2.place(x=0, y=375, width=200, height=150)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_Window(self.new_window)

    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_Window(self.new_window)

    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=Detail_Window(self.new_window)

    def report_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Report_Window(self.new_window)



if __name__ == '__main__':
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
