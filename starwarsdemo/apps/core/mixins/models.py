from django.db import models
from django.utils.text import gettext_lazy as _


class TimeStampedMixin(models.Model):
    """
    TimeStampedMixin add fields `created_at` and `updated_at` to the model
    """

    created_at = models.DateTimeField(
        _("Created At"),
        auto_now_add=True,
        editable=False
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
        auto_now_add=False,
        editable=False
    )

    class Meta:
        abstract = True
