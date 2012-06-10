##################################################################
Information about the Django CI server hosted at ci.django-cms.org
##################################################################

*******
General
*******

* The continouos integration is powered by `Jenkins`_.
* The server is running "Linux ci.django-cms.org 2.6.38-12-server #51-Ubuntu SMP Wed Sep 28 16:07:08 UTC 2011 x86_64 x86_64 x86_64 GNU/Linux".
* The server is an EQ4 dedicated server hosted by hetzner.de, sponsored by divio.ch.
* Jenkins is running behind a nginx server


******
Python
******

There are following Python versions installed:

* Python 2.6.6
* Python 2.7.1+
* PyPy 1.7

All of them have following packages installed globally:

* PIL 1.1.7
* MySQLdb 1.2.3
* psycopg2 2.4.2
* virtualenv 1.6.4
* setuptools 0.6c11
* selenium 2.10.0 (not using 2.15.0 since according to cramm it causes issues)
* PyYAML 3.10

*********
Databases
*********

There are following Databases installed:

* MySQL 5.1
* PostgreSQL 8.4

Postgres
========

We turned ``fs_sync`` to ``off`` to speed things up.

********
Settings
********

The Django test settings were slightly modified.

The ``jenkins_test_runner.JenkinsDjangoTestSuiteRunner`` is used to generate
Jenkins compatible XML reports of the test runs. It's neccessary to patch the
xmlrunner to import ``unittest`` v2 from django instead of v1 from the stdlib.
Replacing ``from unittest`` with ``from django.utils.unitest`` in 
``xmlrunner/__init__.py`` seems to work for now. If this is not done ``SkipTest``
exceptions are not catched by the testrunner!

The database tables are namespaced by Python version.

****************
Managing Jenkins
****************

Update Jenkins
==============

Log in to the server over ssh and run:

* ``sudo apt-get update``
* ``sudo apt-get install jenkins``

Make sure Jenkins reboots after the installation.

Please do not try to upgrade Jenkins from within Jenkins, this does not work 
when Jenkins is installed using apt-get.


Udate/install plugins
=====================

* Go to http://ci.django-cms.org/pluginManager/
* Do the changes (**note**: Please do not select the "Restart Jenkins when
  installation is complete and no jobs are running" option, as it sometimes
  causes problems)
* After everything went through, log into the server and run
  ``sudo /etc/init.d/jenkins restart``


.. _Jenkins: http://jenkins-ci.org

****
Misc
****

Also installed:

* Firefox 10 (for selenium tests)
* Chromium 18 and it's webdriver (for selenium tests)
* vnc4server so jenkins can run selenium tests headless

*******
Contact
*******

The main contact for the server is Jonas Obrist aka ojii. You can find him:

* IRC: irc.freenode.net in #django-cms and #django-dev as ojii
* Github: https://github.com/ojii
* Twitter: https://twitter.com/ojiidotch
* E-Mail: ojiidotch@gmail.com

