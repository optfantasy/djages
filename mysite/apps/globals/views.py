from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, render_to_response

from globals.utils import slugreverse

def home(request):
    """ Global homepage.  Redirects to user's profile page if authenticated, registration-signup
    otherwise. """

    if request.user.is_authenticated():
        return HttpResponseRedirect(slugreverse(request.user, "user-profile", args=[request.user.id]))
    else:
        context = {}

        return render_to_response("landing.html", context, context_instance=RequestContext(request))


def globals_logout(request):
    logout(request)
    return redirect("/")