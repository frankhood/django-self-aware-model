=====
Usage
=====

To use Django Self Aware Model in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'self_aware_model',
        ...
    )

Add Django Self Aware Model's URL patterns:

.. code-block:: python

    from self_aware_model import urls as self_aware_model_urls


    urlpatterns = [
        ...
        url(r'^', include(self_aware_model_urls)),
        ...
    ]
