from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise ValueError("Type in positive")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"BMI: {self.calculate_bmi():.2f}")
        print(f"Category: {self.get_bmi_category()}")

class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height**2)
    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if  bmi  < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Weight"
        elif bmi < 29.9:
            return "Overweight"
        elif bmi > 24:
            return "Obese"


class Child(Person):

    def calculate_bmi(self):
        return (self.weight / (self.height ** 2))* 1.3

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal wight"
        elif bmi < 24:
            return "Overweight"
        elif bmi > 24:
            return "Obese"


class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_user_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        height = float(input("Enter height (in meters): "))
        weight = float(input("Enter weight (in kg): "))

        if age >= 18:
            person = Adult(name, age, height, weight)
        else:
            person = Child(name, age, height, weight)

        self.add_person(person)

    def print_results(self):
        print("\n--- BMI Results ---")
        for person in self.people:
            person.print_info()
            print("-------------------")

    def run(self):
        while True:
            self.collect_user_data()

            choice = input("Do you want to add another person? (y/n): ").lower()
            if choice != 'y':
                break

        self.print_results()