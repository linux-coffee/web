from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('aboutme/',views.aboutme,name='aboutme'),
    path('contactme/',views.contactme,name='contactme'),
    path('detail/<int:todo_id>/',views.detail,name='details'),
    path('delete/<int:todo_id>/',views.delete,name='delete'),
    path('update/<int:todo_id>/',views.update,name='update'),
    path('create/',views.create,name='create'),
]