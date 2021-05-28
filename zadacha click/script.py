from tkinter import *
root = Tk()
a = 1000000000
x = 10
z = 10
y = 0
narko = 0
barig = 1
prod = 0
root.title('Комната в общаге')
root.geometry('1000x1000')

kypil = 0
def button_clicked():
    global a
    a = 0
    x = 1
    print("Вы всё спалили.")
    text1.delete('1.0', END)
    text1.get('1.0', END)
    text1.insert(1.0, 'Вы всё спалили', a)
def button2_clicked():
    global a
    global x
    a = a + x
    print("Кол-во купюр" + ' ' + str(a))
    text1.delete('1.0', END)
    text1.get('1.0', END)
    text1.insert(1.0, 'Кол-во купюр:' + str(a))
def button3_clicked():
    global a
    global x
    global kypil
    if a > 100:
        a = a - 100
        x = x + 2
        print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(a))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
        button3 = Button(bg = 'red')
def button4_clicked():
    global a
    global x
    global kypil
    if a > 500:
        a = a - 500
        x = x + 10
        print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(a))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
def button5_clicked():
    global a
    global x
    global kypil
    if a > 5000:
        a = a - 5000
        x = x + 20
        print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(a))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
def button6_clicked():
    global a
    global x
    global kypil
    if a > 10000:
        a = a - 10000
        x = x + 50
        print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(a))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
def button7_clicked():
    global a
    global x
    global kypil
    if a > 15000:
        a = a - 15000
        x = x + 100
        print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(a))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
def button8_clicked():
    global a
    global x
    global kypil
    if a > 50000:
        a = a - 50000
        x = x + 150
        print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(a))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
def button9_clicked():
    global a
    global x
    global kypil
    global window
    global narko
    if a > 100000:
        a = a - 100000
        x = x + 200
        print('Стафф лаба куплена' + ' ' + 'Ваши купюры:' + ' ' + str(a))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
        narko_show()
        narko = 1
canvas = Canvas(root, width = 450, height = 50, bg = 'blue')
canvas.create_text(200, 20, text = 'HARDLIVE', font = 14)
canvas.pack()
button = Button(root, bg = 'red', text = "Сжечь в мусорном баке", command = button_clicked, font = 200, fg = 'yellow', width = 50)
button2 = Button(root, bg = 'green', text = "Напечатать деньги", command = button2_clicked, font = 200, fg = 'yellow', width = 50)
button3 = Button(root, bg = 'green', text = "Улучшение №1, Стоимость: 100$", command = button3_clicked, font = 200, fg = 'yellow', width = 50)
button4 = Button(root, bg = 'green', text = "Улучшение №2, Стоимость: 500$", command = button4_clicked, font = 200, fg = 'yellow', width = 50)
button5 = Button(root, bg = 'green', text = "Улучшение №3, Стоимость: 5000$", command = button5_clicked, font = 200, fg = 'yellow', width = 50)
button6 = Button(root, bg = 'green', text = "Улучшение №4, Стоимость: 10000$", command = button6_clicked, font = 200, fg = 'yellow', width = 50)
button7 = Button(root, bg = 'green', text = "Улучшение №5, Стоимость: 15000$", command = button7_clicked, font = 200, fg = 'yellow', width = 50)
button8 = Button(root, bg = 'green', text = "Улучшение №6, Стоимость: 50000$", command = button8_clicked, font = 200, fg = 'yellow', width = 50)
button9 = Button(root, bg = 'green', text = "Купить стафф лабу, Стоимость: 100000$", command = button9_clicked, font = 200, fg = 'yellow', width = 50)
text1=Text(root, height = 1, font='Arial 14', wrap=WORD)
text1.place(x = 10, y = 490)


