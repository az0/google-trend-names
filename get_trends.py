#!/usr/bin/env python

# Copyright (C) 2018 by Andrew Ziem.
# See COPYING

"""
Download the most popular names of people from Google Trends
"""

geo = 'US'


def process_chart(date, cid):
    print 'process_chart(%s, %s)' % (date, cid)
    from pytrends.request import TrendReq
    pytrends = TrendReq(hl='en-US', tz=360)
    top = pytrends.top_charts(date=date, cid=cid, geo=geo, cat='')
    names = set()
    for index, row in top.iterrows():
        name = row['idForTracking']
        names.add(name)
    return names


def save_names(names, csv_fn):
    with open(csv_fn, 'w') as f:
        for name in names:
            f.write('%s\n' % name.encode('utf-8'))


def go():
    cids = ['actors', 'athletes', 'authors', 'musicians',
            'people', 'politicians', 'scientists']
    dates = ['%d01' % d for d in range(2004, 2018)]
    names = set()
    for cid in cids:
        for date in dates:
            new_names = process_chart(date, cid)
            names = names.union(new_names)
    save_names(names, 'people.txt')


go()
