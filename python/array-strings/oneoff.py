#!/usr/bin/python


def oneoff(s1, s2):
    onetry = True
   
    if abs(len(s1) - len(s2)) > 1:
        print s1, s2, 'too long'
        return False

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            pass
        elif onetry == False:
            print s1, s2, 'already modified'
            return False
        else:
            onetry = False

    print s1, s2, 'are one edit away from equal'
    return True


oneoff('abc', 'ab')
oneoff('abcd', 'ab')
oneoff('acd', 'ab')
oneoff('acd', 'abd')

