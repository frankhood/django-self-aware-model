=====
Usage
=====

To use Django Self Aware Model in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_self_aware_model.apps.DjangoSelfAwareModelConfig',
        ...
    )

Add Django Self Aware Model's URL patterns:

.. code-block:: python

    from django_self_aware_model import urls as django_self_aware_model_urls


    urlpatterns = [
        ...
        url(r'^', include(django_self_aware_model_urls)),
        ...
    ]
