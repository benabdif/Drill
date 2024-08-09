from .models import Group

def user_groups(request):
    if request.user.is_authenticated:
        user_groups = Group.objects.filter(members=request.user)
        for group in user_groups:
            if group.is_dm:
                other_member = group.members.exclude(id=request.user.id).first()
                group.name = other_member.username if other_member else None
    else:
        user_groups = Group.objects.none()
    return {'user_groups': user_groups}
