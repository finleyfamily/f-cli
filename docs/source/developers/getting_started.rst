Getting Started
===============


Setup
-----

This section outlines how to setup portions of the repo that cannot be reasonably automated.


Development Environment
~~~~~~~~~~~~~~~~~~~~~~~

This project uses ``pipenv`` to create Python virtual environment. This must be installed in your system before setting up your dev environment.

#. ``export $(cat .env | xargs)`` to setup environment variables. This should be run each time you open a new terminal session when working within this project.
#. ``make sync`` or ``pipenv sync --dev --three`` after completing **Step 1**.


Makefile
--------

This project utilizes ``make`` commands to simplify actions.

+----------------+-------------------------------------------------------+
| Command        | Description                                           |
+================+=======================================================+
| ``make build`` | Use setuptools to build this project                  |
+----------------+-------------------------------------------------------+
| ``make clean`` | Deletes build, dist, and ephemeral directories        |
+----------------+-------------------------------------------------------+
| ``make sync``  | Sync python virtual environment with ``Pipfile.lock`` |
+----------------+-------------------------------------------------------+

