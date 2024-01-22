class sushant:
    def __init__(self):
        self.name = None
        self.age = None

    def set_info(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        if self.name is not None and self.age is not None:
            print(f"Name: {self.name}, Age: {self.age}")
        else:
            print("Information is not set.")

    def reset_info(self):
        self.name = None
        self.age = None

ssushant = sushant()

try:
    ssushant.set_info('Sushant', 34)
    ssushant.display_info()
    
    # Now, reset the information
    ssushant.reset_info()
    ssushant.display_info()
except Exception as e:
    print("An error occurred.")

# Output:
# Name: Sushant, Age: 34
# Information is not set.
