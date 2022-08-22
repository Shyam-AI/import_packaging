
class CUSTOM_PACKAGE():
   

    def __init__(self):
        """custom package
           Author : Shyam U
        """

        self.message = "Inside the constructor"
        print(self.message)

    def train(self):

        self.message = "Inside the trainer function"
        print(self.message)


    def predict(self):
        self.message = "Inside the predict function"
        print(self.message)