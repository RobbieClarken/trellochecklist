trellochecklist
===============

Create a Trello checklist from a text file.

.. image:: https://travis-ci.org/RobbieClarken/trellochecklist.svg?branch=master
   :target: https://travis-ci.org/RobbieClarken/trellochecklist
   :alt: Build Status


Installation
------------

::

   pip3 install git+https://github.com/RobbieClarken/trellochecklist


Usage
-----

First set environment variables for ``TRELLO_API_KEY`` and
``TRELLO_APP_TOKEN``. These can be generated at https://trello.com/app-key.
Then simply run::

   trellochecklist --board Home --card Shopping items.txt

Each line of the specified file will become an item on the checklist.
