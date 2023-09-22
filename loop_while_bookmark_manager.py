book = []
maxw = 5
while maxw > 0:
    web = input("Website name without http://")
    book.append(f"https://{web.lower().strip()}")
    maxw += 1
    print("website added")      
    print(book)
else:
    if len(book) > 0 :
        book.sort()
        index = 0
        print("printig all websits ")
        while index < len(book):
            print(book[index])
            index +=1