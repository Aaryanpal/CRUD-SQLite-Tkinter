import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


def button_function():
    print("button pressed")

def change_screen_size(new_scaling: str):
    new_scaling_float = int(new_scaling.replace("%", "")) / 100
    customtkinter.set_widget_scaling(new_scaling_float)
    print("Scaling button pressed", str)

def change_background_mode(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)
    print("Appearance pressed", str)


app = customtkinter.CTk()
app.title("Subscription Management System")
w = 800
h = 650

ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()


x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

app.geometry('%dx%d+%d+%d' % (w, h, x, y))

# configure grid layout (4x4)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure((0, 1, 2), weight=1)

# create sidebar frame with widgets
app.sidebar_frame = customtkinter.CTkFrame(app, width=140, corner_radius=0)
app.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
app.sidebar_frame.grid_rowconfigure(4, weight=1)
app.logo_label = customtkinter.CTkLabel(app.sidebar_frame, text="Subsify", font=customtkinter.CTkFont(size=20, weight="bold"))
app.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
app.appearance_mode_label = customtkinter.CTkLabel(app.sidebar_frame, text="Appearance Mode:", anchor="w")
app.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
app.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(app.sidebar_frame, values=["System","Light", "Dark"],
                                                            command=change_background_mode)
app.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
app.scaling_label = customtkinter.CTkLabel(app.sidebar_frame, text="UI Scaling:", anchor="w")
app.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
app.scaling_optionemenu = customtkinter.CTkOptionMenu(app.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=change_screen_size)
app.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

# variables used in code
title = ""
name = ""
dob = ""
gender = ""
registration_number = ""
start_of_subscription = ""
end_of_subscription = ""
city = ""
district = ""
state = ""
address = ""
address_two = ""
mobile_number = ""
whatsapp_number = ""
email_address = ""

# create Centerframe with widgets
center_frame = customtkinter.CTkFrame(app, width=100)
center_frame.grid(row=0, column=0, columnspan=4, sticky="nsew",padx=(200,25), pady = 0)
# Title
title = customtkinter.CTkOptionMenu(center_frame, dynamic_resizing=False,values=["Adv", "CA", "CFA", "Mr.", "Mrs.", "M/s"])
title.grid(row=0, column=0, padx=20, pady=(20, 10))
title.set("Title")
# Name
lblName = customtkinter.CTkLabel(center_frame, text="Name", font=customtkinter.CTkFont(size=18, weight="bold"))
lblName.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")
txtName = customtkinter.CTkEntry(center_frame, textvariable=name, placeholder_text="Name")
txtName.grid(row=0, column=2, padx=20, pady=(20, 10))

# DoB
lblDob = customtkinter.CTkLabel(center_frame, text="Date Of Birth", font=customtkinter.CTkFont(size=18, weight="bold"))
lblDob.grid(row=0, column=3, padx=20, pady=(20, 10), sticky="w")
txtDob = customtkinter.CTkEntry(center_frame, textvariable=dob, placeholder_text="Date Of Birth")
txtDob.grid(row=0, column=4, padx=20, pady=(20, 10))
# Gender
# Gender Label code is commented
# lblgender = customtkinter.CTkLabel(center_frame, text="Gender", font=customtkinter.CTkFont(size=18, weight="bold"))
# lblgender.grid(row=0, column=5, padx=20, pady=(20, 10))
optgender = customtkinter.CTkOptionMenu(center_frame, dynamic_resizing=False,values=["Male","Female","Others"])
optgender.grid(row=0, column=5, padx=20, pady=(20, 10), sticky="nsew")
optgender.set("Gender")

#Email
lblEmail = customtkinter.CTkLabel(center_frame, text="Email", font=customtkinter.CTkFont(size=18, weight="bold"))
lblEmail.grid(row=0, column=7, padx=20, pady=(20, 10), sticky="w")
txtEmail = customtkinter.CTkEntry(center_frame, textvariable=email_address, placeholder_text="Email Address")
txtEmail.grid(row=0, column=8, padx=20, pady=(20, 10))

