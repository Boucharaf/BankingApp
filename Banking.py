import customtkinter as CTk
import tkinter as Tk
import datetime as dt
from tkinter import messagebox
from PIL import Image, ImageTk
import json

class BankingApp:

#CONSTRUCTOR 
    def __init__(self):
        self.home = CTk.CTk()
        self.initial_gui()
        self.users = []
        self.load_users()
        self.current_user = None  

# JSON Parts
    
    def save_users(self):
        with open("users.json", "w") as file:
            json.dump(self.users, file)

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                self.users = json.load(file)
        except FileNotFoundError:
        
            with open("users.json", "w") as file:
                json.dump([], file)


    def toggle_password_visibility(self):
        if self.show_password.get():
            self.champ2.configure(show="")
        else:
            self.champ2.configure(show="*")

#Initial page

    def initial_gui(self):
        self.home.geometry("1200x600")
        CTk.set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.home.grid_rowconfigure(0, weight=1)
        self.home.grid_columnconfigure(0, weight=1)
        self.home.resizable(width=False, height=False)
        
        home_frame = CTk.CTkFrame(master=self.home, width=1000, height=500)
        home_frame.pack(padx=0, pady=20, fill="both")
        home_frame.configure(bg_color="#2C3E50")
        image_ctk = CTk.CTkImage(light_image = Image.open('assets/68dfe759284dc5b24dcb194d3b46d79b.jpg'), size=(500, 500))
        image_label = CTk.CTkLabel(master=home_frame, image=image_ctk, text="")
        
        image_label.pack()
        image_label.place(x=0, y=0)

        home_label = CTk.CTkLabel(master=home_frame, text="WELCOME to the BIT's banking transaction management system", font=("Helvetica", 35, "bold"), text_color="#FFFFFF", wraplength=400)
        home_label.pack(pady=10, padx=20)
        home_label.place(x=700, y=25)
        home_label1 = CTk.CTkLabel(master=home_frame, text="Click on the buttton for log in", font=("Helvetica", 40, "bold"), text_color="#75AAFF", wraplength=400)
        home_label1.pack(pady=70, padx=20)
        home_label1.place(x=700, y=250)
        home_button1 = CTk.CTkButton(master=home_frame, text="NEXT", font=("Helvetica", 25, "bold"), command=self.login_page, hover_color="#00FF77", width= 100, height=40)
        home_button1.pack(pady=20, padx=10, ipady=40, ipadx=40)
        home_button1.place(x=770, y=400)


    
# login page
                
    def login_page(self):
        self.home.destroy()
        self.root = CTk.CTk()
        self.root.geometry("1200x600")
        CTk.set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.resizable(width=False, height=False)

        self.frame = CTk.CTkFrame(master=self.root, border_color="#222", border_width=5)
        self.frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.frame.pack(padx=60, pady=20, fill="both")
        
        self.title = CTk.CTkLabel(master=self.frame, text="Sign in", font=("Helvetica", 40, "bold"), text_color="#FFFFFF")
        self.title.pack(pady=10, padx=15)
        self.title.pack_propagate(False)
        
        self.champ1 = CTk.CTkEntry(master=self.frame, placeholder_text="Your name", width=350, height=40, font=("Helvetica", 20))
        self.champ1.pack(pady= 20, padx=10)
        
        self.champ2 = CTk.CTkEntry(master=self.frame, placeholder_text="Your password", show="*", width=350, height=40, font=("Helvetica", 20))
        self.champ2.pack(pady=20, padx=10)

        self.show_password = CTk.BooleanVar()
        show_password_checkbox = CTk.CTkCheckBox(master=self.frame, text="Show password", variable=self.show_password, command=self.toggle_password_visibility)
        show_password_checkbox.pack(pady=5)

        self.button1 = CTk.CTkButton(master=self.frame, text="Log in", hover_color="#0F968C", font=("Helvetica", 25, "bold"), command=self.login)
        self.button1.pack(pady=30, padx=10, ipady= 20, ipadx = 30)

        self.label1 = CTk.CTkLabel(master=self.frame, text="You don't have an account", font=("Helvetica", 20))
        self.label1.pack(pady=15, padx=10)
        self.label1.place(x=175, y= 445)

        self.button2 = CTk.CTkButton(master=self.frame, text="Create an account", font=("Helvetica", 23, "bold"), hover_color="#4158D0", command=self.sign_up)
        self.button2.pack(pady=50, padx=20, ipady=20)
        self.root.mainloop()


