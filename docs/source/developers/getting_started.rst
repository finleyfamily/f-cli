Getting Started
===============


Setup
-----

This section outlines how to setup portions of the repo that cannot be reasonably automated.


Development Environment
~~~~~~~~~~~~~~~~~~~~~~~

The following must be installed globally on your system.

- `poetry`_ is used for Python virtual environments, building, and publishing this project.
    - ``pip install "poetry>=1.0.0"``
    - the virtual environment is created in the `.venv/` directory of the project.
- `poetry-dynamic-versioning`_ is used to set the version of the project to allow for easy management.
    ``pip install "poetry-dynamic-versioning~=0.4"``


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

.. _poetry: https://python-poetry.org/docs/
.. _poetry-dynamic-versioning: https://pypi.org/project/poetry-dynamic-versioning/
