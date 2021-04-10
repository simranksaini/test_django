from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from .forms import SignUpForm


class UserView(DetailView):
    template_name = './profile.html'

    def get_object(self):
        return self.request.user


class TotalView(DetailView):
    template_name = './total.html'

    def get_object(self):
        return self.request.user

    def series(self, request, x, n):
        if(x == 0):
            return
        sum = 0.0
        for i in range(1, n+1):
            sum += 1.0/power(x, i)
        return render(request, "./total.html", context={"sum": sum})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, email=user.email,
                                password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")
            return redirect('users:profile')
    else:
        form = SignUpForm()
    return render(request, './signup.html', {'form': form})


def power(base, exp):
    if(exp == 0):
        return(1)
    if(exp == 1):
        return(base)
    if(exp != 1):
        return(base*power(base, exp-1))
