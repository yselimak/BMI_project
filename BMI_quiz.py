import tkinter

#screen
bmi_window = tkinter.Tk()
bmi_window.title("BMI Calculator")
bmi_window.config(
                  padx=50,
                  pady=50)

#label
bmi_label = tkinter.Label(text="Enter Your Weight (kg):")
bmi_label.pack()

#find height - width
#bmi_label.update()
#print(bmi_label.winfo_width())


#entry
bmi_entry = tkinter.Entry()
bmi_entry.pack()
#bmi_entry.update()
#print(bmi_entry.winfo_width())


#label2
bmi_label2 = tkinter.Label(text="Enter Your Height (cm):")
bmi_label2.pack()


#entry2
bmi_entry2 = tkinter.Entry(width=20)
bmi_entry2.pack()


def button_clicked():
    bmi_weight = bmi_entry.get()
    bmi_height = bmi_entry2.get()

    if bmi_height == "" or bmi_weight == "":
        bmi_result_label.config(text="enter both its!")

    else:
        try:
            bmi = float(bmi_weight) / (float(bmi_height)/100) ** 2
            print(bmi)
            bmi_result_label.config(text=f"Your BMI: {round(bmi,2)}, {bmi_table(bmi)}")
        except:
            bmi_result_label.config(text="Enter a valid number!")




    #print(f"height: {bmi_height}, weight: {bmi_weight}")


def bmi_table(value):
    result = "You are "
    if value<18:
        result+="Underweight"
    elif 18 < value < 23:
        result+="Normal"
    elif 23< value< 25:
        result+="Overweight"
    else:
        result+="Obese"
    return result


#button
bmi_button = tkinter.Button(text="Caculate")
bmi_button.pack()
bmi_button.config(bg="red",
                  fg="white",
                  command=button_clicked)


#result_label
bmi_result_label = tkinter.Label()
bmi_result_label.pack()


bmi_window.mainloop()