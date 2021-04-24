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
* For the next steps you need a Linux shell. Checkout the whole repository
and execute the backup.sh (replace MYBEARERTOKEN in the next step with the token you have in your clipboard):

.. code-block:: bash

    $ ./backup.sh MYBEARERTOKEN
    Processing 1/447: {'id': 'Y2lzY29....', 'title': 'Daily Meeting Room', 'type': 'direct', 'isLocked': False, 'lastActivity': '2021-04-20T11:32:36.567Z', 'creatorId': 'Y2lzY29....', 'created': '2021-04-20T11:23:01.055Z', 'ownerId': 'Y2lzY29....'}
    Processing 2/447: {'id': 'Y2lzY29....', 'title': 'Upgrade WarRoom', 'type': 'group', 'isLocked': False, 'lastActivity': '2021-04-20T08:09:14.276Z', 'teamId': 'Y2lzY29....', 'creatorId': 'Y2lzY29....', 'created': '2021-04-20T08:08:49.388Z', 'ownerId': 'Y2lzY29....'}

It iterates now through all the channels and private communiations (447 in total in my case) and prints a line for each.
After this you have a folder (and a packed gz file) for each communication with a nice html file. 

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
