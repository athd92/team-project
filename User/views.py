from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView
from django.views.generic import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'registration/login.html'


class UserRegisterView(FormView):
    """
    A view that handle the creation of a new user.
    """

    def post(self, request):
        """
        Handles the case information is passed through the form to the
         webserver.
        """
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f"Bienvenue {name}!")
            login(request, user)
            return redirect('Launch:index',)
        else:
            for elt in form.errors.as_data():
                messages.info(request, f"{elt}: {form.errors.as_data()[elt]}")
            return redirect('User:register',)

    def get(self, request):
        """
        Displays the webpage with the form when trying to access the page
         for the first time.
        """
        template_name = 'registration/register.html'
        form = UserCreationForm()
        return render(request, template_name, {'form': form})


class UserLogoutView(View):
    """
    Class based view to simply log out the user. Displays also a message.
    """

    def get(self, request):
        logout(request)
        messages.info(request, "Vous avez été déconnecté!")
        return redirect(reverse('Launch:index',))
