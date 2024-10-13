from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from .models import Group



@receiver(m2m_changed, sender=Group.members.through)
def validate_dm_group_members(sender, instance, action, pk_set, **kwargs):
    if instance.is_dm:
        if action == "pre_add":
            if (instance.members.count() + len(pk_set)) > 2:
                raise ValidationError("A direct message group cannot have more than 2 members.")
        elif action == "pre_remove":
            if (instance.members.count() - len(pk_set)) > 2:
                raise ValidationError("A direct message group cannot have more than 2 members.")