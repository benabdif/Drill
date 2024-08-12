from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Message, Group

User = get_user_model()


@login_required
def chat_home(request):
    groups = Group.objects.filter(members=request.user)
    context = {
        "groups": groups,
    }
    return render(
        request=request,
        template_name="chat/chat.html",
        context=context,
    )


@login_required
def user_chat(request, group_id):
    group = get_object_or_404(Group, id=group_id, members=request.user)
    messages = group.message_set.filter(is_deleted=False).order_by("-timestamp")

    paginator = Paginator(messages, 25)
    page_number = request.GET.get("p", 1)

    json = request.GET.get("json")
    page_obj = paginator.page(page_number)

    if json == "true":
        messages_data = [
            {
                "sender": msg.sender.username,
                "profile": msg.sender.userprofile.picture.url,
                "content": msg.content,
                "id": msg.id,
                "timestamp": msg.timestamp.isoformat(),
                "is_read": msg.is_read,
            }
            for msg in page_obj
        ]
        return JsonResponse(
            {
                "messages": messages_data,
                "has_next": page_obj.has_next(),
            },
        )

    return render(
        request,
        "chat/user_chat.html",
        {
            "page_obj": page_obj,
            "group": group,
        },
    )
