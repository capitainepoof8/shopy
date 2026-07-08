# defits creer un gestionnaire de biblioteque 

livre = [
    {"number": 1, "name": "Alice in Borderland"},
    {"number": 2, "name": "The Alchemist"},
    {"number": 3, "name": "1984"},
    {"number": 4, "name": "To Kill a Mockingbird"},
    {"number": 5, "name": "The Great Gatsby"},
    {"number": 6, "name": "Harry Potter and the Philosopher's Stone"},
    {"number": 7, "name": "The Hobbit"},
    {"number": 8, "name": "The Lord of the Rings"},
    {"number": 9, "name": "The Catcher in the Rye"},
    {"number": 10, "name": "The Little Prince"},
    {"number": 11, "name": "The Da Vinci Code"},
    {"number": 12, "name": "The Hunger Games"},
    {"number": 13, "name": "Pride and Prejudice"},
    {"number": 14, "name": "The Chronicles of Narnia"},
    {"number": 15, "name": "A Game of Thrones"},
    {"number": 16, "name": "The Kite Runner"},
    {"number": 17, "name": "The Book Thief"},
    {"number": 18, "name": "The Fault in Our Stars"},
    {"number": 19, "name": "Rich Dad Poor Dad"},
    {"number": 20, "name": "Atomic Habits"}
]


def user_name():
    user_name = input("enter your user name : ")
    
    if user_name  =="":
        return
    if not user_name.format:
        return
    
def password():
    password = input("enter your password: ")
    if user_name  =="":
        return
    if not password.isdigit:
        return
    
def login():
    login = user_name()+ password()
    
    
def add():
    add = input(f"enter the number of the book you want")
    if add  =="":
        return
    if not add.isdigit():
        print("Numéro invalide.")
        return
    
def main():
    print("======================welcome new user ====================")
    login()