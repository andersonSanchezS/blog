from django.db import models
from apps.base.models import BaseModel
from apps.authentication.api.models.permission.index import Permission
from apps.authentication.api.models.role.index import Role


class RolePermission(BaseModel):
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    role       = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        db_table = 'rolePermissions'
        verbose_name = 'rolePermission'
        verbose_name_plural = 'rolePermissions'
        ordering = ['created_at']
