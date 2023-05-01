from django.contrib.auth.views import LoginView
from django.views.generic import FormView

from authentication.forms import SignUpForm


class SignUpView(FormView):
    template_name = 'auth/signup.html'
    form_class = SignUpForm
    success_url = '/'

    def form_valid(self, form):
        """
        If the form is valid, save the user
        """
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        If the form is invalid, re-render the page
        """
        return super().form_invalid(form)


class SignInView(LoginView):
    template_name = 'auth/signin.html'
    success_url = '/'
    redirect_authenticated_user = True


