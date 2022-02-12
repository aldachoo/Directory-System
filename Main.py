#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""

Created on Tue Apr 20 16:08:27 2021



@author: aldachoo

"""



# -*- coding: utf-8 -*-





"""

Created on Sun Apr 11 14:44:53 2021



@author: aldachoo

"""



#!/usr/bin/env python3

# -*- coding: utf-8 -*-







from tkinter import *
import ImageTk, Image, ImageFilter

import pandas as pd

import numpy as np

import pygame

import math

from sys import exit

import sqlite3

from pandastable import Table,TableModel

import webbrowser




root = Tk()

root.title('B2')

root.geometry("1300x865")



bg = PhotoImage(file = "Taka_building.png")



#create a label 

my_label = Label(root, image=bg)

my_label.place(x=0, y=0, relwidth = 1, relheight = 1)



#add something to top of image

display_text = Label(root, text="Welcome to Takashimaya's B2 Food Directory",\

                     font = ("Helvetica", 30), bg="pink", fg="black")

display_text.pack(pady=35)



#create a frame

my_frame = Frame(root, bg="white")

my_frame.pack(pady=70)  



def add():

    top = Toplevel()

    top.title('Add eateries')

    top.geometry("1300x865")

    top.bg = PhotoImage (file = 'BGrd.png')

    label1 = Label (top, image = top.bg)

    label1.place (anchor = 'n', relx = 0.5)

    

    def add_eatery():

       nameofshop = NameofShop.get()

       cuisine = Cuisine.get()

       unitnumber = UnitNumber.get()

       price = Price.get()

       ratings = Ratings.get()

       dinein = DineIn.get()

       takeaway = Takeaway.get()

       inclusiveofGST = InclusiveofGST.get()

       

       New = []

       New.append(nameofshop)

       New.append(cuisine)

       New.append(unitnumber)

       New.append(price)

       New.append(ratings)

       New.append(dinein)

       New.append(takeaway)

       New.append(inclusiveofGST)

       

       print(New)

       

       from csv import writer

       with open('Takashimaya_B2_dataset.csv',"a") as fd:

           writer_object=writer(fd)

           writer_object.writerow(New)

           fd.close()

           

           root.destroy()

    

    NameofShopLabel = Label(top, text="Name of Shop", font = ("Helvetica", 15), bg="pink", fg="black")

    NameofShopLabel.grid(row=1, column=0,sticky="w")

    CuisineLabel = Label(top, text="Cuisine", font = ("Helvetica", 15), bg="pink", fg="black")

    CuisineLabel.grid(row=2, column=0,sticky="w")

    UnitNumberLabel = Label(top, text="Unit Number", font = ("Helvetica", 15), bg="pink", fg="black")

    UnitNumberLabel.grid(row=3, column=0,sticky="w")

    PriceLabel = Label(top, text="Price    (1:$, 2:$$, 3:$$$)", font = ("Helvetica", 15), bg="pink", fg="black")

    PriceLabel.grid(row=4, column=0,sticky="w")

    RatingsLabel = Label(top, text="Ratings   (3:3stars, 4:4stars, 5:5stars)", font = ("Helvetica", 15), bg="pink", fg="black")

    RatingsLabel.grid(row=5, column=0,sticky="w")

    DineInLabel = Label(top, text="Dinein    (yes or no)", font = ("Helvetica", 15), bg="pink", fg="black")

    DineInLabel.grid(row=6, column=0,sticky="w")

    TakeawayLabel = Label(top, text="Takeaway    (yes or no)", font = ("Helvetica", 15), bg="pink", fg="black")

    TakeawayLabel.grid(row=7, column=0,sticky="w")

    InclusiveofGSTLabel = Label(top, text="Is it inclusive of GST & Service Charge    '(yes or no)'", font = ("Helvetica", 15), bg="pink", fg="black")

    InclusiveofGSTLabel.grid(row=8, column=0,sticky="w")

    

    

    

    NameofShop = Entry(top)

    NameofShop.grid(row=1, column=1, sticky="w")

    Cuisine = Entry(top)

    Cuisine.grid(row=2, column=1, sticky="w")  

    UnitNumber = Entry(top)

    UnitNumber.grid(row=3, column=1, sticky="w")

    Price = Entry(top)

    Price.grid(row=4, column=1, sticky="w")

    Ratings = Entry(top)

    Ratings.grid(row=5, column=1, sticky="w")

    DineIn = Entry(top)

    DineIn.grid(row=6, column=1, sticky="w")

    Takeaway = Entry(top)

    Takeaway.grid(row=7, column=1, sticky="w")

    InclusiveofGST = Entry(top)

    InclusiveofGST.grid(row=8, column=1, sticky="w")

    

    

    AddEatery = Button(top, text="Enter", command=add_eatery)

    AddEatery.grid(row=8,column=2,sticky="w")

    

def login(): 

    

    if (entry2.get() == "admin" and entry3.get() == "password"):

        messagebox.showinfo("", "Login success", command=add())

    else:

        messagebox.showinfo("", "Invalid Login")

     

     

def page7():

     top7 = Toplevel()

     top7.title('Edit information')

     top7.geometry("1300x865")

     top7.bg = PhotoImage (file = 'BGrd.png')

     label1 = Label (top7, image = top7.bg)

     label1.place (anchor = 'n', relx = 0.5) 

     global entry2

     global entry3

     label2 = Label(top7, text="Username:", font=('Helvetica',12))

     entry2 = Entry(top7)
     
     label3 = Label(top7, text="Password:", font=('Helvetica',12))

     entry3 = Entry(top7, show="*")

     btn27 = Button(top7, text="Enter", font = ("Helvetica", 10), command=login)
         
     btn28 = Button(top7, text="Cancel", font = ("Helvetica", 10), command=top7.destroy).pack()

     label2.pack()

     entry2.pack()

     label3.pack()

     entry3.pack()

     btn27.pack()   

     

def start():

    

    top = Toplevel()

    top.title('Choices')

    top.geometry("1300x865")

    top.bg = PhotoImage (file = 'Taka_building.png')

    label1 = Label (top, image = top.bg)

    label1.place (anchor = 'n', relx = 0.5)

    

    top.configure(background="pink")

    my_label1 = Label(top, text="What is your criterion for choosing your food?",\

                      font = ("Helvetica", 25), bg="lightskyblue1", fg="black", \

                          pady=15).pack()

    btn1 = Button(top, text= "Store Locations", bg='light blue', \

                  font = ("Helvetica", 15), width = 15, command=page1).pack()

    btn2 = Button(top, text="Price", bg='light blue', \

                  font = ("Helvetica", 15), width = 15, command=page2).pack()

    btn3 = Button(top, text="Ratings",bg='light blue', \

                  font = ("Helvetica", 15), width = 15, command=page3).pack()

    btn4 = Button(top, text="Dine In", bg='light blue', \

                  font = ("Helvetica", 15), width = 15,command=page4).pack()

    btn5 = Button(top, text="Waiting Time", bg='light blue', \

                  font = ("Helvetica", 15), width = 15, command=page5).pack()

    btn6 = Button (top, text="Cuisine Categories", bg='light blue', \

                   font = ("Helvetica", 15), width = 15,command=page6).pack() 
        
    btn29 = Button (top, text="Links", bg='light blue', \
                   
                   font = ("Helvetica", 15), width = 15,command=page8).pack()
        

    btnc = Button(top, text="Close Window",bg='light green',\

                  font = ("Helvetica", 15), width = 15, command =top.destroy).pack()

    



#add button

btn1 = Button(my_frame, text="START", command=start, bg='yellow', \

              font = ("Helvetica", 15), width = 5)

btn1.grid(row=1, column=1, padx= 15, pady =1)

btn2 = Button(my_frame, text="ADD", command=page7, bg='yellow', \

              font = ("Helvetica", 15), width = 5)

btn2.grid(row=1, column=2, padx= 15, pady =1)

btn3 = Button(my_frame, text="EXIT", command=root.destroy, \

              bg='yellow', font = ("Helvetica", 15), width = 5)

btn3.grid(row=1, column=3, padx= 15, pady =1)





def page1():

     

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    name_of_shops = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

            

            

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    name_of_shops=pd.DataFrame([])

    name_of_shops=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    name_of_shops.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(name_of_shops)

    

    name_of_shops =pd.DataFrame(name_of_shops)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top1):

            

            top1 = Toplevel()

            top1.title('Store Locations')

            top1.geometry("1300x865")

            top1.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label (top1, image = top1.bg)

            label1.place (anchor = 'n', relx = 0.5)

            top1.configure(background="white")

            

            f = Frame(top1)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top1.table = pt = Table(f, dataframe=name_of_shops,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

    

   

  

def p_1():   

    

    #filepath = '/Users/aldachoo/Documents/CV1014/ours/Takashimaya_B2_dataset.csv'

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    #Reader = csv.reader(File)

    #data_B2 = list(Reader)

    

    list_of_prices = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    

    for i in range(0,len(data_B2)):

        if data_B2["Price"][i] == 1:

           print(data_B2["Name of Shop"][i])

           namesos.append(data_B2["Name of Shop"][i])

           pop.append(data_B2["Popular item"][i])

           unitnum.append(data_B2["Unit Number"][i])

           waiting.append(data_B2["Waiting time"][i])

           price.append(data_B2["Price"][i])

           rating.append(data_B2["Ratings"][i])

           cuisine.append(data_B2["Cuisine"][i])

           dinein.append(data_B2["Dine in"][i])

           takeaway.append(data_B2["Takeaway"][i])

           inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    list_of_prices=pd.DataFrame([])

    list_of_prices=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    list_of_prices.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(list_of_prices)

    

    list_of_prices =pd.DataFrame(list_of_prices)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_p1):

          

            top_p1 = Toplevel()

            top_p1.title('$')

            top_p1.geometry("1300x865")

            top_p1.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_p1, image = top_p1.bg)

            label1.place (anchor = 'n', relx = 0.5)

            top_p1.configure(background="white")

            

            f = Frame(top_p1)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_p1.table = pt = Table(f, dataframe=list_of_prices,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

                

def p_2():

    

    

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    list_of_prices = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    

    for i in range(0,len(data_B2)):

        if data_B2["Price"][i] == 2:

           print(data_B2["Name of Shop"][i])

           namesos.append(data_B2["Name of Shop"][i])

           pop.append(data_B2["Popular item"][i])

           unitnum.append(data_B2["Unit Number"][i])

           waiting.append(data_B2["Waiting time"][i])

           price.append(data_B2["Price"][i])

           rating.append(data_B2["Ratings"][i])

           cuisine.append(data_B2["Cuisine"][i])

           dinein.append(data_B2["Dine in"][i])

           takeaway.append(data_B2["Takeaway"][i])

           inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    list_of_prices=pd.DataFrame([])

    list_of_prices=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    list_of_prices.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(list_of_prices)

    list_of_prices =pd.DataFrame(list_of_prices)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_p2):

         

            top_p2 = Toplevel()

            top_p2.title('$$')

            top_p2.geometry("1300x865")

            top_p2.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_p2, image = top_p2.bg)

            label1.place (anchor = 'n', relx = 0.5)

            top_p2.configure(background="white")

            

            f = Frame(top_p2)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_p2.table = pt = Table(f, dataframe=list_of_prices,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

  

    

      

        

def p_3():

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    list_of_prices = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    

    for i in range(0,len(data_B2)):

        if data_B2["Price"][i] == 3:

           print(data_B2["Name of Shop"][i])

           namesos.append(data_B2["Name of Shop"][i])

           pop.append(data_B2["Popular item"][i])

           unitnum.append(data_B2["Unit Number"][i])

           waiting.append(data_B2["Waiting time"][i])

           price.append(data_B2["Price"][i])

           rating.append(data_B2["Ratings"][i])

           cuisine.append(data_B2["Cuisine"][i])

           dinein.append(data_B2["Dine in"][i])

           takeaway.append(data_B2["Takeaway"][i])

           inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    list_of_prices=pd.DataFrame([])

    list_of_prices=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    list_of_prices.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(list_of_prices)

    list_of_prices =pd.DataFrame(list_of_prices)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_p3):

            

            top_p3 = Toplevel()

            top_p3.title('$$$')

            top_p3.geometry("1300x865")

            top_p3.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_p3, image = top_p3.bg)

            label1.place (anchor = 'n', relx = 0.5)

            top_p3.configure(background="white")

            

            f = Frame(top_p3)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_p3.table = pt = Table(f, dataframe=list_of_prices,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

    

    

def page2():

    top2 = Toplevel()

    top2.title('Prices')

    top2.geometry("1300x865")

    top2.bg = PhotoImage (file = 'BGrd.png')

    label1 = Label(top2, image = top2.bg)

    label1.place (anchor = 'n', relx = 0.5)

    top2.configure(background="white")

    label_wmin = Label(top2, text= "What is your budget?:\n\
                       (With $ being the lowest and $$$ being the highest)",\

                        font = ("Helvetica", 20), bg="white", fg="black")

    label_wmin.pack()

    btn7 = Button(top2, text="$", bg='light blue', font = ("Helvetica", 15),\

                  width = 15, command= p_1).pack()

    btn8 = Button(top2, text="$$",bg='light blue', font = ("Helvetica", 15),\

                  width = 15, command= p_2).pack()

    btn9 = Button(top2, text="$$$",bg='light blue', font = ("Helvetica", 15),\

                  width = 15,command= p_3).pack()

    btnc = Button(top2, text="Close Window",bg='light green', \

           font = ("Helvetica", 15), width = 15,  command =top2.destroy).pack()    

        

def r_1():   

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    list_of_ratings = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    

    for i in range(0,len(data_B2)):

        if data_B2["Ratings"][i] == 3:

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    list_of_raings=pd.DataFrame([])

    list_of_raings=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    list_of_raings.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(list_of_raings)

    list_of_raings =pd.DataFrame(list_of_raings)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_r1):

            

            top_r1 = Toplevel()

            top_r1.title('3 Stars')

            top_r1.geometry("1300x865")

            top_r1.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_r1, image = top_r1.bg)

            label1.place (anchor = 'n', relx = 0.5)

            top_r1.configure(background="white")

            

            f = Frame(top_r1)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_r1.table = pt = Table(f, dataframe=list_of_raings,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    



def r_2():

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    list_of_ratings = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2["Ratings"][i] == 4:

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    list_of_raings=pd.DataFrame([])

    list_of_raings=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    list_of_raings.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(list_of_raings)

    list_of_raings =pd.DataFrame(list_of_raings)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_r2):

            

            top_r2 = Toplevel()

            top_r2.title('4 Stars')

            top_r2.geometry("1300x865")

            top_r2.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_r2, image = top_r2.bg)

            label1.place (anchor = 'n', relx = 0.5) 

            

            f = Frame(top_r2)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_r2.table = pt = Table(f, dataframe=list_of_raings,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

    

def r_3():

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    list_of_ratings = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2["Ratings"][i] == 5:

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    list_of_raings=pd.DataFrame([])

    list_of_raings=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    list_of_raings.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(list_of_raings)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_r3):

            

            top_r3 = Toplevel()

            top_r3.title('5 Stars')

            top_r3.geometry("1300x865")

            top_r3.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_r3, image = top_r3.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_r3)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_r3.table = pt = Table(f, dataframe=list_of_raings,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

    

def page3():

    top3 = Toplevel()

    top3.title('Ratings')

    top3.geometry("1300x865")

    top3.bg = PhotoImage (file = 'BGrd.png')

    label1 = Label(top3, image = top3.bg)

    label1.place (anchor = 'n', relx = 0.5)

    label_wmin = Label(top3, text= "Which rating satisfy your criterion?:",\

                       font = ("Helvetica", 20), bg="white", fg="black")

    label_wmin.pack()

    btn10 = Button(top3, text="3 stars",bg='light blue', \

                   font = ("Helvetica", 15), width = 15, command= r_1 ).pack()

    btn11 = Button(top3, text="4 stars",bg='light blue', \

                   font = ("Helvetica", 15), width = 15, command= r_2 ).pack()

    btn12 = Button(top3, text="5 stars",bg='light blue', \

                   font = ("Helvetica", 15),  width = 15,command= r_3 ).pack()

    btnc = Button(top3, text="Close Window",bg='light green', \

            font = ("Helvetica", 15),  width = 15,command =top3.destroy).pack()    

    

def di():

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    dine_in = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    

    for i in range(0,len(data_B2)):

        if data_B2["Dine in"][i] == "Yes":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    dine_in=pd.DataFrame([])

    dine_in=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    dine_in.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(dine_in)

    dine_in =pd.DataFrame(dine_in)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_di):

            

            top_di = Toplevel()

            top_di.title('Dine in or Takeaway')

            top_di.geometry("1300x865")  

            top_di.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_di, image = top_di.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_di)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_di.table = pt = Table(f, dataframe=dine_in,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

    

    

    

def ta():

    

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    takeaway = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    taway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Takeaway'][i] == "Yes":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            taway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    taway=pd.DataFrame(taway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    takeaway=pd.DataFrame([])

    takeaway=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,taway,inclusiveofGST],ignore_index=False,axis=1)

    takeaway.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(takeaway)

    takeaway =pd.DataFrame(takeaway)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_ta):

            

            top_ta = Toplevel()

            top_ta.title('Dine in or Takeaway')

            top_ta.geometry("1300x865")  

            top_ta.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_ta, image = top_ta.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_ta)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_ta.table = pt = Table(f, dataframe=takeaway,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

def page4():

    top4 = Toplevel()

    top4.title('Dine In')

    top4.geometry("1300x865")

    top4.bg = PhotoImage (file = 'BGrd.png')

    label1 = Label(top4, image = top4.bg)

    label1.place (anchor = 'n', relx = 0.5)

    label_wmin = Label(top4, text= "Do you wish to dine in?", \

                       font = ("Helvetica", 20), bg="white", fg="black")

    label_wmin.pack()

    btn13 = Button(top4, text="Yes", bg='light blue', \

                   font = ("Helvetica", 15), width = 15,command=di).pack()

    btn14 = Button(top4, text="No", bg='light blue', \

                   font = ("Helvetica", 15), width = 15,command=ta).pack()

    btnc = Button(top4, text="Close Window",bg='light green',\

            font = ("Helvetica", 15), width = 15,  command =top4.destroy).pack()

    

def zero_to_ten_mins():

    

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    z_to_t = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Waiting time'][i] > 0 and data_B2['Waiting time'][i] < 10 :

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    z_to_t=pd.DataFrame([])

    z_to_t=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    z_to_t.columns=["Names Of Shops","Popular item", "Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(z_to_t)

    z_to_t =pd.DataFrame(z_to_t)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_10mins):

            

            top_10mins = Toplevel()

            top_10mins.title('Waiting time below 10 mins')

            top_10mins.geometry("1300x865")

            top_10mins.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_10mins, image = top_10mins.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_10mins)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_10mins.table = pt = Table(f, dataframe=z_to_t,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

    

def ten_to_twenty_mins(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    t_to_t = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Waiting time'][i] > 10 and data_B2['Waiting time'][i] < 20 :

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    t_to_t=pd.DataFrame([])

    t_to_t=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    t_to_t.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(t_to_t)

    t_to_t =pd.DataFrame(t_to_t)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top10_20mins):

            

            top10_20mins = Toplevel()

            top10_20mins.title('Waiting time between 10 to 20 mins')

            top10_20mins.geometry("1300x865")

            top10_20mins.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top10_20mins, image = top10_20mins.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top10_20mins)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top10_20mins.table = pt = Table(f, dataframe=t_to_t,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    



def above25mins(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    t_to_tf = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Waiting time'][i] > 25:

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    t_to_tf=pd.DataFrame([])

    t_to_tf=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    t_to_tf.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(t_to_tf)

    t_to_tf =pd.DataFrame(t_to_tf)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_above25mins):

            

            top_above25mins = Toplevel()

            top_above25mins.title('Waiting time above 25mins')

            top_above25mins.geometry("1300x865")

            top_above25mins.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_above25mins, image = top_above25mins.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_above25mins)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_above25mins.table = pt = Table(f, dataframe=t_to_tf,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

  

def page5():

    top5 = Toplevel()

    top5.title('Waiting Time')

    top5.geometry("1300x865")

    top5.bg = PhotoImage (file = 'BGrd.png')

    label1 = Label(top5, image = top5.bg)

    label1.place (anchor = 'n', relx = 0.5)

    label_wmin = Label(top5, text= "How long are you willing to wait for?:",\

                       font = ("Helvetica", 20), bg="white", fg="black")

    label_wmin.pack()

    btn15 = Button(top5, text="Below 10 mins",bg='light blue',\

        font = ("Helvetica", 15), width = 15, command=zero_to_ten_mins).pack()

    btn16 = Button(top5, text="10-20 mins",bg='light blue',\

        font = ("Helvetica", 15), width = 15, command=ten_to_twenty_mins).pack()

    btn17 = Button(top5, text="Above 25mins",bg='light blue',\

        font = ("Helvetica", 15), width = 15, command=above25mins).pack()

    btnc = Button(top5, text="Close Window",bg='light green',\

        font = ("Helvetica", 15), width = 15, command =top5.destroy).pack()



def chi(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    chi = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Chinese":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(data_B2)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    chi=pd.DataFrame([])

    chi=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    chi.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(chi)

    chi =pd.DataFrame(chi)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_chi):

            

            top_chi = Toplevel()

            top_chi.title('Chinese Cuisine')

            top_chi.geometry("1300x865")

            top_chi.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_chi, image = top_chi.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_chi)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_chi.table = pt = Table(f, dataframe=chi,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

   

   

def confec(): 

    

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    confec = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Confectionery ":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    confec=pd.DataFrame([])

    confec=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    confec.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(confec)

    confec =pd.DataFrame(confec)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_confec):

            

            top_confec = Toplevel()

            top_confec.title('Confectionary')

            top_confec.geometry("1300x865")

            top_confec.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_confec, image = top_confec.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_confec)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_confec.table = pt = Table(f, dataframe=confec,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

def drinks(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    drinks = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Drinks":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    drinks=pd.DataFrame([])

    drinks=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    drinks.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(drinks)

    drinks =pd.DataFrame(drinks)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_drinks):

            

            top_drinks = Toplevel()

            top_drinks.title('Drinks')

            top_drinks.geometry("1300x865")

            top_drinks.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_drinks, image = top_drinks.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_drinks)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_drinks.table = pt = Table(f, dataframe=drinks,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

   

def european():

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    euro = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "European ":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    euro=pd.DataFrame([])

    euro=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    euro.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(euro)

    euro =pd.DataFrame(euro)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_euro):

            

            top_euro = Toplevel()

            top_euro.title('European Cuisine')

            top_euro.geometry("1300x865")

            top_euro.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_euro, image = top_euro.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_euro)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_euro.table = pt = Table(f, dataframe=euro,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

   

def grocery(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    groc = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Grocery":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    groc=pd.DataFrame([])

    groc=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    groc.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(groc)

    groc =pd.DataFrame(groc)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_gro):

            

            top_gro = Toplevel()

            top_gro.title('Grocery')

            top_gro.geometry("1300x865")

            top_gro.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_gro, image = top_gro.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_gro)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_gro.table = pt = Table(f, dataframe=groc,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()



                

def jap(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    jap = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Japanese":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    jap=pd.DataFrame([])

    jap=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    jap.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(jap)

    jap =pd.DataFrame(jap)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_jap):

            

            top_jap = Toplevel()

            top_jap.title('Japanese Cuisine')

            top_jap.geometry("1300x865")

            top_jap.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_jap, image = top_jap.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_jap)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_jap.table = pt = Table(f, dataframe=jap,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

    

def thai(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    thail = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Thai ":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    thail=pd.DataFrame([])

    thail=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    thail.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(thail)

    thail =pd.DataFrame(thail)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_thai):

            

            top_thai = Toplevel()

            top_thai.title('Thai Cuisine')

            top_thai.geometry("1300x865")

            top_thai.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_thai, image = top_thai.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_thai)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_thai.table = pt = Table(f, dataframe=thail,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

                

def western(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    wes = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Western":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    wes=pd.DataFrame([])

    wes=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    wes.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(wes)

    wes =pd.DataFrame(wes)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_wes):

            

            top_wes = Toplevel()

            top_wes.title('Western Cuisine')

            top_wes.geometry("1300x865")

            top_wes.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_wes, image = top_wes.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_wes)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_wes.table = pt = Table(f, dataframe=wes,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

   

def winery(): 

    File = pd.read_csv('Takashimaya_B2_dataset.csv')

    data_B2=pd.DataFrame(File)

    

    wine = pd.DataFrame([])

    namesos=list()

    pop=list()

    unitnum=list()

    waiting=list()

    price=list()

    rating=list()

    cuisine=list()

    dinein=list()

    takeaway=list()

    inclusiveofGST=list()

    for i in range(0,len(data_B2)):

        if data_B2['Cuisine'][i] == "Winery ":

            print(data_B2["Name of Shop"][i])

            namesos.append(data_B2["Name of Shop"][i])

            pop.append(data_B2["Popular item"][i])

            unitnum.append(data_B2["Unit Number"][i])

            waiting.append(data_B2["Waiting time"][i])

            price.append(data_B2["Price"][i])

            rating.append(data_B2["Ratings"][i])

            cuisine.append(data_B2["Cuisine"][i])

            dinein.append(data_B2["Dine in"][i])

            takeaway.append(data_B2["Takeaway"][i])

            inclusiveofGST.append(data_B2["Inclusive of GST/ Service charge"][i])

    

    print(namesos)

    namesos=pd.DataFrame(namesos)

    pop=pd.DataFrame(pop)

    unitnum=pd.DataFrame(unitnum)

    waiting=pd.DataFrame(waiting)

    price=pd.DataFrame(price)

    rating=pd.DataFrame(rating)

    cuisine=pd.DataFrame(cuisine)

    dinein=pd.DataFrame(dinein)

    takeaway=pd.DataFrame(takeaway)

    inclusiveofGST=pd.DataFrame(inclusiveofGST)

    

    wine=pd.DataFrame([])

    wine=pd.concat([namesos,pop,unitnum,waiting,price,rating,cuisine,dinein,takeaway,inclusiveofGST],ignore_index=False,axis=1)

    wine.columns=["Names Of Shops","Popular item","Unit Number", "Waiting time","Price","Ratings","Cuisine","Dine in","Takeaway","Inclusive of GST/ Service charge"]

    print(wine)

    wine =pd.DataFrame(wine)

    class TestApp(Frame):

        """Basic test frame for the table"""

        def __init__(top_wine):

            

            top_wine = Toplevel()

            top_wine.title('Winery')

            top_wine.geometry("1300x865")

            top_wine.bg = PhotoImage (file = 'BGrd.png')

            label1 = Label(top_wine, image = top_wine.bg)

            label1.place (anchor = 'n', relx = 0.5)

            

            f = Frame(top_wine)

            f.pack(fill=BOTH,expand=1)

            df = TableModel.getSampleData()

            top_wine.table = pt = Table(f, dataframe=wine,

                                    showtoolbar=True, showstatusbar=True)

            

            pt.show()

            return

    

    app = TestApp()

    #launch the app

    app.mainloop()

    

   

def page6():

    top6 = Toplevel()

    top6.title('Cuisine Categories')

    top6.geometry("1300x865")

    top6.bg = PhotoImage (file = 'BGrd.png')

    label1 = Label(top6, image = top6.bg)

    label1.place (anchor = 'n', relx = 0.5)

    label_wmin = Label(top6, text= "What type of cuisine are you looking for?:",\

                       font = ("Helvetica", 20), bg="white", fg="black")

    label_wmin.pack()    

    btn18 = Button(top6, text="Chinese", bg='light blue',\

                   font = ("Helvetica", 15), width = 15,command=chi).pack()

    btn19 = Button(top6, text="Confectionery",bg='light blue',\

                   font = ("Helvetica", 15), width = 15, command=confec).pack()

    btn20 = Button(top6, text="Drinks",bg='light blue',\

                   font = ("Helvetica", 15), width = 15, command=drinks).pack()

    btn21 = Button(top6, text="European", bg='light blue',\

                   font = ("Helvetica", 15), width = 15,command=european).pack()

    btn22 = Button(top6, text="Grocery", bg='light blue',\

                   font = ("Helvetica", 15), width = 15,command=grocery).pack()

    btn23 = Button(top6, text="Japanese",bg='light blue',\

                   font = ("Helvetica", 15), width = 15, command=jap).pack()

    btn24 = Button(top6, text="Thai", bg='light blue', \

                   font = ("Helvetica", 15), width = 15,command=thai).pack()

    btn25 = Button(top6, text="Western",bg='light blue',\

                   font = ("Helvetica", 15), width = 15, command=western).pack()

    btn26 = Button(top6, text="Winery", bg='light blue',\

                   font = ("Helvetica", 15), width = 15,command=winery).pack()

    btnc = Button(top6, text="Close Window", bg='light green',\

                   font = ("Helvetica", 15), width = 15,command =top6.destroy).pack()    

def page8():
    
    top8 = Toplevel()

    top8.title('Website Links')

    top8.geometry("1300x865")

    top8.bg = PhotoImage (file = 'BGrd.png')

    label1 = Label(top8, image = top8.bg)

    label1.place (anchor = 'n', relx = 0.5)

    label_wmin = Label(top8, text= "Click on the stores for more info",\

                       font = ("Helvetica", 15), bg="white", fg="black")

    label_wmin.pack()
    
    def callback(url):
        webbrowser.open_new(url)
    link1 = Label(top8, text="Ambush", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.ambush.com.sg/menu/"))
    link1.place(x=200, y=30)

    link2 = Label(top8, text="Asian Snacks", fg="blue", cursor="hand2")
    link2.pack()
    link2.bind("<Button-1>", lambda e: callback("https://www.instagram.com/explore/locations/847986/singapore/singapore/food-village-takashimaya/"))
    link2.place(x=400, y=30)

    link3 = Label(top8, text="Azabu Sabo", fg="blue", cursor="hand2")
    link3.pack()
    link3.bind("<Button-1>", lambda e: callback("https://www.instagram.com/explore/locations/221512286/azabu-sabo-hokkaido-ice-cream-takashimaya/?hl=en"))
    link3.place(x=600, y=30)

    link4 = Label(top8, text="Baikohken", fg="blue", cursor="hand2")
    link4.pack()
    link4.bind("<Button-1>", lambda e: callback("http://www.hawkerfood.com/baikohken-ramen-ngee-ann-city-takashimaya-shopping-centre/"))
    link4.place(x=800, y=30)

    link5 = Label(top8, text="Bankaku ", fg="blue", cursor="hand2")
    link5.pack()
    link5.bind("<Button-1>", lambda e: callback("https://bankaku.com.sg/product/"))
    link5.place(x=1000, y=30)
    
    link6 = Label(top8, text="Bee Cheng Hiang", fg="blue", cursor="hand2")
    link6.pack()
    link6.bind("<Button-1>", lambda e: callback("https://www.beechenghiang.com.sg/grillery/bistro.html"))
    link6.place(x=200, y=80)

    link7 = Label(top8, text="Bengawansolo", fg="blue", cursor="hand2")
    link7.pack()
    link7.bind("<Button-1>", lambda e: callback("http://www.bengawansolo.com.sg/category.aspx"))
    link7.place(x=400, y=80)

    link8 = Label(top8, text="Boost Juice", fg="blue", cursor="hand2")
    link8.pack()
    link8.bind("<Button-1>", lambda e: callback("https://www.boostjuicebars.com.sg/drinks/"))
    link8.place(x=600, y=80)

    link9 = Label(top8, text="Butter Studio ", fg="blue", cursor="hand2")
    link9.pack()
    link9.bind("<Button-1>", lambda e: callback("https://order.thebutterstudio.com/en_SG/"))
    link9.place(x=800, y=80)
    
    link10 = Label(top8, text="Cold Storage", fg="blue", cursor="hand2")
    link10.pack()
    link10.bind("<Button-1>", lambda e: callback("https://coldstorage.com.sg/"))
    link10.place(x=1000, y=80)

    link11 = Label(top8, text="Cookie Mixx", fg="blue", cursor="hand2")
    link11.pack()
    link11.bind("<Button-1>", lambda e: callback("https://www.cookiemixx.com.sg/"))
    link11.place(x=200, y=130)

    link12 = Label(top8, text="DONQ", fg="blue", cursor="hand2")
    link12.pack()
    link12.bind("<Button-1>", lambda e: callback("https://www.facebook.com/donqbakery/"))
    link12.place(x=400, y=130)

    link13 = Label(top8, text="Dragon Brand Bird's Nest", fg="blue", cursor="hand2")
    link13.pack()
    link13.bind("<Button-1>", lambda e: callback("https://dragonbrand.com.sg/"))
    link13.place(x=600, y=130)

    link14 = Label(top8, text="Enoteca Wine", fg="blue", cursor="hand2")
    link14.pack()
    link14.bind("<Button-1>", lambda e: callback("https://www.instagram.com/enoteca_singapore/?hl=en"))
    link14.place(x=800, y=130)

    link15 = Label(top8, text="Fauchon", fg="blue", cursor="hand2")
    link15.pack()
    link15.bind("<Button-1>", lambda e: callback("https://www.fauchon.com/en/"))
    link15.place(x=1000, y=130)

    link16 = Label(top8, text="Fukujuen ", fg="blue", cursor="hand2")
    link16.pack()
    link16.bind("<Button-1>", lambda e: callback("https://www.fukujuen.com/en/"))
    link16.place(x=200, y=180)

    link17 = Label(top8, text="GODIVA", fg="blue", cursor="hand2")
    link17.pack()
    link17.bind("<Button-1>", lambda e: callback("https://www.godiva.com.sg/"))
    link17.place(x=400, y=180)

    link18 = Label(top8, text="Gourmet Grocery by Ourchoice", fg="blue", cursor="hand2")
    link18.pack()
    link18.bind("<Button-1>", lambda e: callback("https://www.ourchoice.com/"))
    link18.place(x=600, y=180)

    link19 = Label(top8, text="Harrods ", fg="blue", cursor="hand2")
    link19.pack()
    link19.bind("<Button-1>", lambda e: callback("https://www.harrods.com/en-sg/shopping/harrods/food-wine-tea-loose-leaf-tea"))
    link19.place(x=800, y=180)

    link20 = Label(top8, text="Honey Farm ", fg="blue", cursor="hand2")
    link20.pack()
    link20.bind("<Button-1>", lambda e: callback("https://www.honeyfarm.com.sg/?v=0f177369a3b7"))
    link20.place(x=1000, y=180)

    link21 = Label(top8, text="Japanese Snacks", fg="blue", cursor="hand2")
    link21.pack()
    link21.bind("<Button-1>", lambda e: callback("https://www.google.com/search?q=japanese%20snacks%20store&rlz=1C1CHZN_enSG924SG924&biw=1536&bih=703&sxsrf=ALeKk00wlGGNl-GY8Im8sVgQjlOypdM2AQ:1619161976755&ei=WHOCYJPgLYnYz7sPgZ28uA0&oq=japanese+snacks+store&gs_lcp=Cgdnd3Mtd2l6EAMyBAgjECcyBAgjECcyBAgAEEMyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCCMQsAMQJzoHCAAQRxCwA1CVIliVImCjJWgBcAJ4AIABiQGIAcABkgEDMS4xmAEAoAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz&ved=2ahUKEwjM39Sz6JPwAhUm8HMBHdsuA9sQvS4wAnoECAgQSg&uact=5&tbs=lf:1,lf_ui:10&tbm=lcl&rflfq=1&num=10&rldimm=16589470856311184891&lqi=ChVqYXBhbmVzZSBzbmFja3Mgc3RvcmVI7s-x1o-vgIAIWj4KFWphcGFuZXNlIHNuYWNrcyBzdG9yZRAAEAEQAhgAGAEiFWphcGFuZXNlIHNuYWNrcyBzdG9yZSoECAMQApIBCXNuYWNrX2JhcpoBJENoZERTVWhOTUc5blMwVkpRMEZuU1VSVmIxbHlUM3BSUlJBQqoBGwoLL20vMDExODZmZmYQASoKIgZzbmFja3MoAA&phdesc=_jpo2ToYXHM&rlst=f#rlfi=hd:;si:16589470856311184891,l,ChVqYXBhbmVzZSBzbmFja3Mgc3RvcmVI7s-x1o-vgIAIWj4KFWphcGFuZXNlIHNuYWNrcyBzdG9yZRAAEAEQAhgAGAEiFWphcGFuZXNlIHNuYWNrcyBzdG9yZSoECAMQApIBCXNuYWNrX2JhcpoBJENoZERTVWhOTUc5blMwVkpRMEZuU1VSVmIxbHlUM3BSUlJBQqoBGwoLL20vMDExODZmZmYQASoKIgZzbmFja3MoAA,y,_jpo2ToYXHM;mv:[[1.5402448,103.955922],[1.2707732999999999,103.73070279999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!1m4!1u2!2m2!2m1!1e1!2m1!1e2!2m1!1e3!3sIAE,lf:1,lf_ui:10"))
    link21.place(x=200, y=230)

    link22 = Label(top8, text="Juchheim Baumkuchen", fg="blue", cursor="hand2")
    link22.pack()
    link22.bind("<Button-1>", lambda e: callback("https://www.facebook.com/juchheimsingapore/"))
    link22.place(x=400, y=230)

    link23 = Label(top8, text="Kimukatsu", fg="blue", cursor="hand2")
    link23.pack()
    link23.bind("<Button-1>", lambda e: callback("https://www.instagram.com/kimukatsusg/?hl=en"))
    link23.place(x=600, y=230)

    link24 = Label(top8, text="Kobe Fugetsudo ", fg="blue", cursor="hand2")
    link24.pack()
    link24.bind("<Button-1>", lambda e: callback("https://www.takashimaya.com.sg/post_store/kobe-fugetsudo/"))
    link24.place(x=800, y=230)

    link25 = Label(top8, text="Kyoho-ya", fg="blue", cursor="hand2")
    link25.pack()
    link25.bind("<Button-1>", lambda e: callback("https://www.kyoho.com.sg/"))
    link25.place(x=1000, y=230)

    link26 = Label(top8, text="Laderach", fg="blue", cursor="hand2")
    link26.pack()
    link26.bind("<Button-1>", lambda e: callback("https://www.laderach.com.sg/shop/"))
    link26.place(x=200, y=280)

    link27 = Label(top8, text="Leroy Wine ", fg="blue", cursor="hand2")
    link27.pack()
    link27.bind("<Button-1>", lambda e: callback("https://www.millesima.sg/producer-leroy.html"))
    link27.place(x=400, y=280)

    link28 = Label(top8, text="Mankaso ", fg="blue", cursor="hand2")
    link28.pack()
    link28.bind("<Button-1>", lambda e: callback("http://www.mankaso.co.jp/"))
    link28.place(x=600, y=280)

    link29 = Label(top8, text="Mignon's Steak & Grill ", fg="blue", cursor="hand2")
    link29.pack()
    link29.bind("<Button-1>", lambda e: callback("https://www.quandoo.sg/place/mignons-steak-and-grill-71019/menu"))
    link29.place(x=800, y=280)

    link30 = Label(top8, text="Minamoto Kitchoan ", fg="blue", cursor="hand2")
    link30.pack()
    link30.bind("<Button-1>", lambda e: callback("https://www.kitchoan.com/"))
    link30.place(x=1000, y=280)

    link31 = Label(top8, text="Mini One", fg="blue", cursor="hand2")
    link31.pack()
    link31.bind("<Button-1>", lambda e: callback("https://www.instagram.com/explore/locations/298042555/takashimaya-mini-one/?hl=en"))
    link31.place(x=200, y=330)

    link32 = Label(top8, text="Nakajima Suisan (Sushi & Fish)", fg="blue", cursor="hand2")
    link32.pack()
    link32.bind("<Button-1>", lambda e: callback("https://www.facebook.com/pages/Nakajima-Suisan-Grilled-Fish/193230334046252"))
    link32.place(x=400, y=330)

    link33 = Label(top8, text="Nakajima Suisan Grilled Fish ", fg="blue", cursor="hand2")
    link33.pack()
    link33.bind("<Button-1>", lambda e: callback("https://www.facebook.com/pages/Nakajima-Suisan-Grilled-Fish/193230334046252"))
    link33.place(x=600, y=330)

    link34 = Label(top8, text="NamNam ", fg="blue", cursor="hand2")
    link34.pack()
    link34.bind("<Button-1>", lambda e: callback("https://namnam.net/menus/singapore-menu/"))
    link34.place(x=800, y=330)

    link35 = Label(top8, text="Nuts & Nibble", fg="blue", cursor="hand2")
    link35.pack()
    link35.bind("<Button-1>", lambda e: callback("https://www.facebook.com/pages/category/Food---Beverage-Company/Nuts-Nibbles-300733806719075/"))
    link35.place(x=1000, y=330)

    link36 = Label(top8, text="Peck ", fg="blue", cursor="hand2")
    link36.pack()
    link36.bind("<Button-1>", lambda e: callback("https://www.peck.it/en/where-we-are/singapore"))
    link36.place(x=200, y=380)

    link37 = Label(top8, text="Royce", fg="blue", cursor="hand2")
    link37.pack()
    link37.bind("<Button-1>", lambda e: callback("https://royce.com.sg/products.php"))
    link37.place(x=400, y=380)

    link38 = Label(top8, text="Ryugetsu ", fg="blue", cursor="hand2")
    link38.pack()
    link38.bind("<Button-1>", lambda e: callback("https://www.takashimaya.com.sg/post_recommendations/top-5-japanese-snacks-love/"))
    link38.place(x=600, y=380)

    link39 = Label(top8, text="Shiseido Parlour ", fg="blue", cursor="hand2")
    link39.pack()
    link39.bind("<Button-1>", lambda e: callback("https://parlour.shiseido.co.jp/en/shoplist/singaporetakashimaya/"))
    link39.place(x=800, y=380)

    link40 = Label(top8, text="Sinpopo", fg="blue", cursor="hand2")
    link40.pack()
    link40.bind("<Button-1>", lambda e: callback("https://www.sinpopo.com/content/restaurant.html"))
    link40.place(x=1000, y=380)

    link41 = Label(top8, text="Spa Foods", fg="blue", cursor="hand2")
    link41.pack()
    link41.bind("<Button-1>", lambda e: callback("https://spafoods.com.sg/shop/index.php?main_page=index&zenid=1mnrmc2nn1q456bashin3666t7"))
    link41.place(x=200, y=430)

    link42 = Label(top8, text="St Leaven Bakery", fg="blue", cursor="hand2")
    link42.pack()
    link42.bind("<Button-1>", lambda e: callback("https://sg.openrice.com/en/singapore/r-st-leaven-orchard-r16129"))
    link42.place(x=400, y=430)

    link43 = Label(top8, text="Sugi Bee Garden ", fg="blue", cursor="hand2")
    link43.pack()
    link43.bind("<Button-1>", lambda e: callback("https://www.facebook.com/sugibeesgp/"))
    link43.place(x=600, y=430)

    link44 = Label(top8, text="Tai Cheong Bakery ", fg="blue", cursor="hand2")
    link44.pack()
    link44.bind("<Button-1>", lambda e: callback("https://www.taicheong.com.sg/"))
    link44.place(x=800, y=430)

    link45 = Label(top8, text="Thye Shan Medical Hall", fg="blue", cursor="hand2")
    link45.pack()
    link45.bind("<Button-1>", lambda e: callback("https://thyeshan.com/"))
    link45.place(x=1000, y=430)
    
    link46 = Label(top8, text="Tian Yuan Xiang", fg="blue", cursor="hand2")
    link46.pack()
    link46.bind("<Button-1>", lambda e: callback("https://www.qchicken.com.sg/"))
    link46.place(x=200, y=480)
    
    link47 = Label(top8, text="Tsuru-Koshi Udon", fg="blue", cursor="hand2")
    link47.pack()
    link47.bind("<Button-1>", lambda e: callback("https://www.facebook.com/tsurukoshi.sg/"))
    link47.place(x=400, y=480)
    
    link48 = Label(top8, text="TWG Tea", fg="blue", cursor="hand2")
    link48.pack()
    link48.bind("<Button-1>", lambda e: callback("https://twgtea.com/Files/Images/TWG-Menu/[WEB]%20TWG%20Tea%20[SG]%20-%20MBS%20Bay&Garden_ION%20Orchard_Takashimaya_Swissotel.pdf"))
    link48.place(x=600, y=480)
    
    link49 = Label(top8, text="Venchi", fg="blue", cursor="hand2")
    link49.pack()
    link49.bind("<Button-1>", lambda e: callback("https://venchi.sg/?utm_source=google&utm_medium=cpc&utm_campaign=Venchi%20SG%20%2F%20Search%20%2F%20Brand&utm_content=Brand&utm_term=%2Bvenchi%20singapore&gclid=Cj0KCQjwvYSEBhDjARIsAJMn0li2_ARpSGxulUplKMWu2SUSa8lMHCkMmZ-ZcYYVQxAJ-QkWzJM92H4aAmX2EALw_wcB"))
    link49.place(x=800, y=480)
    
    link50 = Label(top8, text="Xndo", fg="blue", cursor="hand2")
    link50.pack()
    link50.bind("<Button-1>", lambda e: callback("https://www.xndo.com/"))
    link50.place(x=1000, y=480)
    
    link51 = Label(top8, text="Yakun", fg="blue", cursor="hand2")
    link51.pack()
    link51.bind("<Button-1>", lambda e: callback("http://yakun.com/"))
    link51.place(x=200, y=530)
    
    link52 = Label(top8, text="Yi Kou Wei ", fg="blue", cursor="hand2")
    link52.pack()
    link52.bind("<Button-1>", lambda e: callback("http://www.yikowei.com.sg/restaurant.html"))
    link52.place(x=400, y=530)
    
    link53 = Label(top8, text="Yonehachi ", fg="blue", cursor="hand2")
    link53.pack()
    link53.bind("<Button-1>", lambda e: callback("https://www.facebook.com/yonehachisg/"))
    link53.place(x=600, y=530)
    
    

root.mainloop()
