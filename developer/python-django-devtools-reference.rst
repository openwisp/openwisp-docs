Python/django dev tools reference
=================================

In this page, we aim at helping technical users and contributors to work
on OpenWISP and we introduce to some python tools they might find very
useful during development and debugging.

Python and its advantages
-------------------------

As you may already know, `Python <https://www.python.org>`_ is a
programming language, more specifically an interpreted high-level
programming language for general-purpose programming. It is also widely
used these days! Big companies like Google, Disney and Dropbox make
excessive use of this programming language! You'll know why in a moment.

- To begin with, the syntax in python helps programmers to do
  coding in fewer steps as compared to other languages such as
  Java or C++ because it uses relatively less lines and words
  while still performing the same operations.
- Additionally, python offers excellent readability and uncluttered
  simple-to-learn syntax which helps beginners to utilize this
  programming language.
- Also, python has a large standard library full of pre-defined
  functions which can help fulfil tasks related to string operations,
  Internet, web service tools, operating system interfaces and protocols
  a lot more quickly and easily.
- Believe it or not, the python language is licensed under an
  OSI-approved open source license, which makes it free to use and
  distribute, including for commercial purposes!
- Python provides powerful data types which can be used to construct
  flexible and fast data structures.
- Python is widely used in the networking and configuration management
  world as famous libraries such as
  `networkx <https://networkx.github.io>`_,
  `ansible <https://www.ansible.com>`_,
  `salt <https://docs.saltstack.com/en/latest/topics/>`_,
  `paramiko <http://www.paramiko.org>`_ and
  `fabric <http://www.fabfile.org>`_ make use of it.
- Finally, finding developers who know python is very easy and allows for
  the project to expand which allows the community to grow considerably
  over time.

So, did all these advantages make your mouth watery yet? If you want to
learn python as a programming language, you can try taking a look quickly
`there <https://www.learnpython.org>`_ or consider checking out the
python course on `SoloLearn <https://www.sololearn.com>`_ for a more
detailed beginner course.

Django
------

`Django <https://www.djangoproject.com/start/>`_ is a high-level Python
Web framework which encourages rapid development and clean, pragmatic
design. It takes care of much of the hassle of Web development and is
free and open source.

In OpenWISP we chose Django mainly for these reasons:

- It has a rich ecosystem and pluggable apps which allow us to get a lot
  done very fast.
- It has been battle tested over many years by a high amount of people and
  high profile companies.
- Security vulnerabilities are usually privately disclosed to the
  developers and quickly fixed.
- With it being popular, it's easy to find python developers who have
  experience with django and can contribute to OpenWISP.

You can get started with django by following `this tutorial
<https://www.djangoproject.com/start/>`_ or `this one
<https://pythonprogramming.net/web-development-tutorials/>`_.

Django REST framework
---------------------

`Django REST framework <https://www.django-rest-framework.org>`_
is a powerful and flexible toolkit for building Web APIs and it's used
and trusted by internationally recognised companies including Mozilla,
Red Hat, Heroku, and Eventbrite.

Here are some reasons why you would want to use the REST framework:

- Simplicity, flexibility, quality, and test coverage of source code.
- Powerful serialization engine compatible with both ORM and non-ORM
  data sources.
- Clean, simple, views for Resources, using Django's new class based
  views.
- HTTP response handling, content type negotiation using HTTP Accept
  headers.
- Publishing of metadata along with querysets.

Thus, DRF has the flexibility to extend and customize the framework’s
tools according to programmer’s demands which greatly reduces
development time. You can find some more details with examples
`on the official DRF website <https://www.django-rest-framework.org>`_
or consider checking out the DRF tutorial along with some other
tutorials on `this website <https://wsvincent.com/>`_.

Django Extensions
-----------------

`Django Extensions <https://django-extensions.readthedocs.io/>`_ is a
collection of custom extensions for the Django Framework. These include
management commands, additional database fields, admin extensions and
much more but we will focus on 2 of them for now, namely
``shell_plus`` and ``runserver_plus``.

Django Extensions can be installed with:

``pip install django-extensions``

`shell_plus
<django-extensions.readthedocs.io/en/latest/shell_plus.html>`_:
Django shell with autoloading of the apps database models and subclasses
of user-defined classes.

`runserver_plus
<django-extensions.readthedocs.io/en/latest/runserver_plus.html>`_:
Typical runserver with Werkzeug debugger baked in.

Django Debug Toolbar
--------------------

The `Django Debug Toolbar <https://django-debug-toolbar.readthedocs.io/>`_
is a configurable set of panels which display various debug information
about the current request/response and, when clicked, display more details
about the panel’s content.

