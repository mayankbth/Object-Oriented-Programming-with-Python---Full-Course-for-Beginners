# When to use class methods and when to use static method.

class Item:
    @staticmethod
    def is_integer():
        """
        this should do something that has a relationship with the class, but not something that must be unique
        per instance!

        OR

        we will use the static method when we want to do something that is not unique per instance.
        """

    @classmethod
    def instantiate_from_something(cls):
        """
        This should also do something that has a relationship with the class, but usually, those are used to manipulate
        different structures of data to instantiate objects, like we have done with CSV.

        OR

        the reason for which we would like to create a class method is for instantiating instances for some structured
        data like CSV.
        """

# a class method and a static method can only be called from a calss level. However, those only can be called form
# instances.
item1 = Item()
item1.is_integer()
item1.instantiate_from_something()