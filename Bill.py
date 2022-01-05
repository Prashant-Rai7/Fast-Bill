from tkinter import*
import math,random,os
from tkinter import messagebox

class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        
        self.root.wm_iconbitmap("Bill Logo.ico")
        
        bg_color="#074463"
        title=Label(self.root,text='Billing Software',bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)
        
        
        
        
        
        #____________________Variables_________________
        
    
        
        ###================Cosmetics===================
        
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()

        
        ###==================Grocery====================
        
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()


        ###=================Cold Drinks ==================
        
        
        self.limca=IntVar()
        self.coke=IntVar()
        self.frooti=IntVar()
        self.sprite=IntVar()
        self.thumsup=IntVar()
        self.fanta=IntVar()
        
        
        ###===================Total Product Price & Tax Variable===============
        
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_drinks_price=StringVar()
        
        
        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drinks_tax=StringVar()
        
        
        ###=================Customers============================
        
        self.c_name=StringVar()
        self.c_phone=StringVar()
        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        
        self.search_bill=StringVar()
        
        
    
        #____________________________________CUSTOMER DETAILS_______________________________
        
        ### -------------Customer Details Frame = F1
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,'bold'),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        
        ## -------------Customer Name
        customer_name_label = Label(F1,text="Customer Name",bg=bg_color, fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        customer_name_text = Entry(F1,width=15,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        ## -------------Contact Number
        contact_number_label = Label(F1,text="Phone No.",bg=bg_color, fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        ontact_number_text = Entry(F1,width=15,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)
        
        ## -------------Bill Number
        Bill_number_label = Label(F1,text="Bill No.",bg=bg_color, fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        Bill_number_text = Entry(F1,width=15,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        ## -------------Search Button
        Search_Button = Button(F1, text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=60)
        
        
        
        #___________________________ PRODUCTS ENTRY_________________________
        
        ## -------------Cosmetic Frame
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,'bold'),fg="gold",bg=bg_color)
        F2.place(x=0,y=183,width=325,height=380)
        
        Bath_Soap_label = Label(F2,text="Bath Soap",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10)
        Bath_Soap_text = Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        Face_Cream_label = Label(F2,text="Face Cream",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10)
        Face_Cream_text = Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
       
        Face_Wash_label = Label(F2,text="Face Wash",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10)
        Face_Wash_text = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
       
        Hair_Spray_label = Label(F2,text="Hair Spray",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10)
        Hair_Spray_text = Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
       
        Hair_Gel_label = Label(F2,text="Hair Gel",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10)
        Hair_Gel_text = Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
       
        Body_Lotion_label = Label(F2,text="Body Loshan",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10)
        Body_Lotion_text = Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
       
        
        
        
        ## -------------Grocery Frame
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,'bold'),fg="gold",bg=bg_color)
        F3.place(x=330,y=183,width=325,height=380)
        
        Rice_label = Label(F3,text="Rice",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10)
        Rice_text = Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        Food_oil_label = Label(F3,text="Food Oil",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10)
        Food_oil_text = Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
       
        Daal_label = Label(F3,text="Daal",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10)
        Daal_text = Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
       
        Wheat_label = Label(F3,text="Wheat",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10)
        Wheat_text = Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
       
        Sugar_label = Label(F3,text="Sugar",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10)
        Sugar_text = Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
       
        Tea_label = Label(F3,text="Tea",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10)
        Tea_text = Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
       
        
        
        
        
        
        
        ## -------------Cold Drinks Frame
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks",font=("times new roman",15,'bold'),fg="gold",bg=bg_color)
        F4.place(x=660,y=183,width=325,height=380)
        
        
        Limca_label = Label(F4,text="Limca",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=0,column=0,padx=10,pady=10)
        Limca_text = Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,pady=10,padx=10)
        
        Coke_label = Label(F4,text="Coke",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=1,column=0,padx=10,pady=10)
        Coke_text = Entry(F4,width=10,textvariable=self.coke,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,pady=10,padx=10)
       
        Frooti_label = Label(F4,text="Frooti",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=2,column=0,padx=10,pady=10)
        Frooti_text = Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,pady=10,padx=10)
       
        Sprite_label = Label(F4,text="Sprite",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=3,column=0,padx=10,pady=10)
        Sprite_text = Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,pady=10,padx=10)
       
        Thumsup_label = Label(F4,text="Thumsup",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=4,column=0,padx=10,pady=10)
        Thumsup_text = Entry(F4,width=10,textvariable=self.thumsup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,pady=10,padx=10)
       
        Fanta_label = Label(F4,text="Fanta",bg=bg_color, fg="lightgreen",font=("times new roman",16,"bold")).grid(row=5,column=0,padx=10,pady=10)
        Fanta_text = Entry(F4,width=10,textvariable=self.fanta,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,pady=10,padx=10)
       
       
       
       
       
       #______________________________Billing Area_________________________
    
        
        ## -------------Billing Area Frame
        
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=990,y=183,width=360,height=380)
        
        Bill_title_label = Label(F5,text="Bill Area",fg="black",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y = Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        
        
        
        
        
        
        
        ###--------------------  Billing Menu Frame
        
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Billing Menu",font=("times new roman",15,'bold'),fg="gold",bg=bg_color)
        F6.place(x=0,y=560,relwidth=1, height=140)
        
        ##---------------------- For Rows = m 
        m1_label = Label(F6,text="Total Cosmetic Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=18,textvariable=self.cosmetic_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)
        
        m2_label = Label(F6,text="Total Grocery Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=18,textvariable=self.grocery_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_label = Label(F6,text="Total Cold Drink Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=18,textvariable=self.cold_drinks_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)


        ##-------------------------- For Columns = C
        c1_label = Label(F6,text="Cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=18,textvariable=self.cosmetic_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)
        
        c2_label = Label(F6,text="Grocery Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=18,textvariable=self.grocery_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        c3_label = Label(F6,text="Cold Drink Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=18,textvariable=self.cold_drinks_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)

        
        
        
        
        ##------------------------------- For Buttons Frames
        buton_F=Frame(F6,bd=7,relief=GROOVE)
        buton_F.place(x=740,width=590,height=105)

        Total_buton=Button(buton_F,command=self.total, text="Total",bg="cadetBlue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=0,padx=4,pady=5)
        Generate_buton=Button(buton_F,text="Generate Bill",command=self.bill_area ,bg="cadetBlue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=1,padx=4,pady=5)
        Clear_buton=Button(buton_F,text="Clear",command=self.clear_data,bg="cadetBlue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=2,padx=4,pady=5)
        Exit_buton=Button(buton_F,text="Exit",command=self.Exit_app,bg="cadetBlue",fg="white",bd=5,pady=15,width=10,font="arial 15 bold").grid(row=0,column=3,padx=4,pady=5)
        self.welcome_bill()




#________________________________________________Total Amount Logic____________________________________________________________


    def total(self):
        self.c_S_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hs_p=self.spray.get()*180
        self.c_hg_p=self.gell.get()*140
        self.c_bl_p=self.loshan.get()*180
        
#-----------------------------------Cosmetic Sum Logic-----------------------------------------
        self.total_cosmetic_price=float(
                                        self.c_S_p+
                                        self.c_fc_p+
                                        self.c_fw_p+
                                        self.c_hs_p+
                                        self.c_hg_p+
                                        self.c_bl_p
                                        )
        
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price*0.05),2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))




#-----------------------------------Grocery Sum Logic-----------------------------------------


        self.g_r_p=self.rice.get()*60
        self.g_f_p=self.food_oil.get()*180
        self.g_d_p=self.daal.get()*80
        self.g_w_p=self.wheat.get()*40
        self.g_s_p=self.sugar.get()*45
        self.g_t_p=self.tea.get()*100
        
        self.total_grocery_price=float(
                                        self.g_r_p+
                                        self.g_f_p+
                                        self.g_d_p+
                                        self.g_w_p+
                                        self.g_s_p+
                                        self.g_t_p
                                        )
        
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round((self.total_grocery_price*0.1),2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        
        
        
        
        
#-----------------------------------SOft Drinks Sum Logic-----------------------------------------
        
        
        self.d_frt_p=self.frooti.get()*75
        self.d_c_p=self.coke.get()*50
        self.d_f_p=self.fanta.get()*40
        self.d_t_p=self.thumsup.get()*45
        self.d_l_p=self.limca.get()*30
        self.d_s_p=self.sprite.get()*40
        
        self.total_drinks_price=float(
                                        self.d_frt_p+
                                        self.d_c_p+
                                        self.d_f_p+
                                        self.d_t_p+
                                        self.d_l_p+
                                        self.d_s_p
                                        )
        
        self.cold_drinks_price.set("Rs. "+str(self.total_drinks_price))
        self.d_tax=round((self.total_drinks_price*0.05),2)
        self.cold_drinks_tax.set("Rs. "+str(self.d_tax))


        self.Total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_drinks_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                              )
        
        

# __________________________________________Default Bill Area Printing Code________________________________________________________


    def welcome_bill(self):
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\tWelcome Fast Bill Retail")
            self.txtarea.insert(END,f"\n\n Bill No. : {self.bill_no.get()}")
            self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
            self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
            self.txtarea.insert(END,f"\n=======================================")
            self.txtarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
            self.txtarea.insert(END,f"\n=======================================")
            
            
            
#____________________________________Customer Details Not Entered Pop-Up Box_________________________________        
            
    def bill_area(self):
            if self.c_name.get()=="" or self.c_phone.get()=="":
                messagebox.showerror("Error","Customer Details are Must")
            elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
                messagebox.showerror("Error","No Product Purchased")
            
        
            self.welcome_bill()
            
            
#____________________________________Any Product Not Entered Error__________________________________________

#------------------------------------------Cosmetics--------------------------------------------
            if self.soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_S_p}")
                
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
                
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
            
            if self.spray.get()!=0:
                self.txtarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_hs_p}")
                
            if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gel\t\t{self.gell.get()}\t\t{self.c_hg_p}")
                
            if self.loshan.get()!=0:
                self.txtarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}")


