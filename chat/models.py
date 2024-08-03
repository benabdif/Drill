import ulid
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

"""
? Chatting Database Desgin

Message:
    * sender: User
    * group: Group
    * content: str
    * timestamp: Datetime
    is_updated: bool
    updated_at: Datetime
    is_read: bool
    attachments: MessageAttachment

Attachment:
    message: Messasge
    file: FileField

Group:
    * name
    * description
    * memebers: Users
    * is_dm: bool
"""


def validate_file_size(value):
    max_size = 10 * 1024 * 1024  # 10MB
    if value.size > max_size:
        raise ValidationError("File size must be under 10MB.")


class Group(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=ulid.ULID,
        editable=False,
    )
    name = models.CharField(
        max_length=255,
        blank=True,
    )
    description = models.TextField(
        blank=True,
    )
    members = models.ManyToManyField(
        User,
    )
    is_dm = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return self.name if self.name else f"Group {self.id}"


class Message(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=ulid.ULID,
        editable=False,
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    content = models.TextField(
        max_length=5000,
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        db_index=True,
    )
    is_updated = models.BooleanField(
        default=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )
    is_read = models.BooleanField(
        default=False,
    )
    is_deleted = models.BooleanField(
        default=False,
    )

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return f"Message from {self.sender} to {self.group} at {self.timestamp}"


class MessageAttachment(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=ulid.ULID,
        editable=False,
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="attachments",
    )
    file = models.FileField(
        upload_to="chat/messages/attachments/",
        max_length=255,
        validators=[validate_file_size],
    )

    def __str__(self):
        return f"Attachment {self.file_name} for message {self.message.id}"
