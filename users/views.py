from django.shortcuts import render_to_response, get_object_or_404
from users.models import User

# Create your views here.


def view_user(request, id):
    return render_to_response('view_user.html', {
        'user': get_object_or_404(User, id=id)
    })