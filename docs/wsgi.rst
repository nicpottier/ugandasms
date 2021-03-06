Using WSGI
==========

You can run the system using `PasteDeploy
<http://pythonpaste.org/deploy/>`_ and `PasteScript
<http://pythonpaste.org/script/>`_.

Included in the repository are two configuration files for running the
site in either a development- or a deployment scenario::

  development.ini
  deployment.ini.sample

Both of these require a local ``settings.py`` file. Customize the
included ``settings.py.sample`` file to get started.

Setting up Django's admin
-------------------------

To serve the Django admin user interface files, copy the contents of
your ``django/contrib/admin/media`` directory into a local directory
``./media``.

Development
-----------

To run the server, install (or develop) the package and use
``paster``::

  $ python setup.py develop
  $ easy_install pastescript
  $ paster serve development.ini

Deployment
----------

The ``deployment.ini.sample`` file contains a deployment configuration
template. To customize::

  $ cp deployment.ini.sample deployment.ini

By default it runs an ``scgi`` server on port ``8080``. Here's an
example of a configuration for the `lighttpd
<http://www.lighttpd.net/>`_ software::

  $HTTP["host"] =~ "^host.org$" {
        scgi.server = (
              "" =>
                ( "host" =>
                  (
                    "host" => "127.0.0.1",
                    "port" => 8080,
                    "check-local" => "disable"
                  )
                )
            )
  }

To run the server, simply use ``paster``::

  $ paster serve deployment.ini

