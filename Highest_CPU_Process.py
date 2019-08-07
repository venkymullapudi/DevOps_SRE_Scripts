import sys
#INPUT
#123 30 Java
#234 90 Python
#456 45 Ruby
#567 88 Scala
#CTRL+D
#OUTPUT
#234
msg = sys.stdin.readlines()
highmap={}
for item in msg:
    highmap[item.split( )[1]] = item.split( )[0]
print (highmap[max(highmap.keys())])