It can be installed with:

``pip install django-debug-toolbar``

More details can be found on its `website
<https://django-debug-toolbar.readthedocs.io/en/latest/>`_
or on `pypi <https://pypi.org/project/django-debug-toolbar/>`_.

IPython and ipdb
----------------

`IPython <https://ipython.org>`_ (Interactive Python) is a command shell
for interactive computing in multiple programming languages, originally
developed for the Python programming language, which offers introspection,
rich media, shell syntax, tab completion, and history.

It provides:

- A powerful interactive shell.
- A browser-based notebook interface with support for code, text,
  mathematical expressions, inline plots and other media.
- Support for interactive data visualization and use of GUI toolkits.
- Flexible, embeddable interpreters to load into one's own projects.
- Tools for parallel computing.

More details including installation and updates can be found on the
`official webite <https://ipython.org>`_ and a simple usage tutorial
can be found `here <http://cs231n.github.io/ipython-tutorial/>`_.

As for ipdb, it exports functions to access the IPython debugger. It
comes along with ipython. More details about ipdb can be obtained
on `its pypi page <https://pypi.org/project/ipdb/>`_.

How to add these tools to an OpenWISP development environment
-------------------------------------------------------------

These tools can be added to an OpenWISP development environment and
significantly improve the efficiency and experience while developing.
Let's do a walkthrough of how to use them in `OpenWISP Controller
<https://github.com/openwisp/openwisp-controller>`_ as an example. In the
``tests/`` folder, ``local_settings_example.py`` must be copied and
renamed to ``local_settings.py`` which we will use for customization.
This technique can be used in other OpenWISP development environments too.

.. code-block:: bash

  cd tests/
  cp local_settings_example.py local_settings.py

To start, the `steps <https://github.com/openwisp/openwisp-controller>`_
for installing OpenWISP Controller must be followed. The commands
``pipenv run ./manage.py migrate`` and
``pipenv run ./manage.py createsuperuser`` must be run and
``SPATIALITE_LIBRARY_PATH`` should be specified in the
``local_settings.py`` file.

To start the development server, run ``python manage.py runserver_plus``
which will provide more debugging information.

Also, ``ipython`` can be used along ``shell_plus`` by running the command
``./manage.py shell_plus --ipython`` in the terminal. This will provide
an interactive shell for running code in python.

To debug the code, ``ipdb`` can be used. Commands similar to
``ipdb mymodule.py`` may be used to carry out that process. A
list of lines where errors have been found or lines which can be further
optimized will be returned.

Lastly, ``django-debug-toolbar`` may be used along to display information
about processes occuring on the website. To achieve that, some code needs
to be added to our current module, i.e ``openwisp-controller``. To begin,
the lines ``'debug_toolbar'`` and
``'debug_toolbar.middleware.DebugToolbarMiddleware'`` need to be added
to the ``INSTALLED_APPS`` and to the``MIDDLEWARE`` settings respectively
and the line ``INTERNAL_IPS = ('127.0.0.1')`` should be mentioned else
the django debug toolbar won't be displayed. We also need to import
``django_extensions`` and add it to our ``INSTALLED_APPS`` setting but
this is already done in ``settings.py``. Here's what ``local_settings.py``
will roughly look like at the end:

.. code-block:: python
  
    from django.conf import settings

    settings.INSTALLED_APPS += [
        'debug_toolbar',
        #django_extensions
	# already enabled in openwisp-controller, you may need to
	# uncomment the previous line in other development environments
    ]

    # This setting is specific for openwisp-controller.
    # Other OpenWISP development environments might not need it.
    SPATIALITE_LIBRARY_PATH = 'mod_spatialite'
    
    settings.MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    ]

    INTERNAL_IPS = ('127.0.0.1')

To complete the process, the Debug Toolbar’s URL needs to be added
to the URLconf of ``openwisp-controller`` as shown in `this
<django-debug-toolbar.readthedocs.io/en/latest/installation.html>`_
tutorial but this is already present in the last lines of ``urls.py``:

.. code-block:: python

    if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar
    	    urlpatterns += [
    	        url(r'^__debug__/', include(debug_toolbar.urls))
	    ]

Now, logging to http://127.0.0.1:8000 and inputting the credentials we created
earlier, something similar should be shown:

.. image:: ../images/intro/DDT.jpg
   :scale: 50%
   :align: center

And that's how you integrate these tools with OpenWISP modules. Try
to experiment and do the same for other modules!
