from tkinter import *
window = Tk()
e=Entry(window,width=20)
e.pack(side=LEFT)
e.insert(0,"Name:")

# Layout
def h_h():
    myLabel2=Label(window,text="Welcome to Health Wealth "+e.get())
    myLabel2.pack()

myLabel=Label(window,text="HEALTH IS WEALTH")

def window_quit():
    exit()

button_quit=Button(window,text="Exit",command=window_quit)
button_quit.pack(side=BOTTOM)

myButton2=Button(window,text="Click",pady=10,padx=10,command=h_h,bg="red")

#myButton=Button(window,text="BMI CALCULATOR",pady=10,padx=10)
myLabel.pack(side=TOP)

myButton2.pack(side=LEFT)
button_quit.pack(side=BOTTOM)

# CALORIES
def na_me():
    from dataclasses import dataclass
    
    import numpy as np
    import matplotlib.pyplot as plt

    CALORIE_GOAL_LIMIT=3000
    PROTEIN_GOAL=180
    FAT_GOAL=80
    CARBS_GOAL=300

    today=[]

    @dataclass
    class Food:
        name: str
        calories: int
        protein: int
        fats: int
        carbs: int

    done=False

    while not done:
        print("""
        (1) Add a new food
        (2) Visualize progress
        (q) Quit
        """)

        choice=input("Choose the option: ")

        if choice=="1":
            print("Adding a new food!")
            name=input("Name: ")
            calories=int(input("Calories: "))
            proteins=int(input("Proteins: "))
            fats=int(input("Fats: "))
            carbs=int(input("Carbs: "))
            food=Food(name,calories,proteins,fats,carbs)
            today.append(food)
            print("Successfully added!")

        elif choice=="2":
            calorie_sum=sum(food.calories for food in today)
            protein_sum=sum(food.protein for food in today)
            fats_sum=sum(food.fats for food in today)
            carbs_sum=sum(food.carbs for food in today)

            fig, axs=plt.subplots(2,2)
            axs[0,0].pie([protein_sum,fats_sum,carbs_sum],labels=["Proteins","Fats","Carbs"],autopct="%.1f%%")
            axs[0,0].set_title("Macronutrients")
            axs[0,1].bar([0,1,2],[protein_sum,PROTEIN_GOAL,CARBS_GOAL],width=0.4)
            axs[0,1].bar([0;.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width= 0.4)
            axs[0,1].set_title("Macronutrient Goals")
            axs[1,0].pie([calorie_sum,CALORIE_GOAL_LIMIT-calorie_sum],labels=["Calories","Remaining"],autopct="%.1f%%")
            axs[1,0].set_title("Calories Goal Progress")
            axs[1,1].plot(list(range(len(today))),np.cumsum([food.calories for food in today]),label="Calories Eaten")
            axs[1,1].plot(list(range(len(today))),[CALORIE_GOAL_LIMIT]*len(today),label="Calorie Goal")
            axs[1,1].legend()
            axs[1,1].set_title("Calories Goal Over Time")
            
            fig.tight_layout()
            plt.show()

        elif choice=="q":
            done=True
        else:
            print("Invalid Choice")
            
myButton=Button(window,text="Calories",pady=10,padx=10,command=na_me)
myButton.pack(side=LEFT)

# BMI
def bm_i():
    def from_kg():

        # Convert kg to gram
        gram = float(e2_value.get())*1000

         # Convert kg to pound
        pound = float(e2_value.get())*2.20462

         # Convert kg to ounce
        ounce = float(e2_value.get())*35.274

        # Enters the converted weigjt to the text widget

        t1.delete("1.0", END)
        t1.insert(END, gram)

        t2.delete("1.0", END)
        t2.insert(END, pound)

        t3.delete("1.0", END)
        t3.insert(END, ounce)
        
        #Create Label Widgets
        
        e1 = Label(window, text = "Enter the weight in Kg")

        e2_value = StringVar()
        e2 = Entry(window, textvariable = e2_value)

        e3 = Label(window, text = "Gram")
        e4 = Label(window, text = "Pound")
        e5 = Label(window, text = "Ounce")

        #Create text widgets

        t1 = Text(window, height = 1, width = 20)
        t2 = Text(window, height = 1, width = 20)
        t3 = Text(window, height = 1, width = 20)

        # Create Button Widget
       b1 = Button(window, text = "Convert", command = from_kg)

       #grid method is used for placind the widgets at respective positions in the table

       e1.grid(row = 0, column = 0)
       e2.grid(row = 0, column = 1)
       e3.grid(row = 1, column = 0)
       e4.grid(row = 1, column = 1)
       e5.grid(row = 1, column = 2)
       t1.grid(row = 2, column = 0)
       t2.grid(row = 2, column = 1)
       t3.grid(row = 2, column = 2)
       b1.grid(row = 0, column = 2)
       
    

myButton5=Button(window,text="Weight Converter",command=bm_i)
myButton5.pack()

# Solutions
def so_lu():
    weight=float(input("Enter your weight: "))
    height=float(input("Enter your height: "))
    
    BMI = weight / (height/100)**2

    # Providing Solutions

    if (BMI<18.5):
        print("Is underweight and requires more intake of food")
    elif (BMI>=18.5 and BMI<24.9):
        print("Is healthy!")
    elif (BMI>=25.0 and BMI<29.9):
        print("Is overweight and requires exercise and additional help")
    else:
        print("Is obese and requires medical help immediately")

myButton4=Button(window,text="Solutions",command=so_lu)
myButton4.pack()

# Receive feedback

from tkinter import *

def feed_back():
    
    feedback=input("Are you happy with the solution?: ")
    
    if feedback=="YES":
        print("Thank you for the feedback")
    elif feedback=="NO":
        print("We will try to make your visit with us better the next time")
    else:
        print("Visit Again")

myButton5=Button(window,text="Feedback",command=feed_back)
myButton5.pack()
window.mainloop()

# Notifications
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="ALERT!!",
            message="Reminder: Eat Healthy!",
            timeout = 10
        )
        time.sleep(3600)
