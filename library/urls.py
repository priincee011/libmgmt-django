from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('borrow/', views.borrow_book, name='borrow_book'),
    path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
]
