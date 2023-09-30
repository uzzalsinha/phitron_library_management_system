from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("book_addition/", views.book_addition, name="book_addition"),
    path("show_books/", views.show_books, name="show_books"),
    path("show_students/", views.show_students, name="show_students"),
    path("issue_book/", views.issue_book, name="issue_book"),
    path("show_issued_book/", views.show_issued_book, name="show_issued_book"),
    path("student_issued_books/", views.student_issued_books, name="student_issued_books"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),



    path("student_registration/", views.student_registration, name="student_registration"),
    path("change_password/", views.change_password, name="change_password"),
    path("student_login/", views.student_login, name="student_login"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("logout/", views.Logout, name="logout"),

    path("delete_book/<int:myid>/", views.delete_book, name="delete_book"),
    path("delete_student/<int:myid>/", views.delete_student, name="delete_student"),
]