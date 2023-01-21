
from django.urls import path
from myapp import views

# http://127.0.0.1/ -> myapp -> views 로 위임
# http://127.0.0.1/app/

# http://127.0.0.1/create/
# http://127.0.0.1/read/1/

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('delete/', views.delete),
    path('update/<id>/', views.update),
]
