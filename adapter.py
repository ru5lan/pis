class Existing_functionality:
    """
    Main functionality of some Service (Target class)
    """

    def request(self) -> str:
        return "Normal string!"


class Useful_functionality:
    """
    New functionality that service wants to have, but does not support (Adaptee class)
    """

    def specific_request(self) -> str:
        return "!gnirts lamron toN"


class Adapter(Existing_functionality, Useful_functionality):
    """
    Makes the interface of the 'Existing_functionality' compatible with 'Useful_functionality' class
    interface due to multiple inheritance
    """

    def request(self) -> str:
        return self.specific_request()[::-1]


def some_code(target: "Existing_functionality") -> None:
    """
    Code supports all classes that use the 'Existing_functionality' interface
    """

    print(target.request(), end="\n\n")


if __name__ == "__main__":
    print("Existing_functionality output:")
    target = Existing_functionality()
    some_code(target)

    adaptee = Useful_functionality()
    print(f"New_functionality output(NOT OK):\n{adaptee.specific_request()}", end="\n\n")

    print("Adapter output(OK):")
    adapter = Adapter()
    some_code(adapter)
