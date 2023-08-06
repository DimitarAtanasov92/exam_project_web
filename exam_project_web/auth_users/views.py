from django.shortcuts import render
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import mixins as auth_mixins
from django.urls import reverse_lazy
from django.views import generic as views
from django.utils.translation import gettext_lazy as _

from exam_project_web.FashionForEveryone.models import UserModel, Profile


# Create your views here.

class RegisterUserForm(auth_forms.UserCreationForm):
    content = forms.BooleanField()
    first_name = forms.CharField(
        max_length=30,
        required=True,
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=_("Repeat password!!!"),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.help_text = _("It works")

    def save(self, commit=True):
        user = super().save(commit)

        profile = Profile(first_name=self.cleaned_data["first_name"],
                          user=user, )
        if commit:
            profile.save()

        return user

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ("email",)


class RegisterUserView(views.CreateView):
    template_name = "register.html"
    form_class = RegisterUserForm
    success_url = reverse_lazy("register_user")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = "login.html"


class LogoutUserView(auth_views.LogoutView):
    pass


UserModel = get_user_model()


@login_required
def func_view(request):
    pass


class ViewWithPermission(auth_mixins.PermissionRequiredMixin, views.TemplateView):
    template_name = "user_list.html"


class UserListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = "user_list.html"
