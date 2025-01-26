book_list=[]
n = int(input("Enter the Number of Books to be in the List: "))
for i in range (0,n):
    bookname = str(input("Enter the Book name:"))
    book_list.append(bookname)
print(book_list)
count = 0
for book in book_list:
    if(len(book) >25):
      count+=1
print("Toatl count of Books titles longer that 25 charaters:",count)
