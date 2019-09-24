from tkinter import *

#создание основного поля
root = Tk()
root.title("Encryption")
root["bg"] = "black"
root.geometry('480x200')

AMOUNT = 26


message = StringVar()
#ввод кода
firstEntry = Entry(width=40, textvariable=message, font=10)
firstEntry.grid(column=2, row=1)


k1 = IntVar()
#ввод коэффициента
secondEntry = Entry(width=40, font=10, textvariable=k1)
secondEntry.grid(column=2, row=2)

k2 = IntVar()
#ввод второго коэффициента
thirdEntry = Entry(width=40, font=10, textvariable=k2)
thirdEntry.grid(column=2, row=3)

#подписи
label1 = Label(text="Enter string",font=14, bg="black", fg="white").grid(row=1, column=0)
label2 = Label(text="     Enter k1", font=10, bg="black", fg="white").grid(row=2, column=0)
label3 = Label(text="     Enter k2", font=10,bg="black", fg="white").grid(row=3, column=0)
label4 = Label(text="Encryption", font=14,bg="black", fg="white").grid(row=5, column =0)
label5 = Label(text="Decryption", font=14,bg="black", fg="white").grid(row=7, column=0)


#поле вывода кодировки
codText = Text(width=40,height = 1.2,font=10)
codText.grid(column=2, row=5)

#поле вывода раскодировки
decodText = Text(width=40,height=1.2,font=10)
decodText.grid(column=2, row=7)

enLetter = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9,
            "K":10, "L":11, "M":12, "N":13, "O":14, "P":15, "Q":16, "R":17, "S":18,
            "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25}

deLetter = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 6:"G", 7:"H", 8:"I", 9:"J",
            10:"K", 11:"L", 12:"M", 13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S",
            19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y", 25:"Z"}

start = []
code = []
decode = []
code2 = []
FLAG = True

def __takeInfo():
    newCode = message.get().upper()
    codText.delete(1.0, END)
    for i in newCode:
        #проверка на правильность ввода строки
        try:
            num = enLetter[i]
            start.append(num)
        except:
            start.clear()
            codText.insert(1.0,"ERROR STRING ")
            break
    #чистка строки кодирования


def __encrypt():
    FLAG = True
    codText.delete(1.0, END)
    __takeInfo()
    coaf1 = k1.get()
    coaf2 = k2.get()
    #костыльная проверка на кривой коэффициент
    if((coaf1>AMOUNT and coaf1%AMOUNT == 0) or (coaf2>AMOUNT and coaf2%AMOUNT == 0) or coaf1%2 == 0 or (coaf2 != 0 and coaf2%2 == 0) or
    coaf1%13 == 0 or (coaf2 != 0 and coaf2%13 == 0)):
        codText.insert(1.0, "ERROR COEFFICIENT ")
        FLAG = False
        return FLAG
    for i in start:
        lett = (i*coaf1 + coaf2)%AMOUNT
        code.append(deLetter[lett])

def __decrypt():
    coaf1 = k1.get()
    coaf2 = k2.get()
    decodText.delete(1.0, END)
    if not decode:
        decodText.insert(1.0, "ENCRYPT STRING IS EMPTY")
    else:
        for i in decode:
            num = enLetter[i]
            for k in range(26):
                if (num == (k*coaf1 + coaf2)%AMOUNT):
                    #lett = k
                    code2.append(deLetter[k])


#кодировка
def printCode():
    __encrypt()
    if(FLAG):
        codText.insert(1.0,code)
        for i in code:
            decode.append(i)
        #чистка списков
        code.clear()
        start.clear()



#декодировка
def printDecode():
    __decrypt()
    decodText.insert(1.0,code2)
    decode.clear()
    code2.clear()


#кнопка кодировки
button1 = Button(text="Encrypt",background="green",foreground="white",
                 padx="50", pady="1", font=12, command=printCode).grid(row=4, column = 2)

#кнопка раскодировки
button1 = Button(text="Decrypt", background="red",foreground="white",padx="50", pady="1", font=12, command=printDecode).grid(row=6, column = 2)


root.mainloop()
