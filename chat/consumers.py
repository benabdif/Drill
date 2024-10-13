import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .models import Message, Group

User = get_user_model()


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        if not self.user.is_authenticated:
            await self.close(code=4003, reason="Authentication required")
            return

        self.group_id = self.scope["url_route"]["kwargs"]["group_id"]
        self.group_obj = await self.get_group(self.user.id, self.group_id)

        if not self.group_obj:
            await self.close(
                code=123,
                reason="You aren't allowed to message this user.",
            )
            return

        self.room_group_name = f"chat_{self.group_obj.id}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, "room_group_name"):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name,
            )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if "message" in text_data_json:
            # Handle new message
            message_content = text_data_json["message"]
            new_message = await self.save_message(
                self.user.id,
                self.group_obj.id,
                message_content,
            )
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": new_message,
                },
            )
        elif "edit_message" in text_data_json:
            # Handle message editing
            message_id = text_data_json["edit_message"]["id"]
            new_content = text_data_json["edit_message"]["content"]
            updated_message = await self.edit_message(
                self.user.id,
                message_id,
                new_content,
            )
            if updated_message:
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        "type": "chat_message",
                        "message": updated_message,
                    },
                )
        elif "delete_message" in text_data_json:
            message_id = text_data_json["delete_message"]
            deleted_message = await self.delete_message(
                self.user.id,
                message_id,
            )
            if deleted_message:
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        "type": "chat_message",
                        "message": deleted_message,
                    },
                )
        elif "read_receipt" in text_data_json:
            # Handle read receipt
            message_id = text_data_json["read_receipt"]
            await self.mark_message_as_read(message_id)
            # Notify group about the read receipt
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "message_read_receipt",
                    "message_id": message_id,
                    "user": self.user.username,
                },
            )

    async def chat_message(self, event):
        message = event["message"]
        await self.send(
            text_data=json.dumps(message),
        )

    async def message_read_receipt(self, event):
        message_id = event["message_id"]
        user = event["user"]
        await self.send(
            text_data=json.dumps(
                {
                    "type": "message_read_receipt",
                    "message_id": message_id,
                    "user": user,
                }
            ),
        )

    @database_sync_to_async
    def save_message(self, sender_id, group_id, content):
        message = Message.objects.create(
            sender_id=sender_id,
            group_id=group_id,
            content=content,
        )
        return {
            "content": message.content,
            "is_read": message.is_read,
            "sender": message.sender.username,
            "profile": message.sender.userprofile.picture.url,
            "timestamp": message.timestamp.isoformat(),
            "id": str(message.id),
            "type": "chat_message"
        }

    @database_sync_to_async
    def edit_message(self, sender_id, message_id, new_content):
        try:
            message = Message.objects.get(id=message_id, sender_id=sender_id)
            message.content = new_content
            message.is_updated = True
            message.save()
            return {
                "content": message.content,
                "is_read": message.is_read,
                "sender": message.sender.username,
                "profile": message.sender.userprofile.picture.url,
                "timestamp": message.timestamp.isoformat(),
                "id": str(message.id),
                "type": "message_edited",
                "is_updated": message.is_updated,
                "updated_at": message.updated_at.isoformat(),
            }
        except ObjectDoesNotExist:
            return None

    @database_sync_to_async
    def delete_message(self, sender_id, message_id):
        try:
            message = Message.objects.get(id=message_id, sender_id=sender_id)
            message.is_deleted = True
            message.save()
            return {
                "id": str(message.id),
                "type": "message_deleted",
            }
        except ObjectDoesNotExist:
            return None

    @database_sync_to_async
    def get_group(self, user_id, group_id):
        try:
            return Group.objects.get(
                id=group_id,
                members__id=user_id,
            )
        except ObjectDoesNotExist:
            return None

    @database_sync_to_async
    def mark_message_as_read(self, message_id):
        try:
            message = Message.objects.get(id=message_id)
            if message.sender != self.user:
                message.is_read = True
                message.save()
        except ObjectDoesNotExist:
            pass
