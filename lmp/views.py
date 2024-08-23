from django.shortcuts import render,redirect
from student.models import Student
from books.models import Books


def Add_student(request):
    if request.POST:
        studentroll=request.POST.get('studentroll')
        studentname=request.POST.get('studentname')
        address=request.POST.get('address')
        booktiti=request.POST.get('booktiti')
        bookpricet=request.POST.get('studyprogram')
        Students=Student(student_roll=studentroll,student_name=studentname,student_address=address,booktiti=booktiti,bookpricet=bookpricet)
        Students.save()
        return redirect("/add-student")
    
    return render(request,'add-student.html')

def add_book(request):
    if request.POST:
        bookstitle= request.POST.get('bookstitle')
        bookauther= request.POST.get('bookauther')
        bookprice= request.POST.get('bookprice')

        books= Books(book_title=bookstitle,book_auther=bookauther,book_price=bookprice)
        books.save()

        return redirect("/add-book")
    return render (request,'add-book.html')

def index(request):
    return render (request,'index.html')

def Students(request):
    Students= Student.objects.all()
    data={"data":Students}
    return render(request,'students.html',data)

def Book(request):
    Book= Books.objects.all()
    data={"data":Book}
    return render (request, 'books.html',data)

def Delete(request,id):
    Student.objects.get(id= id).delete()

    return redirect('/students')

def Deletet(request,id):
    Books.objects.get(id=id).delete()

    return redirect('/books')




