# function running the login-page
         
    def login(self):
        
        self.username = self.champ1.get()
        self.password = self.champ2.get()

        user_found = False
        for user in self.users:
            if user["name"] == self.username and user["password"] == self.password:
                user_found = True
                self.current_user = user
                break

        if user_found:
            self.menu()

        elif self.username == "" and self.password == "":
            messagebox.showinfo("Info", "Please enter your name and your password")
            
        else:
            messagebox.showerror("Error", "Incorrect username or password")
            #self.champ1.delete(0, "end")
            self.champ2.delete(0, "end")
            


#sign-up page
        
    def sign_up(self):
        self.new_window = CTk.CTk()
        self.new_window.geometry("1176x576")
        self.new_window._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.new_window.grid_rowconfigure(0, weight=1)
        self.new_window.grid_columnconfigure(0, weight=1)
        self.new_window.resizable(width=False, height=False)
        self.frame1 = CTk.CTkFrame(master=self.new_window)
        self.frame1.pack(padx=60, pady=20, fill="both")
        self.frame1.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")

        label_0 = CTk.CTkLabel(master=self.frame1, text="Create your account", font=("Helvetica", 40, "bold"), text_color="#FFFFFF")
        label_0.pack(pady=18, padx=10)

        self.champ3 = CTk.CTkEntry(master=self.frame1, placeholder_text="Your name", width=350, height=40, font=("Helvetica", 20))
        self.champ3.pack(pady=20, padx=10)

        self.champ4 = CTk.CTkEntry(master=self.frame1, placeholder_text="Password", show="*", width=350, height=40, font=("Helvetica", 20))
        self.champ4.pack(pady=20, padx=10)

        self.champ5 = CTk.CTkEntry(master=self.frame1, placeholder_text="Entrer your balance", width=350, height=40, font=("Helvetica", 20))
        self.champ5.pack(pady=20, padx=10)

        self.button2 = CTk.CTkButton(master=self.frame1, text="Create your account", hover_color="#0F968C", font=("Helvetica", 25, "bold"),command= self.creation)
        self.button2.pack(pady=30, padx=10, ipady= 20, ipadx = 30)

        self.new_window.mainloop()


