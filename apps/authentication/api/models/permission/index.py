from django.db import models
from apps.base.models import BaseModel


class Permission(BaseModel):

    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'permissions'
        verbose_name = 'permission'
        verbose_name_plural = 'permissions'
        ordering = ['created_at']
