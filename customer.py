class Customer():
    def __init__(self,customer_ID, name, age, license, email):
        self.customer_ID = customer_ID
        self.name = name
        self.age = age
        self.license = license
        self.email = email
    
    def get_customer(self):
        return self.customer_ID
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_license(self):
        return self.license
    def get_email(self):
        return self.email
