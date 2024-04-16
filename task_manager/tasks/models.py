from django.db import models

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    """Tasks."""
    title = models.CharField(_('Имя'), max_length=100, unique=True)
    describe = models.TextField(_('Описание'), blank=True, null=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=_('Статус')
    )
    creator = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name=_('Создатель'),
        related_name='creator_id'
    )
    executor = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        verbose_name=_('Исполнитель'),
        related_name='executor_id',
        blank=True,
        null=True
    )
    label = models.ManyToManyField(Label, verbose_name='Метки',
                                   blank=True, related_name='labels',
                                   null=True)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.title