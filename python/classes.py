#!/usr/bin/python

class alpha(object):
    def __init__(self, s='one'):
        self.a = 10
        print s

class beta(alpha):
    def __init__(self, s='two'):
        self.b = 20
        super(beta,self).__init__('once')
        print s

class gamma(beta):
    def __init__(self, s='three'):
        self.c = 30
        super(gamma,self).__init__('twice')
        print s

#a = alpha('ONE')
#b = beta('Two')
c = gamma('thrice')

print type(c), id(c), dir(c), c.__dict__

