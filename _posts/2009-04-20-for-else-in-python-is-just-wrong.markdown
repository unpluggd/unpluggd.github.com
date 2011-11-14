---
layout: post
title: "for...else in Python is wrong"
excerpt: ""
tags: development,python
published: false
---

Big statement: The <code>else</code> keyword which comes after a <code>for</code> in Python is just wrong. 

Or rather, its very misleading. When starting out in any new language having a background in another, you look for the keywords which make sense to you to get a "handle" on things[1]. My first thoughts when seeing the <code>else</code> keyword after a <code>for</code> was "so, if there aren't any items to iterate over, it drops to the else so you don't get an error message."

No.

From the docs:

It would make _much_ more sense for it to look like the following:

    for x in range(10):
      print(x)
    then:
      print("success!")

[1]: which is why I still haven't grok'd erlang!
