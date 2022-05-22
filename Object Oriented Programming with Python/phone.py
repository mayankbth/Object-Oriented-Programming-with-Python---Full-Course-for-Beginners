from item import Item


"""
Inheritance
"""
# # The attribute "broken_phones" is unique per instance. So, in order to solve this problem in order to best practices
# # in object oriented programing then we could go ahead and create a seperated class that will inherit the functionality
# # that the Item class brings with it. this is exactly we could benefit form inheritance.
# phone1 = Item("jscPhone10", 500, 5)
# phone1.broken_phones = 1
# phone2 = Item("jscPhone20", 700, 5)
# phone2.broken_phones = 1

# child class "Phone" of parent class "Item"
class Phone(Item):

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        """super(): allows us to have the full access of all the attributes of the parents class"""
        # call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )

        # Run a validation to received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to zero!"

        # Assign to self object
        self.broken_phones = broken_phones


# phone1 = Phone("jscPhone10", 500, 5, 1)
# print(phone1.calculate_total_prise())
# print(Item.all)
# print(Phone.all)


