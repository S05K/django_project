from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "user"
urlpatterns = [
    path("/", views.index,name="index"),
    path("/login", views.login, name="login"),
    path("/home", views.home, name="home"),
    path("/jobs", views.jobs, name="jobs"),
    path("/get_user", views.get_user, name="get_user"),
    path("/<int:user_id>/<int:job_id>/apply_for_job", views.apply_for_job, name="apply_for_job"),
    path("/forgot_password", views.forgot_password, name="forgot_password"),
    path("/find_email", views.find_email, name="find_email"),
    path('/reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path("/update_password/update_password/<uidb64>/<token>/", views.update_password, name="update_password"),
    path("/search_jobs", views.search_jobs, name="search_jobs"),
    # path('user/reset_password/<str:uid>/<str:token>/', views.reset_password, name='reset_password'),
    # path("/reset_password/<int:uid>/<token>", views.reset_password, name="reset_password"),
    # path("/reset_password", views.reset_password, name="reset_password"),


]