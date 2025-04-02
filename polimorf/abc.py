class A:
    def say_hello(self):
        print("Labas iš A klasės")

class B(A):
    def say_hello(self):
        print("Sveikas iš B klasės")

class C(B):
    def say_hello(self):
        print("Labas iš C klasės")
    
obj = C()
obj.say_hello()

class A:
    def say_hello(self):
        print("Labas iš A klasės")

class B(A):
    def say_hello(self):
        print("Sveikas iš B klasės")
        super().say_hello()  

class C(B):
    def say_hello(self):
        print("Labas iš C klasės")
obj = C()
obj.say_hello()

class A:
    def say_hello(self):
        print("Labas iš A klasės")

class B(A):
    def say_hello(self):
        print("Sveikas iš B klasės")
        super().say_hello()

class C(B):
    def say_hello(self):
        print("Labas iš C klasės")
        super().say_hello()  

obj = C()
obj.say_hello()

# class A:
#     def say_hello(self):
#         print("Hello from class A")


# class B(A):
#     def say_hello(self):
#         print("Hello from class B")


# class C(B):
#     def say_hello(self):
#         print("Hello from class C")


# # Create an object of class C and call say_hello
# c_instance = C()
# c_instance.say_hello()  # Output: "Hello from class C"

# class A:
#     def say_hello(self):
#         print("Hello from class A")


# class B(A):
#     def say_hello(self):
#         super().say_hello()  # Calls A's say_hello
#         print("Hello from class B")


# class C(B):
#     def say_hello(self):
#         print("Hello from class C")


# # Create an object of class C and call say_hello again
# c_instance = C()
# c_instance.say_hello()  # Output: "Hello from class C"