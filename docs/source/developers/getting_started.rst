Getting Started
===============


Setup
-----

This section outlines how to setup portions of the repo that cannot be reasonably automated.


Development Environment
~~~~~~~~~~~~~~~~~~~~~~~

This project uses ``pipenv`` to create Python virtual environment. This must be installed on your system before setting up your dev environment.

#. ``export $(cat .env | xargs)`` to setup environment variables. This should be run each time you open a new terminal session when working within this project.
#. ``make sync`` or ``pipenv sync --dev --three`` after completing **Step 1**.


Requirements for Git Pre-Commit Hooks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This project uses pre-commit hooks to perform checks and remediation before code is pushed to the remote. In order for these to run, ``pre-commit~=1.21`` must be installed using your system installed Python 3 (not just the project's virtual environment).

Install instructions can be found `HERE <https://pre-commit.com/#install>`_.


Makefile
--------

This project utilizes ``make`` commands to simplify actions.

+---------------------------+--------------------------------------------------------+
| Command                   | Description                                            |
+===========================+========================================================+
| ``make build``            | Use setuptools to build this project                   |
+---------------------------+--------------------------------------------------------+
| ``make clean``            | Deletes build, dist, and ephemeral directories         |
+---------------------------+--------------------------------------------------------+
| ``make lint``             | Runs various python linting                            |
+---------------------------+--------------------------------------------------------+
| ``make sort``             | Runs ``isort`` to correct import order to pass linting |
+---------------------------+--------------------------------------------------------+
| ``make sync``             | Sync python virtual environment with ``Pipfile.lock``  |
+---------------------------+--------------------------------------------------------+
| ``make update-precommit`` | Updated the pre-commit scripts using the config yaml   |
+---------------------------+--------------------------------------------------------+
