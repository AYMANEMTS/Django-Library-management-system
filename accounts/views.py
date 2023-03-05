

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileForm
from .models import User
from django.contrib.auth import update_session_auth_hash

class MyLoginView(LoginView):
    template_name = 'login.html'

class MyLogoutView(LoginRequiredMixin, LogoutView):
  next_page = reverse_lazy('login')

class MyRegisterView(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('profile')
    template_name = 'register.html'

    def form_valid(self, form):
        valid = super().form_valid(form)
        email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        user = authenticate(self.request, email=email, password=password)
        login(self.request, user)
        return valid

class MyProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user
    
    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        if password:
            user.set_password(password)
            update_session_auth_hash(self.request, user)

            # logout and redirect to login if password was changed
            logout(self.request)
            return redirect('login')

        user.save()
        
        return redirect(self.success_url)
