from django.urls import path

from exam_project_web.auth_users.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDetailView, \
    ProfileDeleteView, ProfileUpdateView

urlpatterns = [
    path("registration/", RegisterUserView.as_view(), name="register_user"),
    path("login/", LoginUserView.as_view(), name="login_user"),
    path("logout/", LogoutUserView.as_view(), name="logout_user"),
    path("details/<int:pk>", ProfileDetailView.as_view(), name="details_user"),
    path("delete/<int:pk>", ProfileDeleteView.as_view(), name="delete_user"),
    path("edit/<int:pk>", ProfileUpdateView.as_view(), name="update_user"),
]