# function running the sign-up page
            
    def creation(self):
        name = self.champ3.get()
        password = self.champ4.get()
        balance = self.champ5.get()
        if name != "" and password != "":
            if balance.isdigit():
                user_data = {"name": name, "password": password, "balance": balance}
                self.users.append(user_data)
                self.save_users()  # Save the users in the JSON file
                self.show_confirmation()
                return True
            else:
                messagebox.showerror("Error","Invalid balance, please start again")
                self.champ5.delete(0, "end")
                return False
            
        elif name != "" and password == "":
            messagebox.showerror("Error","Your password is not valid")
            self.champ4.delete(0, "end")
            return False
        
        elif name == "" and password != "":
            messagebox.showerror("Error","Your name is not valid")
            self.champ3.delete(0, "end")
            return False
        
        else:
             messagebox.showerror("Error","Your name and your password are not valid")
             self.champ3.delete(0, "end")
             self.champ4.delete(0, "end")
             self.champ5.delete(0, "end")
             self.new_window.destroy()
             return False


             
            
    def show_confirmation(self):
        self.window2 = CTk.CTk()
        self.window2.geometry("1176x576")
        self.window2._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        #self.window2.grid_rowconfigure(0, weight=1)
        #self.window2.grid_columnconfigure(0, weight=1)
        self.window2.resizable(width=False, height=False)
        self.frame1 = CTk.CTkFrame(master=self.window2, height=500)
        self.frame1.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.frame1.pack(padx=60, pady=80, fill="both")

        label1 = CTk.CTkLabel(master=self.frame1, text="Account creation", font=("Helvetica", 40, "bold"), text_color="#FFFFFF")
        label1.pack(pady=12, padx=10)

        labell = CTk.CTkLabel(master=self.frame1, text="Your account has been successfully created", font=("Helvetica", 20, "bold"))
        labell.pack()
        
        button_back = CTk.CTkButton(master=self.frame1, text="Come back to Log in", hover_color="#0F968C", font=("Helvetica", 25, "bold"), command= self.windows_destroy_1)
        button_back.pack(pady=30, padx=10, ipady= 20, ipadx = 30)
        self.window2.mainloop()


 # Show menu
           
    def menu(self):
        self.root.destroy()
        self.menu_ctk = CTk.CTk()
        self.menu_ctk.geometry("1200x600")
        self.menu_ctk._set_appearance_mode('dark')
        CTk.set_default_color_theme("dark-blue")
        self.menu_ctk.grid_rowconfigure(0, weight=1)
        self.menu_ctk.grid_columnconfigure(0, weight=1)
        #self.menu_ctk.resizable(width=False, height=False)
        self.menu_frame = CTk.CTkFrame(master=self.menu_ctk, width=1000, height=550)
        self.menu_frame.pack()
        self.menu_frame.grid(row=0, column=0, padx=10, pady=25, sticky="nsew")
        menu_label0 = CTk.CTkLabel(master= self.menu_frame, text="Welcome", font=("Helvetica", 35, "bold"), text_color="#FFFFFF")
        menu_label0.pack(pady=10, padx=20)
        menu_label0.place(x= 450, y=25)
        menu_label00 = CTk.CTkLabel(master= self.menu_frame, text= " "+self.current_user['name'], font=("Helvetica", 40, "bold"),text_color="#15FF99")
        menu_label00.pack(pady=10, padx=20)
        menu_label00.place(x=600, y=20)
        menu_label2 = CTk.CTkLabel(master=self.menu_frame, text= "What do you want to do", font=("Helvetica", 30, "bold"))
        menu_label2.pack(pady=30, padx=20)
        menu_label2.place(x=500,y=70)

        menu_label3 = CTk.CTkButton(master=self.menu_frame, text= "1. See your balance", font=("Helvetica", 20), hover_color="#0F968C", width= 150, height=45, command=self.see_balance)
        menu_label3.pack(pady=40, padx=20)
        menu_label3.place(x=500, y=140)

        menu_label4 = CTk.CTkButton(master=self.menu_frame, text= "2. Make a deposit", font=("Helvetica", 20), hover_color="#0F968C", width= 150, height=45, command=self.deposit)
        menu_label4.pack(pady=40, padx=20)
        menu_label4.place(x=500, y=210)

        menu_label5 = CTk.CTkButton(master=self.menu_frame, text= "3. Make a withdraw", font=("Helvetica", 20), hover_color="#0F968C", width= 150, height=45, command=self.withdraw)
        menu_label5.pack(pady=60, padx=20)
        menu_label5.place(x=500, y=280)

        menu_label6 = CTk.CTkButton(master=self.menu_frame, text= "4. Make a transfer", font=("Helvetica", 20), hover_color="#0F968C", width= 150, height=45, command= self.transfer)
        menu_label6.pack(pady=60, padx=20)
        menu_label6.place(x=500, y=350)

        menu_label7 = CTk.CTkButton(master=self.menu_frame, text= "5. View historic of transactions", font=("Helvetica", 20), hover_color="#0F968C", width= 150, height=45, command= self.view_historic)
        menu_label7.pack(pady=40, padx=20)
        menu_label7.place(x=500, y=420)

        menu_label8 = CTk.CTkButton(master=self.menu_frame, text= "6. Exit", font=("Helvetica", 20), hover_color="#0F968C", width= 150, height=45, command=self.exit)
        menu_label8.pack(pady=40, padx=20)
        menu_label8.place(x=500, y=490
                          )
        self.menu_ctk.mainloop()

