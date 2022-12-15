class Helloer:
    """
    Helloer is a person that say hello to the queen.
    """

    def __init__(self, name="Parham"):
        self.count = 0
        self.name = name

    def say(self) -> str:
        self.count += 1

        return "Hello"


class Queen:
    """
    Queen must have only one person that say hello to her
    """

    def __init__(self, helloer=Helloer("Parham")):
        self.helloer = helloer


if __name__ == "__main__":
    # here we create two differnt instance of the queen
    # class but both of them are using the same initial
    # value for their helloer field, do you believe this?
    q1 = Queen()
    print(q1.helloer.say())
    print(q1.helloer.count)

    q2 = Queen()
    print(q2.helloer.count)
    # q2 helloer never say hello but because they share
    # the same instance of the helloer its conut also
    # increased.
