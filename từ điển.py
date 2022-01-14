databasee = {
    "home": "ngoi nha",
    "baby": "em be"
}

def show_menu():
    print("-" * 50)
    print("TRUONG TRINH TU DIEN")
    print("-" * 50)
    print("1. Them tu")
    print("2. Tim tu")
    print("3. Xoa tu")
    print("4. Xem tat ca")
    print("An 0 de thoat truong trinh")

def add():
    word = input('tu moi: ')
    mean = input('nghia cua tu: ')
    databasee[word] = mean
    print('+Tu moi da duoc them')

def find():
    word = input("tu gi: ")
    if word in databasee:
        print("Tim thay: [ %s: %s ]" % (word, databasee[word]))
    else:
        print('Khong tim thay tu: [ %s ]' % word)

def delete():
    word = input('tu gi: ')
    if word in databasee:
        del databasee[word]
        print("Tu [ %s ] da bi xoa" % word)
    else:
        print('Khong tim thay tu: [ %s ]' % word)

def view_all():
    for word, mean in databasee.items():
        print('[ %s: %s ]' % (word, mean))

show_menu()

choice = int(input("Ban muon lam gi? "))

while choice != 0:
    if choice == 0:
        break
    elif choice == 1:
        add()
    elif choice == 2:
        find()
    elif choice == 3:
        delete()
    elif choice == 4:
        view_all()
    else:
        print(" Khong co lua chon nay!")
    choice = int(input("Ban muon lam gi? "))
print("Hen gap lai")