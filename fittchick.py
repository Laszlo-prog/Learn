class FitnessApp:
    def __init__(self):
        #Initialize user fitness data
        self.data = {"steps": 0, "calories": 0, "workouts": []}

    def add_steps(self):
        steps = int(input("Enter steps walked"))

        self.data["steps"] += steps
        print("Steps update")

    def add_calories(self):

        cal = int(input("enter calories burned"))

        self.data["calories"] += cal

        print("calories update!")

    #add workout name
    def add_workout(self):
        w = input("Enter worout name: ")

        self.data["workouts"].append(w)

        print("workout added!")

    def show_summary(self):
        print("\n======Fitness Summary====")

        print("Total Steps: ", self.data["steps"])
        print("Total Calories: ", self.data["calories"])

        print("Workouts: ", ",".join(self.data["workouts"]) if self.data["workouts"] else "None")

    #Run Menu

    def run(self):
       while True: 
           print("\n1)Add steps \n2) Add Calories\n3) add workout\n4) Show sumary")
           choice = input("Choose: ")

           if choice == "1": self.add_steps()
           elif choice == "2": self.add_calories()
           elif choice == "3": self.add_workout()
           elif choice == "4": self.show_summary()
           elif choice == "5": break
           else: print("Invalid choice! ")

# Run menu!

FitnessApp().run()











    