#---------------------------------------Groceries-------------------------------------------------
            if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
                
            if self.food_oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
                
            if self.daal.get()!=0:
                self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
                
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
                
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
                
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")


#----------------------------------------------Cold Drinks--------------------------------------
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_frt_p}")
                
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\n Coke\t\t{self.coke.get()}\t\t{self.d_c_p}")
                
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}")
                
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
                
            if self.fanta.get()!=0:
                self.txtarea.insert(END,f"\n Fanta\t\t{self.fanta.get()}\t\t{self.d_f_p}")
                
            if self.thumsup.get()!=0:
                self.txtarea.insert(END,f"\n Thumsup\t\t{self.thumsup.get()}\t\t{self.d_t_p}")


# __________________________________________Product Tax Billing Area Default Printing________________________________________________________

            self.txtarea.insert(END,f"\n---------------------------------------")
            if self.cosmetic_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax\t\t\t{self.cosmetic_tax.get()}")
            
            if self.grocery_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
                
            if self.cold_drinks_tax.get()!="Rs. 0.0":
                self.txtarea.insert(END,f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")
               
            
            self.txtarea.insert(END,f"\n Total Bill :\t\t\tRs. {str(self.Total_bill)}")
            self.txtarea.insert(END,f"\n---------------------------------------")
        
            self.save_bill()

#_________________________________________Save Bill in back-End POP-UP BOX_______________________________________
    def save_bill(self):
        op=messagebox.askyesno("Save in Back-End","Do You want to Save the Bill ?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("saved",f"Bill no. {self.bill_no.get()} Saved Succesfully")
        else:
            return
    
    
#_______________________________________________Search Bill_______________________________________
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
           if i.split('.')[0]==self.search_bill.get():
               f1=open(f"bills/{i}","r")
               self.txtarea.delete('1.0',END)
               for d in f1:
                   self.txtarea.insert(END,d)
    
               f1.close()
               present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no.")
            
            
#_______________________________________Clear Button Logic_________________________________    
    
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you Really want to clear ?")    
        if op>0:
           
        
            ###================Cosmetics===================
            
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.loshan.set(0)

            
            ###==================Grocery====================
            
            self.rice.set(0)
            self.food_oil.set(0)
            self.daal.set(0)
            self.wheat.set(0)
            self.sugar.set(0)
            self.tea.set(0)


            ###=================Cold Drinks ==================
            
            
            self.limca.set(0)
            self.coke.set(0)
            self.frooti.set(0)
            self.sprite.set(0)
            self.thumsup.set(0)
            self.fanta.set(0)
            
            
            ###===================Total Product Price & Tax Variable===============
            
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drinks_price.set("")
            
            
            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")
            
            
            ###=================Customers============================
            
            self.c_name.set("")
            self.c_phone.set("")
            
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            
            self.search_bill.set("")
            self.welcome_bill()


#_________________________________________Exit Button Logic___________________________________________                
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you Really want to Exit ?")    
        if op>0:
            self.root.destroy()
            
            
root = Tk()
obj = Bill_App(root)
root.mainloop()


#____________________________________________________DEVELOPED BY PRASHANT RAI__________________________________________________________________