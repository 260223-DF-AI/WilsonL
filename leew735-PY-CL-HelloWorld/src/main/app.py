# Application.py
from lab import Lab

if __name__ == "__main__":
    print("This program will print out whatever is returned by the Lab.sayHello method.")
    print("The current lab output: ")

    hello = Lab()
    output = hello.sayHello()

    print(output)