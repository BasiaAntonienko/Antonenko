import unittest

class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Klient juz wypozyczyl te ksiazke.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Przepraszamy, ale ksiązki nie ma na naszej liście.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook): 
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Klient oddal ksiazke. Dziekujemy za korzystanie z naszego serwisu:)")

class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): 
        print("Ksiazka ktora chcesz wypozyczyc, jest wypozyczona.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): 
        print("Ksiazka ktora oddajesz jest {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
        
# w klasach chodzi o to, by stworzyć szablon funkcjonalności, który przypisujemy kolejnym obiektom tworząc je...

def setup():
    size(220,100)
    global library, Madzia, Basia
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Nad Niemnem"]
    library = Library(books) 
    Madzia = Customer()
    Basia = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) 
    rect(100,40,100,20) 
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc"))
            library.lendBook(Basia.requestBook("Nad Niemnem")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
            library.addBook(Basia.returnBook()) # powtarzanie warunków, to też zdecydowanie zły pomysł
            
            
class ExerciseTen(unittest.TestCase): 
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
    library = Library(books)


    def test_BA2(self): # zapomniałam wspomnieć, że nazwa metody musi się zaczynać od test, żeby właściwie działać
        Basia = Customer()
        self.library.lendBook(Basia.requestBook("Harry Potter"))
        self.assertEqual(["Naocznosc", "Sens Sztuki"], self.library.availableBooks)
        self.assertEqual(Basia.book, "Harry Potter")
        self.assertTrue(Basia.haveBook)

    def test_BA3(self):
        self.library.addBook("Medaliony")
        self.assertEqual(["Naocznosc", "Sens Sztuki", "Medaliony"], self.library.availableBooks)
        
if __name__ == '__main__':
    unittest.main()
    
    #1,25pkt
