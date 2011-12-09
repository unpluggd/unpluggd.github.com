---
layout: post
title: "EC2, Elasticfox, Get Administrator Password, and “Invalid EC2 private key” errors"
excerpt: "If you're using Elasticfox to manage your instance"
tags: 
- server
- ec2
published: true
---

If you're using Elasticfox to manage your instances, and get an "Invalid EC2 private key" error when trying to "Get [the] Administrator Password" you need to change the path to your "EC2 Private Key Template" (under tools) to the correct .pem or .ppk file you were issued when you created the instance.
