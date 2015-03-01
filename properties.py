from collections import UserList

class BaseProperty(object):
    def __init__(self, value):
        self.input(value)

class TextProperty(BaseProperty):
    def input(self, value):
        self.data = value

    def __str__(self):
        return "<%s text:%s>" % (self.__class__.__name__, self.data)

    def Value(self):
        return self.data

    def ToJSON(self):
        return self.data

    def Type():
        return "Text"

class ListProperty(BaseProperty, UserList):

    def input(self, values):
        if isinstance(values, list):
            for value in values:
                self.addToList(value)
        else:
            self.addToList(values)

    def addToList(self, value):
        if value in self.data:
            pass
        else:
            print("addToList", value, self.data)
            self.list.append(value)

    def __str__(self):
        return "<%s list:%s>" % (self.__class__.__name__, self.data)

    def Type():
        return "List"

class IntProperty(BaseProperty):
    def input(self, values):
        result = []

        if isinstance(values, list):
            for value in values:
                if False == value.isdigit():
                    continue

                if isinstance(value, str):
                    result.append(int(value))
        elif isinstance(values, int):
            result.append(values)
        else:
            if values.isdigit():
                result.append(int(values))

        return result

    def Type():
        return "Int"

class RangeProperty(IntProperty):
    min = -1
    max = -1

    def __init__(self):
        min = -1
        max = -1

    def __str__(self):
        return "<%s min:%d max:%d>" % (self.__class__.__name__, self.min, self.max)

    def input(self, values):
        for value in super(RangeProperty, self).input(values):
            if isinstance(value, int):
                self.addToRange(value)

    def addToRange(self, value):
        if value > self.max:
            self.max = value
        elif value < self.min:
            self.min = value

        if self.max < self.min:
            self.max = self.min

        if self.min < 0:
            self.min = self.max

        if self.max < 0:
            self.max = self.min

    def Type():
        return "Range"