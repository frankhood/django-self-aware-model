=============================
Django Self Aware Model
=============================

.. image:: https://badge.fury.io/py/django-self-aware-model.svg
    :target: https://badge.fury.io/py/django-self-aware-model

.. image:: https://travis-ci.org/frankhood/django-self-aware-model.svg?branch=master
    :target: https://travis-ci.org/frankhood/django-self-aware-model

.. image:: https://codecov.io/gh/frankhood/django-self-aware-model/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/frankhood/django-self-aware-model

Your project description goes here

Documentation
-------------

The full documentation is at https://django-self-aware-model.readthedocs.io.

Quickstart
----------

Install Django Self Aware Model::

    pip install django-self-aware-model

Add it to your `INSTALLED_APPS`:

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

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
