from . import views
from django.urls import path

app_name = "testdb"
urlpatterns = [
    path("/", views.index, name = "index"),
    path("/<int:product_id>/<int:account_id>/create", views.create, name="create"),
    path("/get_student", views.get_student, name="get_student"),
    path("/create_student", views.create_student, name="create_student"),
    path("/one_student", views.one_student, name="one_student"),
    path("/create_Customer", views.create_Customer, name="create_Customer"),
    path("/get_address", views.get_address, name="get_address"),
    path("/register_address", views.register_address, name="register_address"),
    path("/image_request", views.image_request, name="image_request"),
]