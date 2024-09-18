from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import UserRegisterForm


class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy("kombuchacalendar:index")
    template_name = "registration/signup.html"

    def register(self, request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                messages.info(request, "Thanks for signing up. You are now logged in.")
                new_user = authenticate(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        )
                login(request, new_user)
                return redirect(self.success_url)
        else:
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form': form})



    # def form_valid(self, form):
    #     valid = super(SignUpView, self).form_valid(form)
    #     email, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
    #     user = authenticate(email=email, password=password)
    #     login(self.request, user)
    #     return valid

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Account created for {username}')
    #
    #         return redirect(reverse_lazy('kombuchacalendar:index'))
    #
    #     return render(request, self.template_name, {"form": form})
    #
    # def form_valid(self, form):
    #     # create user object
    #     user = form.save(commit=False)
    #     # set password manually
    #     # otherwise User will be saved with unhashed password
    #     user.set_password(form.cleaned_data.get("password"))
    #     # save user object to database
    #     user.save()
    #     # get email and password
    #     email = form.cleaned_data.get("email")
    #     password = form.cleaned_data.get("password")
    #     # authenticate your user with unhashed password, because 'authenticate' hashes it again
    #     authenticated_user = authenticate(email=email, password=password)
    #     # log in
    #     login(self.request, authenticated_user)
    #     return redirect(self.success_url)