# Function that shows the balance
            
    def see_balance(self):
        #self.menu_ctk.destroy()
        self.balance_ctk = CTk.CTk()
        self.balance_ctk.geometry("1176x576")
        self.balance_ctk._set_appearance_mode('dark')
        CTk.set_default_color_theme("dark-blue")
        self.balance_ctk.grid_rowconfigure(0, weight=1)
        self.balance_ctk.grid_columnconfigure(0, weight=1)
        #self.balance_ctk.resizable(width=False, height=False)
        self.balance_frame = CTk.CTkFrame(master=self.balance_ctk, width=1000, height=550)
        self.balance_frame.pack()
        self.balance_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        balance_label = CTk.CTkLabel(master=self.balance_frame, text= "Your balance is ", font=("Helvetica", 30), text_color="#FFFFFF")
        balance_label.pack(pady=15, padx=10)
        if self.current_user:
            sold = self.current_user.get("balance")
            balance_label3 = CTk.CTkLabel(master=self.balance_frame, text= "$", font=("Helvetica", 40), text_color="#00FF00")
            balance_label3.place(x=705, y=70)
            balance_label3.pack()
            balance_label2 = CTk.CTkLabel(master=self.balance_frame, text= sold,  font=("Helvetica", 40, "bold"), text_color="#00FF00")
            balance_label2.place(x=710, y=70)
            balance_label2.pack()
            self.log_action("Bank check")
        go_back_btn = CTk.CTkButton(master=self.balance_frame, text="Go Back",font=("Helvetica", 30, "bold"), hover_color="#4158D0", command=self.windows_destroy_0)
        go_back_btn.pack(pady=80, padx=20, ipady=30)
        self.balance_ctk.mainloop()

        

# function to make a deposit

    def deposit(self):
        self.dep_menu = CTk.CTk()
        self.dep_menu.geometry("1176x576")
        self.dep_menu._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.dep_menu.grid_rowconfigure(0, weight=1)
        self.dep_menu.grid_columnconfigure(0, weight=1)
        self.dep_menu.resizable(width=False, height=False)
        self.dep_frame = CTk.CTkFrame(master=self.dep_menu, width=1000, height=550)
        self.dep_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.dep_frame.pack(padx=60, pady=20, fill="both")

        dep_label = CTk.CTkLabel(master=self.dep_frame, text="Enter the amount to deposit", font=("Helvetica", 40, "bold"), text_color="#FFFFFF")
        dep_label.pack(pady=20, padx=10)

        self.dep_entry = CTk.CTkEntry(master=self.dep_frame, placeholder_text="Enter the amount here", width=600, height=60, font=("Helvetica", 40))
        self.dep_entry.pack(pady=20, padx=10)

        dep_button = CTk.CTkButton(master=self.dep_frame, text="Valid", command=self.depot,  hover_color="#0F968C", font=("Helvetica", 30, "bold"))
        dep_button.pack(pady=50, padx=20, ipady= 30, ipadx = 50)

        self.dep_menu.mainloop()

