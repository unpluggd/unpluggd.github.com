---
layout: post
title: "Staying up-to-date on linux."
excerpt: ""
tags: development,linux-servers
published: true
---

We noticed that our servers' clocks were slightly off. Adding the following to our /etc/rc.local file keeps our servers updated whenever it boots:

    set -- `nc time.nist.gov 13`
    date -u --set="$2 $3"

I've also added it to our cron.daily so there's no slip while the servers are running.
