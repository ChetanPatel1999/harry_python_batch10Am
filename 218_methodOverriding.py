class base :
    def display(self):
        print("hi i am base display")

class derived(base):
    def display(self):  #method overriding
        # super().display()
        print("hi i am derived display")

d1= derived()
d1.display()