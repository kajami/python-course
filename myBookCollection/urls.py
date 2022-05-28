from django.contrib import admin
from django.urls import path
from bookCollectionApp import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
    path('books/', views.BookListView.as_view(), name='bookList'),
    path('book/<int:pk>', views.BookDetailView.as_view()),
    path('book/update/<int:pk>', views.BookUpdateView.as_view()),
    path('book/delete/<int:pk>', views.BookDeleteView.as_view()),
    path('books/book/create/', views.BookCreateView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #for creating url to the image path 
