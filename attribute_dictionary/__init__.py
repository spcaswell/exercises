import collections

from typing import Any


class AttributeDictionary(collections.defaultdict):
    """
    A dictionary that allows dot notation to access data inside nested dictionaries.  dict[key1][key2] --> dict.key1.key2
    """
    def __init__(self, *args, **kwargs):
        super(AttributeDictionary, self).__init__(AttributeDictionary)
        self.populate(*args, **kwargs)

    def __getattr__(self, k):
        return self[k]

    def __setattr__(self, k, v):
        self[k] = v

    def populate(self, *args, **kwargs):
        for arg in args:
            if isinstance(arg, dict):
                self.populate(**arg)
        if kwargs:
            for k, v in kwargs.items():
                if isinstance(v, dict):
                    self[k] = AttributeDictionary(v)
                else:
                    self[k] = v


class AttributeObject:
    """
    A general object that instantiates an AttributeDictionary, allowing access to all members using dot notation.
    Setting keys to values via dot notation is also supported.
    """
    def __getattr__(self, item: str) -> Any:
        """
        Searches the AttributeObject for attributes named item.
        :param item: The attribute to search for.
        :return: The attribute if found.
        :raises: Will raise an AttributeError if item is not found.
        """
        to_return = self.__dict__.get(item)
        if not to_return:
            raise AttributeError
        return to_return

    def __getitem__(self, item: str) -> Any:
        """
        Allows use of standard python bracket [] index accessors.
        :param item: That attribute to search for
        :return: The attribute if found
        """
        return getattr(self, item)

    def __setattr__(self, k, v):
        """
        Adds values to the object when assigning values to keys.
        :param k: The key to add/update
        :param v: The value to associate with key
        :return: None
        """
        super(AttributeObject, self).__setattr__(k, v)

    def __init__(self, **kwargs):
        """
        Instantiates the AttributeObject
        :param kwargs: A dictionary that contains the data for the AttributeObject.
        """
        for k, v in kwargs.items():
            if isinstance(v, dict):
                setattr(self, k, AttributeObject(**v))
            else:
                setattr(self, k, v)
