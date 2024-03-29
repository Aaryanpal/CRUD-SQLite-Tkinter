from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from database import *
import openpyxl

db=Database("SqliteDatabase.db")

window=Tk()
window.title("Subscription Management System")
w = 800 
h = 650 

ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
title = StringVar() 
name = StringVar()
gender = StringVar()
registration_number = StringVar()
start_of_subscription = StringVar()
duration = StringVar()
end_of_subscription = StringVar()
city = StringVar()
districts = StringVar()
state = StringVar()
address = StringVar()
address_two = StringVar()
mobile_number = StringVar()
whatsapp_number = StringVar()
email_address = StringVar()

frame1=Frame(window,padx=10,pady=10,bg="#636e72")
frame1.pack(side=TOP,fill=X)


lblName=Label(frame1,text="Name",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblName.grid(row=1,column=0)
cb2=ttk.Combobox(frame1,width=15,textvariable=title,state="readonly",font=("times",16))
cb2['values']=("Adv", "CA", "CFA", "Mr.", "Mrs.", "M/s")
cb2.grid(row=1,column=1)
txtName=Entry(frame1,textvariable=name,font=("times",16),width=10)
txtName.grid(row=1,column=2)

lblgen=Label(frame1,text="Gender",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblgen.grid(row=1,column=4)
cb=ttk.Combobox(frame1,width=10,textvariable=gender,state="readonly",font=("times",16))
cb['values']=("Male","Female","Others")
cb.grid(row=1,column=5)

lblRegistration = Label(frame1,text="Registraion Number",bg="#636e72",fg="white",font=("times",16,"bold"),pady=5)
lblRegistration.grid(row=2,column=0)
txtRegistration = Entry(frame1,font=("times",16),width=15,textvariable=registration_number)
txtRegistration.grid(row=2,column=1)

lblSubscription = Label(frame1,text="Start of Subscription",bg="#636e72",fg="white",font=("times",16,"bold"),pady=1)
lblSubscription.grid(row=3,column=0)
txtSubscription = Entry(frame1,font=("times",16),width=15,textvariable=start_of_subscription)
txtSubscription.grid(row=3,column=1)

lblDuration = Label(frame1,text="Duration",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblDuration.grid(row=3,column=3)
txtDuration = Entry(frame1,font=("times",16),width=10,textvariable=duration)
txtDuration.grid(row=3,column=4)

lblESubscription = Label(frame1,text="End of Subscription",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblESubscription.grid(row=4,column=0)
txtESubscription = Entry(frame1,font=("times",16),width=15,textvariable=end_of_subscription)
txtESubscription.grid(row=4,column=1)

lblCity = Label(frame1,text="City",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblCity.grid(row=5,column=0)
txtCity = Entry(frame1,font=("times",16),width=15,textvariable=city)
txtCity.grid(row=5,column=1)

lblDistrict = Label(frame1,text="District",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblDistrict.grid(row=5,column=2)
txtDistrict = Entry(frame1,font=("times",16),width=15,textvariable=districts)
txtDistrict.grid(row=5,column=3)

lblState = Label(frame1,text="State",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblState.grid(row=5,column=4)
txtState = Entry(frame1,font=("times",16),width=15,textvariable=state)
txtState.grid(row=5,column=5)

lblAdd=Label(frame1,text="Address",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblAdd.grid(row=6,column=0)
txtAdd=Entry(frame1,font=("times",16),width=15,textvariable=address)
txtAdd.grid(row=6,column=1)


lblAdd2=Label(frame1,text="Address 2 (Optional)",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblAdd2.grid(row=6,column=2)
txtAdd2=Entry(frame1,font=("times",16),width=15,textvariable=address_two)
txtAdd2.grid(row=6,column=3)

lblMob=Label(frame1,text="Mobile Number",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblMob.grid(row=7,column=0)
txtMob=Entry(frame1,font=("times",16),textvariable=mobile_number,width=15)
txtMob.grid(row=7,column=1)

lblWnumber=Label(frame1,text="WhatsApp Number",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblWnumber.grid(row=8,column=0)
txtWnumber=Entry(frame1,font=("times",16),textvariable=whatsapp_number,width=15)
txtWnumber.grid(row=8,column=1)

lblEmail=Label(frame1,text="Email Address",bg="#636e72",fg="white",font=("times",16,"bold"),pady=10)
lblEmail.grid(row=9,column=0)
txtEmail=Entry(frame1,font=("times",16),textvariable=email_address,width=15)
txtEmail.grid(row=9,column=1)

btn_frame=Frame(frame1,bg="#2d3436")
btn_frame.grid(row=10,column=1,columnspan=4)

def fetchData():
    table.delete(*table.get_children())
    count=0
    for row in db.fetch_record():
        count+=1
        print("IN FetchData=>>", row)
        table.insert("",END,values=(count, row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))
def addData():
    if txtName.get()=="" or txtAdd.get()=="" or txtMob.get()=="" or txtEmail.get()=="":
        messagebox.showinfo("Message","Please Fill All Records")
    else:
        db.insert(cb2.get(), txtName.get(), cb.get(), txtRegistration.get(), txtSubscription.get(), txtDuration.get(), txtESubscription.get(), txtCity.get(), txtDistrict.get(), txtState.get(), txtAdd.get(), txtAdd2.get(), txtMob.get(), txtWnumber.get(), txtEmail.get())
        fetchData()
        clearData()
        messagebox.showinfo("Message","Record Insert Successfully")

def getrecord(event):
    srow = table.focus()
    data = table.item(srow)
    global row
    row = data['values']
    print("IN GETRECORD=>>", row)
    title.set(row[2])
    name.set(row[3])
    gender.set(row[4])
    registration_number.set(row[5])
    start_of_subscription.set(row[6])
    duration.set(row[7])
    end_of_subscription.set(row[8])
    city.set(row[9])
    districts.set(row[10])
    state.set(row[11])
    address.set(row[12])
    address_two.set(row[13])
    mobile_number.set(row[14])
    whatsapp_number.set(row[15])
    email_address.set(row[16])

def updateData():
    if cb2.get() == "" or txtName.get() == "" or txtAdd.get() == "" or cb.get() == "" or txtMob.get() == "" or txtEmail.get() == "":
        messagebox.showinfo("Message", "Please Fill All Records")
    else:
        db.update_record(cb2.get(), txtName.get(), cb.get(), txtRegistration.get(), txtSubscription.get(), txtDuration.get(), txtESubscription.get(), txtCity.get(), txtDistrict.get(), txtState.get(), txtAdd.get(), txtAdd2.get(), txtMob.get(), txtWnumber.get(), txtEmail.get(), (row[1]))
        fetchData()
        clearData()
        messagebox.showinfo("Message", "Record Update Successfully")

def deleteData():
    db.remove_record(row[1])
    fetchData()
    clearData()
    messagebox.showinfo("Message", "Record Delete Successfully")

def clearData():
    cb2.set("")
    name.set("") 
    gender.set("") 
    registration_number.set("") 
    start_of_subscription.set("") 
    duration.set("") 
    end_of_subscription.set("") 
    city.set("") 
    districts.set("") 
    state.set("") 
    address.set("") 
    address_two.set("") 
    mobile_number.set("") 
    whatsapp_number.set("") 
    email_address.set("")

def exportData():
    # Get all the data from the Treeview
    data = []
    for row in table.get_children():
        data.append([table.item(row)["values"][i] for i in range(len(table["columns"]))])
    
    # Ask the user to choose the location to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    
    # If the user cancels the operation, return
    if not file_path:
        return
    
    # Create a new workbook and select the active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active
    
    # Add headers to the first row
    headers = ["S.NO", "ID", "TITLE", "NAME", "AGE", "GENDER", "REGISTRATION NUMBER", "START OF SUBSCRIPTION", "DURATION",
               "END OF SUBSCRIPTION", "CITY", "DISTRICTS", "STATE", "ADDRESS", "ADDRESS TWO", "MOBILE NUMBER",
               "WHATSAPP NUMBER", "EMAIL ADDRESS"]
    ws.append(headers)
    
    # Append data to the worksheet
    for row in data:
        ws.append(row)
    
    # Save the workbook to the chosen location
    wb.save(file_path)
    messagebox.showinfo("Export", f"Data has been exported to {file_path}")

btnExport=Button(btn_frame,text="Export",bg="#1289A7",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=exportData)
btnExport.grid(row=0,column=4)

btnSub=Button(btn_frame,text="Insert",bg="#01a3a4",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=addData)
btnSub.grid(row=0,column=0)

btnUp=Button(btn_frame,text="Update",bg="#F79F1F",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=updateData)
btnUp.grid(row=0,column=1)

btnDel=Button(btn_frame,text="Delete",bg="#ee5253",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=deleteData)
btnDel.grid(row=0,column=2)

btnClr=Button(btn_frame,text="Clear",bg="#1289A7",fg="white",width=6,padx=20,pady=5,font=("times",16,"bold"),command=clearData)
btnClr.grid(row=0,column=3)


myFrame=Frame(window)
myFrame.place(x=0,y=425,width=1920,height=500)

style=ttk.Style()
style.configure("Treeview",font=("times",15),rowheight=35)
style.configure("Treeview.Heading",font=("times",16,"bold"))

table = ttk.Treeview(myFrame, columns=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16))

table.column("0", anchor=CENTER)
table.column("1", stretch=NO, width=0)
table.column("4", anchor=CENTER)
table.column("11", anchor=CENTER)

table.heading("0", text="S.NO")
table.heading("1", text="ID")
table.heading("2", text="TITLE")
table.heading("3", text="NAME")
table.heading("4", text="GENDER")
table.heading("5", text="REGISTRATION NUMBER")
table.heading("6", text="START OF SUBSCRIPTION")
table.heading("7", text="DURATION")
table.heading("8", text="END OF SUBSCRIPTION")
table.heading("9", text="CITY")
table.heading("10", text="DISTRICTS")
table.heading("11", text="STATE")
table.heading("12", text="ADDRESS")
table.heading("13", text="ADDRESS TWO")
table.heading("14", text="MOBILE NUMBER")
table.heading("15", text="WHATSAPP NUMBER")
table.heading("16", text="EMAIL ADDRESS")

table["show"]='headings'
table.bind("<ButtonRelease-1>",getrecord)
table.pack(fill=X)

fetchData()

window.mainloop()