# function that run the deposit menu
        
    def depot(self):
        #self.dep_menu.destroy()
        self.dep_2_menu = CTk.CTk()
        self.dep_2_menu.geometry("1176x576")
        CTk.set_default_color_theme("dark-blue")
        self.dep_2_menu.grid_rowconfigure(0, weight=1)
        self.dep_2_menu.grid_columnconfigure(0, weight=1)
        self.dep_2_menu.resizable(width=False, height=False)
        self.dep_2_menu._set_appearance_mode("dark")
        self.dep_2_frame = CTk.CTkFrame(master=self.dep_2_menu, width=1000, height=550)
        self.dep_2_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.dep_2_frame.pack(padx=60, pady=20, fill="both")

        dep_confirm = CTk.CTkLabel(master=self.dep_2_frame, text="Your deposit has been successfully completed. Your new balance is: ", font=("Helvetica", 30), text_color="#FFFFFF")
        dep_confirm.pack(pady=20, padx=10)
        if self.current_user:
            sold = int(self.current_user.get("balance", 0))  
            amount_deposited = self.dep_entry.get()
            if amount_deposited.isdigit():
                amount_deposited = int(self.dep_entry.get())
                if amount_deposited > 0:
                    self.current_user['balance'] = sold + amount_deposited 
                    balance_label2 = CTk.CTkLabel(master=self.dep_2_frame, text=self.current_user['balance'], font=("Helvetica", 40, "bold"), text_color="#15FF99")
                    balance_label2.pack(pady=20, padx=10)
                    self.log_action("deposit", amount_deposited)
                    go_back_btn_1 = CTk.CTkButton(master=self.dep_2_frame, text="Go Back", hover_color="#0F968C", font=("Helvetica", 25, "bold"), command=self.windows_destroy_2)
                    go_back_btn_1.pack(pady=50, padx=20, ipady= 30, ipadx = 50)
                    self.dep_2_menu.mainloop()
                else:
                    messagebox.showerror('Error','The amount must be positive')
                    self.dep_entry.delete(0, "end")
                    self.dep_menu.destroy()
            else:
                messagebox.showerror("Error","Invalid amount, try again")
                self.dep_entry.delete(0, "end")
                self.dep_menu.destroy()

            
    # function hat shows the withdraw menu
        
    def withdraw(self):
        self.wd_menu = CTk.CTk()
        self.wd_menu.geometry("1176x576")
        self.wd_menu._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.wd_menu.grid_rowconfigure(0, weight=1)
        self.wd_menu.grid_columnconfigure(0, weight=1)
        self.wd_menu.resizable(width=False, height=False)
        self.wd_frame = CTk.CTkFrame(master=self.wd_menu, width=1000, height=550)
        self.wd_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.wd_frame.pack(padx=60, pady=20, fill="both")
        wd_label = CTk.CTkLabel(master=self.wd_frame, text="Enter the amount to withdraw", font=("Helvetica", 40), text_color="#FFFFFF")
        wd_label.pack(pady=20, padx=10)
        self.wd_entry = CTk.CTkEntry(master=self.wd_frame, placeholder_text="Enter the amount here", width=350, height=40, font=("Helvetica", 20))
        self.wd_entry.pack(pady=20, padx=10)
        wd_button = CTk.CTkButton(master=self.wd_frame, text="Valid", command=self.withdraw_confirm, hover_color="#0F968C", font=("Helvetica", 30, "bold"))
        wd_button.pack(pady=50, padx=20, ipady= 30, ipadx = 50)

        self.wd_menu.mainloop()

    #function that running the withdraw menu

    def withdraw_confirm(self):
        self.wd_2_menu = CTk.CTk()
        self.wd_2_menu.geometry("1176x576")
        self.wd_2_menu._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.wd_2_menu.grid_rowconfigure(0, weight=1)
        self.wd_2_menu.grid_columnconfigure(0, weight=1)
        self.wd_2_menu.resizable(width=False, height=False)
        self.wd_2_frame = CTk.CTkFrame(master=self.wd_2_menu, width=1000, height=550)
        self.wd_2_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.wd_2_frame.pack(padx=60, pady=20, fill="both")
        if self.current_user:
            sold = int(self.current_user.get("balance", 0))  # Convertir en entier
            amount_withdraw = self.wd_entry.get()
            if amount_withdraw.isdigit():
                amount_withdraw = int(self.wd_entry.get())
                if sold >= amount_withdraw:
                    self.current_user['balance'] = sold - amount_withdraw
                    self.wd_2_label = CTk.CTkLabel(master=self.wd_2_frame, text="Your withdraw has been successfully completed. Your new balance is: ", font=("Helvetica", 30), text_color="#FFFFFF")
                    self.wd_2_label.pack(pady=20, padx=10)
                    balance_label2 = CTk.CTkLabel(master=self.wd_2_frame, text=self.current_user['balance'], font=("Helvetica", 40, "bold"), text_color="#15FF99")
                    balance_label2.pack(pady=20, padx=10)
                    self.log_action("withdraw", amount_withdraw)

                    go_back_btn_2 = CTk.CTkButton(master=self.wd_2_frame, text="Go Back", hover_color="#0F968C", font=("Helvetica", 25, "bold"), command=self.windows_destroy_3)
                    go_back_btn_2.pack(pady=50, padx=20, ipady= 30, ipadx = 50)
                    self.wd_2_menu.mainloop()
                else:
                    messagebox.showwarning( "Warning","Your balance is insufficient for performing this operation ")
                    self.wd_entry.delete(0,"end")
                    self.wd_menu.destroy()
            else:
                messagebox.showerror("Error", "Invalid amount, try again")
                self.wd_entry.delete(0,"end")
                self.wd_menu.destroy()

    # function that shows the transfer menu

    def transfer(self):
        self.tr_menu = CTk.CTk()
        self.tr_menu.geometry("1176x576")
        self.tr_menu._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.tr_menu.grid_rowconfigure(0, weight=1)
        self.tr_menu.grid_columnconfigure(0, weight=1)
        self.tr_menu.resizable(width=False, height=False)
        self.tr_frame = CTk.CTkFrame(master=self.tr_menu, width=1000, height=550)
        self.tr_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.tr_frame.pack(padx=60, pady=20, fill="both")
        self.tr_entry = CTk.CTkEntry(master=self.tr_frame, placeholder_text="Enter the name of recipient here", width=500, height=75, font=("Helvetica", 30))
        self.tr_entry.pack(pady=20, padx=10)
        self.tr_entry2 = CTk.CTkEntry(master=self.tr_frame, placeholder_text="Enter the amount to withdraw here", width=500, height=75, font=("Helvetica", 30))
        self.tr_entry2.pack(pady=20, padx=10)
        tr_button = CTk.CTkButton(master=self.tr_frame, text="Valid", command=self.transfer_confirm, hover_color="#0F968C", font=("Helvetica", 30, "bold"))
        tr_button.pack(pady=50, padx=20, ipady= 30, ipadx = 50)

        self.tr_menu.mainloop()


    # function that running the transfer menu
        
    def transfer_confirm(self):
        self.tr_2_menu = CTk.CTk()
        self.tr_2_menu.geometry("1176x576")
        self.tr_2_menu._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        self.tr_2_menu.grid_rowconfigure(0, weight=1)
        self.tr_2_menu.grid_columnconfigure(0, weight=1)
        self.tr_2_menu.resizable(width=False, height=False)
        self.tr_2_frame = CTk.CTkFrame(master=self.tr_2_menu, width=1000, height=550)
        self.tr_2_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.tr_2_frame.pack(padx=60, pady=20, fill="both")
        if self.current_user:
            sold = int(self.current_user.get("balance", 0))  
            amount_transfer = self.tr_entry2.get()  
            recipient = self.tr_entry.get()
            if amount_transfer.isdigit():
                amount_transfer = int(self.tr_entry2.get())
                if amount_transfer > sold:
                    messagebox.showinfo('Info','The amount to transfer is too large. Try again')
                    self.tr_entry2.delete(0,"end")
                    self.tr_2_menu.destroy()
                    self.tr_menu.destroy()
                else:
                    recipient_exists = False
                    for user in self.users:
                        if user['name'] == recipient:
                            recipient_exists = True
                            user['balance'] = int(user['balance']) + amount_transfer  
                            break
                    if recipient_exists:
                        self.current_user['balance'] = sold - amount_transfer
                        tr_2_label = CTk.CTkLabel(master=self.tr_2_frame, text="Your have transferred", font=("Helvetica", 25), text_color="#FFFFFF")
                        tr_2_label.pack(pady=20, padx=10)
                        tr_3_label = CTk.CTkLabel(master=self.tr_2_frame, text = f"{amount_transfer}", font=("Helvetica", 40, "bold"), text_color="#15FF99")
                        tr_3_label.pack(pady=10, padx=10)
                        tr_4_label = CTk.CTkLabel(master=self.tr_2_frame, text="to", font=("Helvetica", 25), text_color="#FFFFFF")
                        tr_4_label.pack(pady=10, padx=10)
                        tr_5_label = CTk.CTkLabel(master=self.tr_2_frame, text=recipient, font=("Helvetica", 40, "bold"), text_color="#FFFFFF")
                        tr_5_label.pack(pady=10, padx=10)
                        tr_6_label = CTk.CTkLabel(master=self.tr_2_frame, text="Your new balance is :", font=("Helvetica", 30), text_color="#FFFFFF")
                        tr_6_label.pack(pady=20, padx=10)
                        tr_7_label = CTk.CTkLabel(master=self.tr_2_frame, text=self.current_user['balance'], font=("Helvetica", 40, "bold"), text_color="#15FF99")
                        tr_7_label.pack(pady=20, padx=10)
                        self.log_action("transfer", amount_transfer) 
                        go_back_btn = CTk.CTkButton(master=self.tr_2_frame, text="Go Back", command=self.windows_destroy_4, hover_color="#0F968C", font=("Helvetica", 25, "bold"))
                        go_back_btn.pack(pady=20, padx=20, ipady= 30, ipadx = 50)  
        
                    else:
                        messagebox.showerror("Recipient not found", "The recipient does not exist.")
                        self.tr_2_menu.destroy()
                        self.tr_menu.destroy()
                        
            else:
                messagebox.showerror("Error","Invalid amount, please try again")
                self.tr_2_menu.destroy()
                self.tr_menu.destroy()
                           
        self.tr_2_menu.mainloop()
    

    # function that shows the historic of each account
    def view_historic(self):
        self.view_menu = CTk.CTk()
        self.view_menu.geometry("1200x600")
        self.view_menu._set_appearance_mode("dark")
        CTk.set_default_color_theme("dark-blue")
        #self.view_menu.grid_rowconfigure(0, weight=1)
        #self.view_menu.grid_columnconfigure(0, weight=1)
        self.view_menu.resizable(width=False, height=False)
        self.view_frame = CTk.CTkScrollableFrame(master=self.view_menu, orientation="vertical", width=1100, height=600)
        self.view_frame.grid(row=0, column=0, padx=20, pady=50, sticky="nsew")
        self.view_frame.pack(padx=60, pady=75, fill="both")
        view_label = CTk.CTkLabel(master=self.view_menu, text="List of past transactions",  font=("Helvetica", 30, "bold"), text_color="#FFFFFF")
        view_label.pack(pady=20, padx=10)
        view_label.place(x=480,y=0)
        
        if self.current_user:
            if "history" in self.current_user:
                for action in self.current_user["history"]:

                    view_label5 = CTk.CTkLabel(master=self.view_frame, text= f"Time:{action['timestamp']}", font=("Helvetica", 23), text_color="#FFFFFF")
                    view_label5.pack(pady=0, padx=0)

                    view_label1 = CTk.CTkLabel(master=self.view_frame, text= f"Type of transaction: {action['type']} ", font=("Helvetica", 23), text_color="#FFFFFF")
                    view_label1.pack(pady=0, padx=100)

                    view_label3 = CTk.CTkLabel(master=self.view_frame, text= f"Amount: {action['amount']}", font=("Helvetica", 23), text_color="#FFFFFF")
                    view_label3.pack(pady=0, padx=100)

                    view_label4 = CTk.CTkLabel(master=self.view_frame, text= "", font=("Helvetica", 23), text_color="#FFFFFF")
                    view_label4.pack(pady=20, padx=0)

                    
            else:
                    view_label1 = CTk.CTkLabel(master=self.view_frame, text= "No transaction history available", font=("Helvetica", 40), text_color="#FFFFFF")
                    view_label1.pack(pady=20, padx=10)
        go_back_btn = CTk.CTkButton(master=self.view_menu, text="Go Back", command=self.windows_destroy_5, hover_color="#0F968C", font=("Helvetica", 25, "bold"))
        go_back_btn.pack(pady=10, padx=20, ipady= 30, ipadx = 50)
        go_back_btn.place(x=600,y=545)
        self.view_menu.mainloop()
    
        
    def log_action(self, action_type, amount=None):
        if self.current_user:
            timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            action = {
                "type": action_type,
                "timestamp": timestamp,
                "amount": amount
            }
            self.current_user.setdefault("history", []).append(action)
            self.save_users()

    def exit(self):
        self.menu_ctk.destroy()
    
    ## destruction of windows
        
    def windows_destroy_0(self):
        self.balance_ctk.destroy()

    def windows_destroy_1(self):
        self.window2.destroy()
        self.new_window.destroy()

    def windows_destroy_2(self):
        self.dep_2_menu.destroy()
        self.dep_menu.destroy()

    def windows_destroy_3(self):
        self.wd_2_menu.destroy()
        self.wd_menu.destroy()

    def windows_destroy_4(self):
        self.tr_2_menu.destroy()
        self.tr_menu.destroy()

    def windows_destroy_5(self):
        self.view_menu.destroy()

#  Processing
if __name__ == "__main__":
    app = BankingApp()
    app.home.mainloop()
