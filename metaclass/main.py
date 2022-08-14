import typing


class ProviderMeta(type):
    def __new__(cls, name, bases, namespace):
        instance = super().__new__(cls, name, bases, namespace)

        if name == "Hello":
            # please note that we can only cast into parent type
            # for example here we can cast to Provide which is
            # defined before Hello and Bye.
            instance = typing.cast(type[Provider], instance)
            print(instance.hlo)

        return instance


class Provider(metaclass=ProviderMeta):
    hlo = "a very lonely class field"
    pass


class Hello(Provider):
    pass


class Bye(Provider):
    pass
