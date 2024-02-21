from django.contrib.contenttypes.models import ContentType
from django.db import models


class SelfAwareModelMixin(models.Model):
    """
    Taken from http://www.slideshare.net/erics1/powerful-generic-patterns-with-django
    """

    def get_ct(self):
        """
        Returns the Content Type for this instance
        What is returned is cached by Django ---> self.__class__._cache[self.db][key]
        """
        return ContentType.objects.get_for_model(self)

    def get_ct_id(self):
        """Returns the id of the Content Type for this instance"""
        return self.get_ct().pk

    def get_app_label(self):
        """Returns the app_label of the Content Type for this instance"""
        return self.get_ct().app_label

    def get_model_name(self):
        """Returns the model_name from the Content Type for this instance"""
        return self.get_ct().model

    class Meta:
        abstract = True
