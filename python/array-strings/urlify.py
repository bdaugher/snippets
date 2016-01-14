#!/usr/bin/python


def urlify(str, len):
    result = ''
   
    for s in str:
        if s == ' ':
            result += '%20'
        else:
            result += s
    return result


print urlify("foo bar baz", len("foo bar baz"))
