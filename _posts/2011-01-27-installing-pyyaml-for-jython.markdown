---
layout: post
title: "Installing PyYAML for Jython"
excerpt: ""
tags: server,jython
published: true
---

PyYAML by default tries to create a C module against the libyaml library, and since Jython can't use C modules attempting to install PyYAML with Jython fails.

...unless you disable the C module install, like this:

{% highlight bash %}
~# wget http://pyyaml.org/download/pyyaml/PyYAML-3.09.tar.gz
~# tar zxf PyYAML-3.09.tar.gz
~# cd PyYAML-3.09
~# jython setup.py --without-libyaml install
{% endhighlight %}
