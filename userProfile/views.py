from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context_processors import csrf
from pip._vendor.requests import auth
from userProfile.models import UserProfile, Relationship, RELATIONSHIP_FOLLOWING


def users(request):
    all_users = UserProfile.objects.all()
    args = {}
    args.update(csrf(request))
    args['users'] = all_users
    args['username'] = request.user.username
    # beret is UserProfile vse danniye
    return render_to_response('users.html', args)


def followUser(request, user_id):
    bacl_url = request.META.get('HTTP_REFERER')
    # dostaem usera is BD
    user_from = UserProfile.objects.get(id=1)
    user_to = UserProfile.objects.get(id=2)
    user_from.add_relationship(user_to, RELATIONSHIP_FOLLOWING)
    return redirect(bacl_url)