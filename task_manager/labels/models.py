from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    """Statuse for Task."""
    title = models.CharField(_('Имя'), max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(_('Дата создания'), auto_now_add=True)

    def __str__(self):
        return self.title