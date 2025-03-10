from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from AuthenticationApp.models import CustomUser

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def profile(request):

    user = request.user  # Get the currently logged-in user
    
    if request.method == "POST":
        # Handle the form submission to update the profile
        print(request.POST)  

        # Update profile-related fields if you have a related Profile model
        user.phonenumber = request.POST.get('phone', user.phonenumber)
        user.location = request.POST.get('location', user.location)
        user.membership = request.POST.get('membership', user.membership)
        user.occupation = request.POST.get('occupation', user.occupation)
        user.skills = request.POST.get('skills', user.skills)
        user.interest = request.POST.get('interests', '').split(',')
        user.membership = request.POST.get('membership', user.membership)

        # Save the changes
        user.save()
        print(user)
        print(f"Updated user: {user.interest},{user.phonenumber}, {user.location}, {user.membership}, {user.occupation}, {user.skills}")  # Log updated user details

        # Display a success message
        messages.success(request, "Your profile has been updated successfully!")

        # Redirect to the same profile page
        return redirect('profile')  # Redirect back to the profile page
    # patch for the interest list.
    user_interests = user.interest.strip("[]").replace("'","").split(',')

    return render(request, 'profile.html', {
        'user': user,
        'MEMBERSHIP_CHOICES': CustomUser.MEMBERSHIP_CHOICES,
        'interests': CustomUser.INTEREST_CHOICES,
        'user_interests':user_interests
    })

# @login_required
# def workspace_view(request):
#     if request.user.membership == 'workspace':  # Only for Creative Workspace Members
#         return render(request, 'workspace.html')
#     else:
#         return redirect('no_access')  # Redirect users without access