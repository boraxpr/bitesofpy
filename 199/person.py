# see __mro__ output in Bite description
class Person:
    def __init__(self, end='\n'):
        self.msg = "I am a person"

    def __str__(self):
        return self.msg


class Father(Person):
    def __init__(self, end=''):
        super(Father, self).__init__(end='')
        self.msg = self.msg + " and cool daddy"

    def __str__(self):
        return self.msg


class Mother(Person):
    def __init__(self, end=''):
        super(Mother, self).__init__(end='')
        self.msg = self.msg + " and awesome mom"

    def __str__(self):
        return self.msg


class Child(Father, Mother, Person):
    def __init__(self):
        super().__init__(end="")
        self.msg = "I am the coolest kid"

    def __str__(self):
        return self.msg


def main():
    person = Person()
    dad = Father()
    mom = Mother()
    child = Child()
    pass

if __name__ == "__main__":
    main()
