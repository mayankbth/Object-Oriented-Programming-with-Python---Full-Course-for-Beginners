import csv


class Item:
    # Class Attribute
    pay_rate = 0.8
    # The pay rate after 20% discount

    all = []

    # # "__init__" also called constructor.
    # # these type of "__method_name__" are called "dunder methods" or "magic methods"...
    # # when we create an instance of a class then python executes the "__inir__" method autometically.
    # def __init__(self, name, price, quantity):
    # # parameter with default value in case it dont get any
    # def __init__(self, name, price, quantity=0):
    # to validate the parameters data using type checking
    # if we pass the "name" like "name: str", then it means that it will only accept string type data as an argument fot "name" parameter.
    # for quantity we do not need to pass the type because we already have provided an integer value as an default.
    def __init__(self, name: str, price: float, quantity=0):
        # print("I am created")
        # print(f"An instance created: {name}")

        # Run vallidation to received an arguments
        # Assertions are statements that assert or state a fact confidently in your program.
        # Assertions are simply boolean expressions that check if the conditions return true or not.
        # If it is true, the program does nothing and moves to the next line of code. However, if it's false,
        # the program stops and throws an error.
        assert price >= 0, f"Price {price} is not greater than or rqual to zero!"
        assert quantity >= 0, f"Price {price} is not greater than or rqual to zero!"

        # assign to self object
        # the "self" parameter holds the object instantiating the class. So it allows us to assign the attributes from the "__init__" method.
        # like, "self.name" = "item1.name"
        # self.name = name
        # self._name = name
        # privet
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Action to be executed
        # this will append all the instences in the list "all"
        Item.all.append(self)


    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        # return self._name
        return self.__name

    @name.setter
    # by doing this we are allowing to set the new values for the name,
    # even after we have set is as a "ead-Only Attribute".
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value


    # # creating a methos to calculate the total prise.
    # # function created inside a class is called "method".
    # def calculate_total_prise(self, x, y):
    def calculate_total_prise(self):
        # # when creating a method python will autometically generate the "self" parameter, inside the parantheses.
        # # because python passes the object as a firs argument when we call the methods.
        # # and "self" as a parameter is a place holder for the object which instantiates the class.
        # # if we remove the "self" parameter then we will get the error:
        # #       "TypeError: calculate_total_price() takes 0 potential argument but 1 was given"
        # # we can replace "self" with any other parameter name, however "self" is a common convention because,
        # # when instantiating a class the first parameter passes through the method is the object it self.
        # return x*y
        return self.__price * self.quantity

    # "apply_discount" method is overwriting the price attribute
    def apply_discount(self):

        # # this will get the "pay_rate" from class level in every case
        # self.price = self.price * Item.pay_rate

        # this will get the "pay_rate" first from instance level, if provided and if not then from class level
        self.__price = self.__price * self.pay_rate

    """
        Class Method: 
        A class method is a method that is bound to a class rather than its object. It doesn't require creation of a 
        class instance, much like staticmethod.

        class method sends the class reference as the first argument.

        The difference between a static method and a class method is:

            Static method knows nothing about the class and just deals with the parameters
            Class method works with the class since its parameter is always the class itself.
    """

    # Instantiating from CSV file I.e. form "item.csv"
    # here instead of "self" we are getting "cls" because when we call class method then the class itself is passed as the first argument
    @classmethod
    def instantiate_from_csv(cls):
        # to read the csv
        with open('items.csv', 'r') as f:
            # "csv.DictReader(f)" will read the content as a list of dictonary
            reader = csv.DictReader(f)
            itmes = list(reader)
        for item in itmes:
            # print(item)
            # creating instances
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    """
        static method:
        static method does the type of work that has some logical connection to a class.

        for example, to check a number if its int or float.

        static methods never sends the instance as the first argument. i.e. object as a first argument.
        i.e. why we should relate the static with the regular function. 
    """

    @staticmethod
    def is_integer(num):
        # We will count out the decimal that are point zero.
        # For example: 5.0, 10.0
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # Python repr() Function returns a printable representation of the object passed to it.
    def __repr__(self):
        # return f"Item('{self.name}', {self.price}, {self.quantity})"

        # A generic way to access the name of the class from the instance
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    """
    Abstraction
    
    Abstraction in Python is the process of hiding the real implementation of an application 
    from the user and emphasizing only on usage of it. 
    """

    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        ...
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()


    """
    Encapsulation:
    
    Encapsulation is one of the fundamental concepts in object-oriented programming (OOP). It describes the idea of 
    wrapping data and the methods that work on data within one unit. This puts restrictions on accessing variables and 
    methods directly and can prevent the accidental modification of data.
    """

    # @property
    # def read_only_name(self):
    #     return "AAA"


