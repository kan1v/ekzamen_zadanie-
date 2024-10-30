from tkinter import *
import sqlite3

window = Tk()
window.geometry("1130x500+200+200")
window.title("My first prog")

##############################
def loadBase():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute("SELECT* FROM CategoriesCosts")
    for row in cursor.fetchall():
        listbox1.insert(END,row)

    connection.close()

def addCategory():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO CategoriesCosts(nameCategory) VALUES('{entry1.get()}')")
    connection.commit()
    connection.close()

def deleteCategory():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM CategoriesCosts WHERE id = '{entrydelete.get()}'")
    connection.commit()
    connection.close()

    loadBase()



def addCost():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO CategoriesCosts(nameCategory, nameCost, price, date) VALUES('{entry2.get()}', '{entry3.get()}', '{entry4.get()}', '{entry5.get()}')")
    connection.commit()
    connection.close()

    loadBase()

def zvitDate():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM CategoriesCosts WHERE date='{entryDate.get()}'")
    for row in cursor.fetchall():
        listbox2.insert(END, row)

    connection.close()

def zvitName():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM CategoriesCosts WHERE nameCost='{entryName.get()}'")
    for row in cursor.fetchall():
        listbox2.insert(END, row)

    connection.close()

def zvitCategory():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM CategoriesCosts WHERE nameCategory='{entryCategories.get()}'")
    for row in cursor.fetchall():
        listbox2.insert(END, row)

    connection.close()

def maxVitratyCategory():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT price FROM CategoriesCosts WHERE nameCategory='{entryReports.get()}'")
    list1 = []
    for row in cursor.fetchall():
        value = int(row[0])
        list1.append(value)
        maxchislo = max(list1)
        text = "Max Cost in this Category: "
    listbox2.insert(END, text, maxchislo)

    connection.close()

def maxVytratyDate():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT price FROM CategoriesCosts WHERE date = '{entryReports.get()}'")
    list1 = []
    for row in cursor.fetchall():
        value = int(row[0])
        list1.append(value)
        maxchislo = max(list1)
        text1 = "Max Cost in this day: "
    listbox2.insert(END,text1, maxchislo)

    connection.close()

def minVytratyCategory():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT price FROM CategoriesCosts WHERE nameCategory='{entryReports.get()}'")
    list1 = []
    for row in cursor.fetchall():
        value = int(row[0])
        list1.append(value)
        minchislo = min(list1)
        text = "Min Cost in this Category: "
    listbox2.insert(END, text, minchislo)

    connection.close()

def minVitratyDate():
    connection = sqlite3.connect("ekzamen_zadanie.db")
    cursor = connection.cursor()
    cursor.execute(f"SELECT price FROM CategoriesCosts WHERE date = '{entryReports.get()}'")
    list2 = []
    for row in cursor.fetchall():
        value2 = int(row[0])
        list2.append(value2)
        minchislo = min(list2)
        text2 = "Min Cost in this day: "
    listbox2.insert(END, text2, minchislo)

    connection.close()

def clearListbox():
    listbox1.delete(0,END)
    listbox2.delete(0,END)


# Колонка в самом начале
label1 = Label(window, text="Info from Base:")
# Колонки для добавления категории
label2 = Label(window, text="Name Category: ")
label3 = Label(window, text="Name Cost:")
label4 = Label(window, text="Price: ")
label5 = Label(window, text="Date: ")
labelzvit = Label(window, text="information from reports: ")


listbox1 = Listbox(window, height=5)
listbox2 = Listbox(window, height=5)

entry1 = Entry(window, width=17)
entry2 = Entry(window)
entry3 = Entry(window)
entry4 = Entry(window)
entry5 = Entry(window)
entrydelete = Entry(window, width=17)
#------------zvit
entryDate = Entry(window)
entryName = Entry(window)
entryCategories = Entry(window)
entryReports = Entry(window)



button1 = Button(text="Load Base", command=loadBase)
button2 = Button(text="Add Category", command=addCategory)
button3 = Button(text="Delete Category", command=deleteCategory)
button4 = Button(text="Add Cost", command=addCost)
# Zvit
button5 = Button(text="Zvit Date", command=zvitDate)
button6 = Button(text="Zvit Name cost", command=zvitName)
button7 = Button(text="Zvit Category", command=zvitCategory)
# Information from reports
buttoMaxCategory = Button(text="Report from  Max Vitraty", command=maxVitratyCategory)
buttonMaxDate = Button(text="Reports from Max Date", command=maxVytratyDate)
buttonMinCategory = Button(text="Reports from Min Vitraty", command=minVytratyCategory)
buttonMinDate = Button(text="Reports from Min Date", command=minVitratyDate)
buttonClear = Button(text="CLear", command=clearListbox)


# Колонка в самом начале
label1.grid(row=0, column=0, padx=5, pady=5)
# Колонки для добавления категории
label2.grid(row=4, column=0, padx=5, pady=5)
label3.grid(row=6, column=0, padx=5, pady=5)
label4.grid(row=8, column=0, padx=5, pady=5)
label5.grid(row=10, column=0, padx=5, pady=5)
labelzvit.grid(row=4, column=6,padx=5, pady=5)

# Info from base
listbox1.grid(row=1, column=0, columnspan=6, sticky="we")
# Zvit
listbox2.grid(row=1, column=4, columnspan=6, sticky="we")

# Entry for add category or delete
entry1.grid(row=2, column=1)
entrydelete.grid(row=2, column=2)
#Entry for button add cost
entry2.grid(row=5, column=0)
entry3.grid(row=7, column=0)
entry4.grid(row=9, column=0)
entry5.grid(row=11, column=0)
#- Entry for zvits
entryDate.grid(row=2, column=5)
entryName.grid(row=2, column=6)
entryCategories.grid(row=2, column=7)
entryReports.grid(row=5, column=6)


#---------
button1.grid(row=3, column=0, sticky="wens", padx=5)
button2.grid(row=3, column=1, sticky="wens", padx=5)
button3.grid(row=3, column=2, sticky="wens", padx=5)
button4.grid(row=12, column=0, sticky="wens", padx=5)
#Zvit
button5.grid(row=3, column=5, sticky="wens", padx=5)
button6.grid(row=3, column=6, sticky="wens", padx=5)
button7.grid(row=3, column=7, sticky="wens", padx=5)
# Information from reports
buttoMaxCategory.grid(row=6, column=5, sticky="wens", pady=5)
buttonMaxDate.grid(row=6, column=6, sticky="wens", pady=5)
buttonMinCategory.grid(row=6, column=7, sticky="wens", pady=5)
buttonMinDate.grid(row=7, column=6, sticky="wens", pady=5)
buttonClear.grid(row=2, column=0)






##############################
window.mainloop()