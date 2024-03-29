from django.db import models

from self_aware_model.models import SelfAwareModelMixin
from tests.example.managers import ExampleAwareModelManager
from tests.example.querysets import ExampleAwareModelQuerySet


class ExampleAwareModel(SelfAwareModelMixin, models.Model):
    objects = ExampleAwareModelManager.from_queryset(ExampleAwareModelQuerySet)()

    title = models.CharField("Title", max_length=255)
    subtitle = models.CharField("Sub Title", max_length=255, blank=True, default="")

    class Meta:
        """Example Aware Model Meta."""

        verbose_name = "Example Aware Model"
        verbose_name_plural = "Example Aware Models"

    def __str__(self) -> str:
        return self.title
