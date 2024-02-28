from django.urls import path
from . import views

urlpatterns = [
    path("", views.Create.as_view(), name= "create"),
    path("list/", views.List.as_view(), name= "list"),
    path("update/<int:pk>", views.Update.as_view(), name= "update"),
    path("delete/<int:pk>", views.Delete.as_view(), name= "delete")
]