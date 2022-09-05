class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def desscribe_user(self):
        print("Your personal information:")
        full_name = f"Full Name: {self.first_name} {self.last_name}\n"
        other_info = f"Age: {self.age}\t Email: {self.email} \n"
        full_info = full_name + other_info
        print(full_info)

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hi {full_name}, Your'e welcome!!")


person = User("Meen", "Madhang", 25, "meenphilip@gmail.com")
person.desscribe_user()
person.greet_user()
