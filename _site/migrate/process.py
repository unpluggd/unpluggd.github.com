import codecs
from datetime import datetime
from lxml import etree

ns = {
    'n':'http://www.w3.org/2005/Atom',
    'zine':'http://zine.pocoo.org/'
    }

tree = etree.parse('digitala.zxa')

results = tree.xpath('/n:feed/n:entry', namespaces=ns)

for result in results:
    layout = u'post'
    title = unicode(result.xpath('n:title/text()', namespaces=ns)[0])
    published = datetime.strptime(result.xpath('n:published/text()', namespaces=ns)[0],
                                  '%Y-%m-%dT%H:%M:%SZ')
    try:
        content = unicode(result.xpath('n:content[@type="text"]/text()', namespaces=ns)[0])
    except IndexError:
        content = u''

    tags = [unicode(tag) for tag in result.xpath('n:category/@term', namespaces=ns)]

    slug = result.xpath('zine:slug/text()', namespaces=ns)[0].split('/')[-1:][0]

    ispublished = False
    if result.xpath('zine:status/text()', namespaces=ns)[0] == '2':
        ispublished = True

    filename = '%s-%s.markdown' % (published.strftime('%Y-%m-%d'), slug)

    with codecs.open('../_posts/'+filename, 'w', 'utf-8') as f:
        f.write(u"""---
layout: %s
title: "%s"
excerpt: ""
tags: %s
published: %s
---

%s
""" % (layout,
       title.replace('"', r'\"'),
       ','.join(tags),
       unicode(ispublished).lower(),
       content.replace("\r\n", "\n")
       ))
