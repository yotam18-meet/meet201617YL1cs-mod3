class Student:
    def __init__(self, name, hometown, age, height, favourite_ice_cream_flavour):
        self.name = name
        self.hometown = hometown
        self.age = age
        self.height = height
        self.favourite_ice_cream_flavour = favourite_ice_cream_flavour
    def print_summary(self):
        print(str(self.name)+" is "+str(self.age)+" years old, and was born in "+ str(self.hometown)+". Did you know "+ str(self.name)+" is "+ str(self.height)+ "cm tall? And they absolutely LOVE "+ str(self.favourite_ice_cream_flavour)+ " ice cream!")

    def get_giraffe_gap(self):
        print("There are " + str(float(500)-float(self.height))+ " cm between "+ str(self.name)+ " and an average giraffe.")
        
