Django is a high-level Python Web framework that encourages rapid development
and clean, pragmatic design. Thanks for checking it out.

All documentation is in the "``docs``" directory and online at
https://docs.djangoproject.com/en/stable/. If you're just getting started,
here's how we recommend you read the docs:

* First, read ``docs/intro/install.txt`` for instructions on installing Django.

* Next, work through the tutorials in order (``docs/intro/tutorial01.txt``,
  ``docs/intro/tutorial02.txt``, etc.).

* If you want to set up an actual deployment server, read
  ``docs/howto/deployment/index.txt`` for instructions.

* You'll probably want to read through the topical guides (in ``docs/topics``)
  next; from there you can jump to the HOWTOs (in ``docs/howto``) for specific
  problems, and check out the reference (``docs/ref``) for gory details.

* See ``docs/README`` for instructions on building an HTML version of the docs.

Docs are updated rigorously. If you find any problems in the docs, or think
they should be clarified in any way, please take 30 seconds to fill out a
ticket here: https://code.djangoproject.com/newticket

To get more help:

* Join the ``#django`` channel on irc.freenode.net. Lots of helpful people hang out
  there. Read the archives at https://botbot.me/freenode/django/.

* Join the django-users mailing list, or read the archives, at
  https://groups.google.com/group/django-users.

To contribute to Django:

* Check out https://docs.djangoproject.com/en/dev/internals/contributing/ for
  information about getting involved.

To run Django's test suite:

* Follow the instructions in the "Unit tests" section of
  ``docs/internals/contributing/writing-code/unit-tests.txt``, published online at
  https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/unit-tests/#running-the-unit-tests

*****************
The SendBird Fork
*****************

1.9.13 is the last minor version of upstream Django 1.9.

1.9.14
======

This version does not exist.

1.9.15
======

`Soda <https://github.com/sendbird/soda>`_ uses this fork since v0.28. (See `sendbird/soda#6667 <https://github.com/sendbird/soda/pull/6667>`_)

* Fixed Python 3.6 deprecation warning for empty model `super()` calls. (82036a5)
* Reverted the upstream microsecond precision support (a20ce1a)
* Suppressed the upstream update of nullable `User.last_login` (1cb5bc2)

1.9.16
======

`Soda <https://github.com/sendbird/soda>`_ uses this fork since v0.33. (See `sendbird/soda#7711 <https://github.com/sendbird/soda/pull/7711>`_)

* Re-enabled the upstream microsecond precision support. (1b55425)
