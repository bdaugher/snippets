#!/usr/bin/python

ids = {}

fd = open('/etc/passwd', 'r')
# read 5 characters
#print fd.read(32)
#print fd.readline()

for line in fd:
    user, pwd, uid, gid = line.split(':')[0:4]
    ids[ user ] = (uid, gid)
fd.close()

fw = open('users', 'w')
for id in sorted(ids):
    s = "user {} id {} group id {}\n".format(id, ids[id][0], ids[id][1])
    fw.write(s)
fw.close()

