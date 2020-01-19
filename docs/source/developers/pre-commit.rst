.. _pre-commit: https://pre-commit.com/

Pre-Commit
==========

Git hooks are used to execute scripts before allowing a new commit. The scripts are handled by `pre-commit`_.


Hooks In Use
------------

Built-In Hooks
~~~~~~~~~~~~~~

- **trailing-whitespace** - Trims trailing whitespace.
- **end-of-file-fixer** - Makes sure files end in a newline and only a newline.
- **check-docstring-first** - Checks for a common error of placing code before the docstring.
- **check-json** - Attempts to load all json files to verify syntax.
- **pretty-format-json** -  Checks that all your JSON files are pretty. "Pretty" here means that keys are sorted and indented.
- **check-yaml** - Attempts to load all yaml files to verify syntax.
- **double-quote-string-fixer** - This hook replaces double quoted strings with single quoted strings.
- **check-added-large-files** - Prevent giant files from being committed.
- **detect-aws-credentials** - Checks for the existence of AWS secrets that you have set up with the AWS CLI.
- **detect-private-key** - Checks for the existence of private keys.
- **check-merge-conflict** - Check for files that contain merge conflict strings.

Custom Hooks
~~~~~~~~~~~~

- **isort** - Check python file import order


Running Manually
----------------

The checks run before a commit can be invoked manually to verify they are working. This can also be used when testing new hooks against the repo.

.. code-block:: shell

    $ pre-commit run --all-files

When running the hooks this way, they are run directly from what is defined in ``.pre-commit-config.yaml`` and not what is in  ``.git/hooks``. If this command is used when adding a new hook, it must be followed by `Update The Script`_ prior to committing the change for it to take effect.


Update The Script
-----------------

If the ``.pre-commit-config.yaml`` file is updated, ``make update-precommit`` will need to be run to update the script being run in ``.git/hooks``.
