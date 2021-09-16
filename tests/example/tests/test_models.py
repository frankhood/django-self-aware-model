from __future__ import absolute_import, print_function, unicode_literals

import logging

from django.test import TestCase
from tests.example.models import ExampleAwareModel
from django.contrib.contenttypes.models import ContentType

logger = logging.getLogger(__name__)

# =======================================================================
# ./manage.py test tests.example.tests.test_models.ExampleAwareModelUnitTest
# =======================================================================
class ExampleAwareModelUnitTest(TestCase):
    def test_str(self):
        # =======================================================================
        # ./manage.py test tests.example.tests.test_models.ExampleAwareModelUnitTest.test_str
        # =======================================================================
        obj = ExampleAwareModel.objects.create(
            title="Title Example", subtitle="Subtitle Example"
        )
        self.assertEqual(obj.__str__(), f"{obj.title}")

    def test_get_ct(self):
        # =======================================================================
        # ./manage.py test tests.example.tests.test_models.ExampleAwareModelUnitTest.test_get_ct
        # =======================================================================
        obj = ExampleAwareModel.objects.create(
            title="Title Example", subtitle="Subtitle Example"
        )
        obj_content_type = ContentType.objects.get(model="exampleawaremodel")
        self.assertEqual(
            obj.get_ct(),
            obj_content_type
        )
    
    def test_get_ct_id(self):
        # =======================================================================
        # ./manage.py test tests.example.tests.test_models.ExampleAwareModelUnitTest.test_get_ct_id
        # =======================================================================
        obj = ExampleAwareModel.objects.create(
            title="Title Example", subtitle="Subtitle Example"
        )
        obj_content_type = ContentType.objects.get(model="exampleawaremodel")
        self.assertEqual(
            obj.get_ct_id(),
            obj_content_type.pk
        )

    def test_get_app_label(self):
        # =======================================================================
        # ./manage.py test tests.example.tests.test_models.ExampleAwareModelUnitTest.test_get_app_label
        # =======================================================================
        obj = ExampleAwareModel.objects.create(
            title="Title Example", subtitle="Subtitle Example"
        )
        obj_content_type = ContentType.objects.get(model="exampleawaremodel")
        self.assertEqual(
            obj.get_app_label(),
            obj_content_type.app_label
        )

    def test_get_model_name(self):
        # =======================================================================
        # ./manage.py test tests.example.tests.test_models.ExampleAwareModelUnitTest.test_get_model_name
        # =======================================================================
        obj = ExampleAwareModel.objects.create(
            title="Title Example", subtitle="Subtitle Example"
        )
        obj_content_type = ContentType.objects.get(model="exampleawaremodel")
        self.assertEqual(
            obj.get_model_name(),
            obj_content_type.model
        )