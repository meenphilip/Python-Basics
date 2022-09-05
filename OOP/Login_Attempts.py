class User():
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def desscribe_user(self):
        print("Your personal information:")
        full_name = f"Full Name: {self.first_name} {self.last_name}\n"
        other_info = f"Age: {self.age}\t Email: {self.email} \n"
        full_info = full_name + other_info
        print(full_info)

    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hi {full_name}, Your'e welcome!!")

    def get_login_attempts(self):
        print(f"Attempted login : {self.login_attempts}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Meen", "Madhang", 25, "meenphilip@gmail.com")
user.desscribe_user()
user.greet_user()

# login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts() 
user.increment_login_attempts()
user.increment_login_attempts()
user.get_login_attempts()
# reset attempts to default
user.reset_login_attempts()
user.get_login_attempts()
