aletheia
========

Multi-purpose Single Source of Truth (SSoT).  Intended for managing virtual
and physical infrastructure.

Usage
=====

.. code-block:: bash

	$ aletheia -h

Manually executing the writer:

.. code-block:: bash

	$ PYTHONPATH=$PYTHONPATH:. python aletheia/shell.py

Testing
=======

Requirements:

* Ansible >= 1.6
* Vagrant >= 1.6
* Tox

Execute unit tests:

.. code-block:: bash

	$ tox

Contents:

.. toctree::
   :maxdepth: 2

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
