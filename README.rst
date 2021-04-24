=====================
Webex Teams Archiver
=====================

*Simple utility to archive Webex Teams rooms*

.. image:: https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg
    :target: https://developer.cisco.com/codeexchange/github/repo/CiscoDevNet/webex-teams-archiver
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/CiscoDevNet/webex-teams-archiver/blob/master/LICENSE
.. image:: https://img.shields.io/pypi/v/webexteamsarchiver.svg
    :target: https://pypi.python.org/pypi/webexteamsarchiver

-------------------------------------------------------------------------------

This version of the Webex Teams Archiver extracts *all*  messages of one
user and saves them in text, HTML, and JSON formats.

How-To
------

* Go to https://developer.webex.com/docs/api/v1/teams/list-teams
* Login
* After you are logged in and back on the page mentioned above you see in the right middle of that the field ``Bearer ****************************``
* Click the copy icon on the right side of that field to copy the Bearer token and click OK for the question in the message box
* Next steps need a Linux shell (replace MYBEARERTOKEN in the next step with the token you have in your clipboard):

.. code-block:: bash

    $ ./backup.sh MYBEARERTOKEN


Note: Please note that use of the Webex Teams Archiver may violate the retention policy, if any, applicable to your use of Webex Teams.


Questions, Support & Discussion
-------------------------------

webexteamsarchiver_ is a *community developed* and *community supported* project. Feedback, thoughts, questions, issues can be submitted using the issues_ page.

Contribution
------------

webexteamsarchiver_ is a *community developed* project. Code contributions are welcome via PRs!

*Copyright (c) 2018-2020 Cisco and/or its affiliates.*


.. _webexteamsarchiver: https://github.com/CiscoDevNet/webex-teams-archiver
.. _issues: https://github.com/CiscoDevNet/webex-teams-archiver/issues
.. _format: https://docs.python.org/3/library/shutil.html#shutil.make_archive
