from django.db import models

from django.contrib.auth.models import User

from automaton.settings.local import REPOSITORY_DIRS


class Repositories(models.Model):
    name = models.CharField(
        max_length=100,
    )
    path = models.FilePathField(
        path=REPOSITORY_DIRS,
        allow_files=False,
        allow_folders=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    creator = models.ForeignKey(
        User,
        related_name='creator',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    modified = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        unique_together = ('creator', 'name')
