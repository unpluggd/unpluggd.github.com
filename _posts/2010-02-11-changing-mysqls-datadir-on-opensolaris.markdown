---
layout: post
title: "Changing MySQL’s datadir on OpenSolaris"
excerpt: "Create the new data dir, and change ownership to t"
tags: 
- server
- opensolaris
published: true
---

Create the new data dir, and change ownership to the `mysql` user.

    ~# mkdir /mysqldatadir
    ~# chown -Rf mysql:mysql /mysqldatadir

Edited the file “/var/svc/manifest/application/database/mysql_51.xml”, changing the value of the 'data' node.

Stop the service then delete and reimport the manifest file using svccfg.

    ~# svcadm disable mysql
    ~# svccfg delete mysql
    ~# svccfg import /var/svc/manifest/application/database/mysql_51.xml

Restart the service.

    ~# svcadm enable mysql

Test everything's working.

    ~# mysql -e "show variables" | grep datadir