canvas.pack()
button.place(x = 10, y = 60)
button2.place(x = 10, y = 110)
button3.place(x = 10, y = 160)
button4.place(x = 10, y = 210)
button5.place(x = 10, y = 260)
button6.place(x = 10, y = 310)
button7.place(x = 10, y = 360)
button8.place(x = 10, y = 410)
button9.place(x = 10, y = 460)
def narko_show():
    def button10_clicked():
        global y
        global z
        y = 0
        z = 10
        print("Вы все смыли.")
        text2.delete('1.0', END)
        text2.get('1.0', END)
        text2.insert(1.0, 'Вы все смыли' + ' ' + str(y))
        text1.delete('1.0', END)
        text1.get('1.0', END)
        text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button11_clicked():
        global y
        global z
        global narko
        if narko > 0:
            global y
            global z
            y = y + z
            print("Кол-во купюр" + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во граммов:' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button12_clicked():
        global a
        global x
        global narko
        global z
        if a > 10000:
            a = a - 10000
            z = z + 20
            print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во купюр:' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button13_clicked():
        global a
        global x
        global narko
        global z
        if a > 50000:
            a = a - 50000
            z = z + 100
            print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во купюр:' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button14_clicked():
        global a
        global x
        global narko
        global z
        if a > 500000:
            a = a - 500000
            z = z + 200
            print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во купюр:' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button15_clicked():
        global a
        global x
        global narko
        global z
        if y > 1000000:
            a = y - 1000000
            z = z + 500

            print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во купюр:' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button16_clicked():
        global a
        global x
        global narko
        global z
        if a > 1500000:
            a = a - 1500000
            z = z + 1000
            print('Улучшение куплено.' + ' ' + 'Ваши купюры:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во :' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button17_clicked():
        global a
        global x
        global narko
        global barig
        global prod
        global y
        if a > 5000000 and barig == 0:
            a = a - 5000000
            barig = 1
            print('Улучшение куплено.' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во граммов:' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
        elif a > 5000000 and barig == 1:
            a = a - 5000000
            barig = 2
            print('Улучшение куплено.' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во граммов' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
        elif a > 5000000 and barig == 2:
            a = a - 5000000
            barig = 3
            print('Улучшение куплено.' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во граммов' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
        elif a > 5000000 and barig == 3:
            a = a - 5000000
            barig = 4
            print('Улучшение куплено.' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Кол-во граммов' + str(y))
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    def button18_clicked():
        global prod
        global a
        global y
        global z
        global window
        global barig
        if barig == 0:
            a = a + y * 2
            y = 0
            print('Стафф продан' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Продано')
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
        elif barig == 1:
            a = a + y * 3
            y = 0
            print('Стафф продан' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Продано')
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
        elif barig == 2:
            a = a + y * 4
            y = 0
            print('Стафф продан' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Продано')
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
        elif barig == 3:
            a = a + y * 5
            y = 0
            print('Стафф продан' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Продано')
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
        elif barig == 4:
            a = a + y * 6
            y = 0
            print('Стафф продана' + ' ' + 'Ваши граммы:' + ' ' + str(y))
            text2.delete('1.0', END)
            text2.get('1.0', END)
            text2.insert(1.0, 'Продано')
            text1.delete('1.0', END)
            text1.get('1.0', END)
            text1.insert(1.0, 'Кол-во купюр:' + str(a))
    button10 = Button(root, bg = 'red', text = "Смыть в унитаз", command = button10_clicked, font = 200, fg = 'yellow', width = 50)
    button11 = Button(root, bg = 'blue', text = "Сварить стафф", command = button11_clicked, font = 200, fg = 'yellow', width = 50)
    button12 = Button(root, bg = 'blue', text = "Нанять рабочего, Стоимость: 10000$", command = button12_clicked, font = 200, fg = 'yellow', width = 50)
    button13 = Button(root, bg = 'blue', text = "Заплатить копам, Стоимость: 50000$", command = button13_clicked, font = 200, fg = 'yellow', width = 50)
    button14 = Button(root, bg = 'blue', text = "Рассказать людям, Стоимость: 500000$", command = button14_clicked, font = 200, fg = 'yellow', width = 50)
    button15 = Button(root, bg = 'blue', text = "Купить плиту, Стоимость: 1000000$", command = button15_clicked, font = 200, fg = 'yellow', width = 50)
    button16 = Button(root, bg = 'blue', text = "Купить рекламу, Стоимость: 1500000$", command = button16_clicked, font = 200, fg = 'yellow', width = 50)
    button17 = Button(root, bg = 'blue', text = "Нанять барыгу, Стоимость: 5000000$", command = button17_clicked, font = 200, fg = 'yellow', width = 50)
    button18 = Button(root, bg = 'blue', text = "Продать стафф", command = button18_clicked, font = 200, fg = 'yellow', width = 50)
    text2=Text(root, height = 1, font='Arial 14', wrap=WORD)
    text2.place(x = 10, y = 550)

    button10.place(x = 500, y = 60)
    button11.place(x = 500, y = 110)
    button12.place(x = 500, y = 160)
    button13.place(x = 500, y = 210)
    button14.place(x = 500, y = 260)
    button15.place(x = 500, y = 310)
    button16.place(x = 500, y = 360)
    button17.place(x = 500, y = 410)
    button18.place(x = 500, y = 460)

root.mainloop()




