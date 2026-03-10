from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-books/', views.my_borrowed_books, name='my_borrowed_books'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
]
