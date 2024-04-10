class StringManipulator:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print("String in uppercase:", self.string.upper())


# Example usage:
s = StringManipulator()
s.get_string()
s.print_string()
