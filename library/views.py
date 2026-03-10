
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
from .models import Book, BorrowRecord
from .forms import BorrowBookForm

@login_required  
def home(request):
    books = Book.objects.all()
    return render(request, 'library/home.html', {'books': books})


@login_required
def my_borrowed_books(request):
    """Show the current user the books they have borrowed (not returned)."""
    borrow_records = BorrowRecord.objects.filter(user=request.user, returned=False).select_related('book')
    return render(request, 'library/my_borrowed_books.html', {'borrow_records': borrow_records})


@login_required
def borrow_book(request, book_id): 
    book_instance = get_object_or_404(Book, id=book_id)
    error = None

    if request.method == 'POST':
        form = BorrowBookForm(request.POST)
        if form.is_valid():
            borrow = form.save(commit=False)
            borrow.user = request.user
            
            borrow.book = book_instance 
            
            if book_instance.available_copies > 0:
                book_instance.available_copies -= 1
                book_instance.save()
                borrow.save()
                return redirect('home')
            else:
                error = 'No copies available'
    else:
        # Pre-select the book 
        form = BorrowBookForm(initial={'book': book_instance})
    
    return render(request, 'library/borrow.html', {
        'form': form, 
        'error': error, 
        'book': book_instance # Passing  the book object 
    })