'''
    In the following type of code one, of the few problems, we have here. that, we do not have a set of rules for the attributes,
    that we like to pass in, in order to instantiate an instance sucessgully. I.e. for each items that I want to go ahade and create I
    need to hard code in the attribute names like "name, price, quantity" and it could have been nicer if we can somehow declare in the class
    that in order to instantiate an instance sucessfully, name, price and quantity must be passed. Otherwise the instance could not have been
    created sucessfully.

    And there is a way to reach such beavihour with the help of a special method called "__init__". This method is also called "construct".
    Basically this is a method with a unique name that we need to call it the way it is intentionally in order to use its special features.
'''
# # instantiating the class "Item()".
# # we can also say that "item1" is an instance of "Item()".
# item1 = Item("Phone", 100, 5)

# assigining some attributes to instance "item1".
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# # # calling a method on "item1" instance
# # # here, the objecct it self is getting passes through in the method as a first argument, by default by the python.
# # # here, "item1.price" and "item1.quantity" is getting passed through as a second and third arguments.
# # print(item1.calculate_total_prise(item1.price, item1.quantity))

# item2 = Item("Laptop", 1000, 3)
# # item2.name = "Laptop"
# # item2.price = 1000
# # item2.quantity = 3
# # # print(item2.calculate_total_prise(item2.price, item2.quantity))

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)


'''
    Constructor or "__init__"
'''
# # to assign some extra attributes to a object outside of constructor
# item2.has_numpad = False
# print(item2.name)
# print(item2.price)
# print(item2.quantity)
# print(item2.has_numpad)

# print(item1.calculate_total_prise())
# print(item2.calculate_total_prise())


'''
    validate the data type of the values that we are passing in into constucrot.
'''
# # there are couple of ways to achive this and one wayes is to using type when declaring parameters.
# item1 = Item("Phone", "100", 1)
# item2 = Item("Laptop", "1000", 3)
# print(item1.calculate_total_prise())
# print(item2.calculate_total_prise())
# # Output:
# # 100
# # 100010001000


'''
    to check "Assertion" defined in "__init__" or "constructor"
'''
# item1 = Item("Phone", 100, -1)
# item2 = Item("Laptop", 1000, -3)
# print(item1.calculate_total_prise())
# print(item2.calculate_total_prise())
# # output:
#     #     assert quantity >= 0, f"Price {price} is not greater than or rqual to zero!"
#     # AssertionError: Price 100 is not greater than or rqual to zero!


'''
    Class attributes: are the variables defined directly in the class that are shared by all objects of the class.

    Instance attributes: are attributes or properties attached to an instance of a class. Instance attributes are defined in the constructor.

    Class Attribute:
        Defined directly inside a class.
        Shared across all objects.
        Accessed using class name as well as using object with dot notation, e.g. "classname.class_attribute" or "object.class_attribute".
        Changing value by using "classname.class_attribute = value" will be reflected to all the objects.

    Instance Attribute:
        Defined inside a constructor using the self parameter.
        Specific to object.
        Accessed using object dot notation e.g. object.instance_attribute.
        Changing value of instance attribute will not be reflected to other objects.        
'''
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# # print(Item.pay_rate)
# # print(item1.pay_rate)
# # print(item2.pay_rate)

# # A special attribute of every module is " __dict__". This is the dictionary containing the module’s symbol table.
# # A dictionary or other mapping object used to store an object’s (writable) attributes.
# print(Item.__dict__)    # All the attributes for class level
# print(item1.__dict__)   # All the attributes for instanse level


'''
    "apply_discount" method for overwriting the price attribute
'''
# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)

# # overwriting the class attribute to apply a 30% discount
# # This is happning because "item2" is getting the attribute "pay_rate" at instance level
# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)


'''
    creating a class attribute for providing the list of all elements "__repr__"
'''
# item1 = Item("Phone", 100, 1)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

# print(Item.all)

# # # if want to print only one of the attributes fromm instances
# # for instance in Item.all:
# #     print(instance.name)


"""
    Class Method:
"""
# Item.instantiate_from_csv()
# print(Item.all)

"""
    static Method:
"""
# print(Item.is_integer(7))
# print(Item.is_integer(7.5))
# print(Item.is_integer(7.0))
