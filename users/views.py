from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
	if request.method == 'POST': # Checks if the form data are POST data when we submit. [datum--data]
		form = UserRegisterForm(request.POST) # If it is, then runs form = ......(request.POST)
		if form.is_valid():
			form.save()																												
			username = form.cleaned_data.get('username')
			messages.success(request, f'Thank you, {username}! Your account has been created! You are now able to log in')
			return redirect('login')

	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required # ei decorator use korle settings e LOGIN_URL = 'login' setup kore dite hobe.
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, 
			                       request.FILES, 
			                       instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.info(request, f'Your profile has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context ={
	    'u_form': u_form,
		'p_form': p_form
		}
	return render(request, 'users/profile.html', context)


