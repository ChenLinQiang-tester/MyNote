def getx(self):
    return self._x


def setx(self, value):
    self._x = value


def delx(self):
    del self._x


# create a property
x = property(getx, setx, delx, "I am doc for x property")
