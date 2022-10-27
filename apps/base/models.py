from django.db import models
import uuid

from sqlalchemy import null
class BaseModel(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    state           = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(null=True, default=None)
    user_created_at = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='%(class)s_created_at', null=True, default=None)
    user_updated_at = models.ForeignKey('authentication.User', on_delete=models.CASCADE, related_name='%(class)s_updated_at', null=True, default=None)

    class Meta:
        abstract = True