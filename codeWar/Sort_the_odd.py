n = 'http://github.com/carbonfive/raygunru'


def x(n):
    if n.find('www') > 0:
        return n[n.find('www')+4: n.index('.', n.find('www')+4)]
    else:
        return n[n.find('//')+2: n.index('.', n.find('//')+2)]


print(x(n))
