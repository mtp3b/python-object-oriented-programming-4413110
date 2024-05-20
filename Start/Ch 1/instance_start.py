# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "SECRET ATTRIBUTE"

        # TODO: add properties

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount  #_ hints to other developers that this attribute is considered internal to the class
    


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("Legions", "Phage the Untouchable", 400, 12.25)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b1.setdiscount(0.5)
print(b1.getprice())


# TODO: properties with double underscores are hidden by the interpreter
print(b2.__secret)