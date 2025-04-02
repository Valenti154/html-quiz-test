class Book:
    def __init__(self, title: str, autor: str, pages: int):
       self.title = title
       self.autor = autor
       self.pages = pages
    def describe(self):
        print(f"Book: {self.title}, {self.autor}, {self.pages}")
    
class EBook (Book):
    def __init__(self,title: str, autor: str, pages: int, file_size: int):
        super().__init__(title, autor, pages)
        self.file_size = file_size
    def download(self):
        print(f"Atsiunciama knyga:{self.title} (dydis: {self.file_size} MB)")

ebook = EBook("Python pamokos", "Mokitojas Jonas", 200, 5)
ebook.describe()
ebook.download()