#Registration Number
lblRegistration = customtkinter.CTkLabel(center_frame, text="Registration Number", font=customtkinter.CTkFont(size=18, weight="bold"))
lblRegistration.grid(row=1, column=0, padx=20, pady=(20, 10), sticky="w")
txtRegistration = customtkinter.CTkEntry(center_frame, textvariable=registration_number, placeholder_text="Registration Number")
txtRegistration.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#Start Of Subscription Number
lblSubscription = customtkinter.CTkLabel(center_frame, text="Start of Subscription", font=customtkinter.CTkFont(size=18, weight="bold"))
lblSubscription.grid(row=1, column=3, padx=20, pady=(20, 10), sticky="w")
txtSubscription = customtkinter.CTkEntry(center_frame, textvariable=start_of_subscription, placeholder_text="Start of Subscription")
txtSubscription.grid(row=1, column=4, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#End Of Subscription Number
lblESubscription = customtkinter.CTkLabel(center_frame, text="End of Subscription", font=customtkinter.CTkFont(size=18, weight="bold"))
lblESubscription.grid(row=1, column=7, padx=20, pady=(20, 10))
txtESubscription = customtkinter.CTkEntry(center_frame, textvariable=end_of_subscription, placeholder_text="End of Subscription")
txtESubscription.grid(row=1, column=8, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#State
lblState = customtkinter.CTkLabel(center_frame, text="State", font=customtkinter.CTkFont(size=18, weight="bold"))
lblState.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")
txtState = customtkinter.CTkEntry(center_frame, textvariable=state, placeholder_text="State")
txtState.grid(row=2, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

#District
lblDistrict = customtkinter.CTkLabel(center_frame, text="District", font=customtkinter.CTkFont(size=18, weight="bold"))
lblDistrict.grid(row=2, column=2, padx=20, pady=(20, 10), sticky="nsew")
txtDistrict = customtkinter.CTkEntry(center_frame, textvariable=district, placeholder_text="District")
txtDistrict.grid(row=2, column=3, padx=(20, 0), pady=(20, 20), sticky="nsew")

#City
lblCity = customtkinter.CTkLabel(center_frame, text="City", font=customtkinter.CTkFont(size=18, weight="bold"))
lblCity.grid(row=2, column=4, padx=20, pady=(20, 10), sticky="w")
txtCity = customtkinter.CTkEntry(center_frame, textvariable=city, placeholder_text="City")
txtCity.grid(row=2, column=5, padx=(20, 0), pady=(20, 20), sticky="nsew")

#Address 1
lblAddress = customtkinter.CTkLabel(center_frame, text="Address", font=customtkinter.CTkFont(size=18, weight="bold"))
lblAddress.grid(row=3, column=0, padx=20, pady=(20, 10), sticky="w")
txtAddress = customtkinter.CTkTextbox(center_frame, width=50, height=25)
txtAddress.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#Address 2
lblAddress = customtkinter.CTkLabel(center_frame, text="Address 2", font=customtkinter.CTkFont(size=18, weight="bold"))
lblAddress.grid(row=3, column=3, padx=20, pady=(20, 10), sticky="w")
txtAddress = customtkinter.CTkTextbox(center_frame, width=50, height=25)
txtAddress.grid(row=3, column=4, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#Mobile Number
lblMob = customtkinter.CTkLabel(center_frame, text="Mobile Number", font=customtkinter.CTkFont(size=18, weight="bold"))
lblMob.grid(row=4, column=0, padx=20, pady=(20, 10), sticky="w")
txtMob = customtkinter.CTkEntry(center_frame, textvariable=city, placeholder_text="Mobile Number")
txtMob.grid(row=4, column=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

#WhatsApp Number
lblWnumber = customtkinter.CTkLabel(center_frame, text="WhatsApp Number", font=customtkinter.CTkFont(size=18, weight="bold"))
lblWnumber.grid(row=4, column=2, padx=20, pady=(20, 10), sticky="w")
txtWnumber = customtkinter.CTkEntry(center_frame, textvariable=city, placeholder_text="WhatsApp Number")
txtWnumber.grid(row=4, column=3, padx=(20, 0), pady=(20, 20), sticky="nsew")

btn_frame = customtkinter.CTkFrame(center_frame, fg_color="#2d3436")
btn_frame.grid(row=5, column=1, columnspan=5, sticky="nsew", pady=(100, 0) )

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



btnExport=customtkinter.CTkButton(btn_frame, text="Export", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=exportData)
btnExport.grid(row=0, column=4, padx=20, pady=10)

btnSub=customtkinter.CTkButton(btn_frame, text="Insert", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=addData)
btnSub.grid(row=0, column=0, padx=20, pady=10)

btnUp=customtkinter.CTkButton(btn_frame, text="Update", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=updateData)
btnUp.grid(row=0, column=1, padx=20, pady=10)

btnDel=customtkinter.CTkButton(btn_frame, text="Delete", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=deleteData)
btnDel.grid(row=0, column=2, padx=20, pady=10)

btnClr=customtkinter.CTkButton(btn_frame, text="Clear",fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=clearData)
btnClr.grid(row=0, column=3, padx=20, pady=10)




app.mainloop()