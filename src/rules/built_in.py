# coding=utf-8

general_formats = [
    lambda x: x.lower(),
    lambda x: x.title(),
    lambda x: x.upper(),
    lambda x: x,
]

name_formats = [
    lambda x: ''.join(x),
    lambda x: ' '.join(x).title().replace(' ', ''),
    lambda x: ''.join(map(lambda i: i[0], x)),
    lambda x: ''.join(map(lambda i: i[0], x)) * 2,
    lambda x: ''.join(map(lambda i: i[0], x)).title(),
    lambda x: ''.join(map(lambda i: i[0], x)).upper(),
    lambda x: '%s%s' % (x[0].title(), ''.join(map(lambda i: i[0], x[1:]))),
    lambda x: '%s%s' % (x[0], ''.join(map(lambda i: i[0], x[1:]))),
    lambda x: ('%s%s' % (x[0], ''.join(map(lambda i: i[0], x[1:])))).upper(),
    # lambda x: '%s%s' % (x[0], ''.join(map(lambda i: i[0].upper(), x[1:]))),
]

date_formats = [
    '%Y',
    '%m%d',
    '%Y%m%d',
    '%y%m%d',
    '%y%-m%-d',
    '%Y%-m%-d',
    # '%y',
    # '%-m%-d',
]

company_formats = [
    lambda x: '@%s' % x,
    lambda x: '%s@' % x,
]
