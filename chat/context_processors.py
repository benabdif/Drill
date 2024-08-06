from .models import Group

def user_groups(request):
    if request.user.is_authenticated:
        user_groups = Group.objects.filter(members=request.user)
    else:
        user_groups = Group.objects.none()
    return {'user_groups': user_groups}
