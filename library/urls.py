from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("add_book/", views.add_book, name="add_book"),
    path("view_books/", views.view_books, name="view_books"),
    path("view_registeredusers/", views.view_registeredusers, name="view_registeredusers"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("view_issued_book/", views.view_issued_book, name="view_issued_book"),
    path("registereduser_issued_books/", views.registereduser_issued_books, name="registereduser_issued_books"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("guest_user/", views.guest_books, name="guest_user"),

    path("registereduser_registration/", views.registereduser_registration, name="registereduser_registration"),
    path("change_password/", views.change_password, name="change_password"),
    path("registereduser_login/", views.registereduser_login, name="registereduser_login"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),

    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("delete_registereduser/<int:myid>/", views.delete_registereduser, name="delete_registereduserr"),
]