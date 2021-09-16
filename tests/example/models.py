from tests.example.querysets import ExampleAwareModelQuerySet
from tests.example.managers import ExampleAwareModelManager
from django.db import models
from django_self_aware_model.models import SelfAwareModelMixin


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

