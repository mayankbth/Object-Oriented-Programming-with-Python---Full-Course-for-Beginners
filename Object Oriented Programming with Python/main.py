# from item import Item
from phone import Phone


# Item.instantiate_from_csv()
#
# print(Item.all)

# item1 = Item("MyItem", 750)

# print(item1.all)
# print(item1.name)

# item1.name = "OtherItem"

# # Exception
# item1.name = "OtherItem123"

# # print(item1.all)
# print(item1.name)


"""
Encapsulation
"""

# print(item1.read_only_name)

# because of "Encapsulation" we wont be able to change the value for "read_only_name"
# once it is created
#
# item1.read_only_name = "BBB"
# print(item1.read_only_name)
# # # output:
# #         item1.read_only_name = "BBB"
# #     AttributeError: can't set attribute

# print(item1.name)
#
# print(item1)

# item1.price = 900
# print(item1.price)
#
# item1.apply_increment(0.2)
#
# print(item1.price)
#
# item1.apply_discount()
#
# print(item1.price)


"""
Abstraction

Abstraction in Python is the process of hiding the real implementation of an application 
from the user and emphasizing only on usage of it. 
"""

# item1.send_email()


"""
Inheritance
"""

item1 = Phone("jscPhone", 1000, 3)

# item1.send_email()

item1.apply_increment(0.2)

print(item1.price)