#i love python
def Main():
  # create the list l of integerers 0 to 20
  l = range(20)
  print "We'll be using the list... \n%s\n" % l

  print "\nl[::2]... \n%s" % l[::2]
  print "\nl[::3].. \n%s" % l[::3]
  print "\nl[::-1]... \n%s" % l[::-1]
  print "\nl[::-2]... \n%s" % l[::-2]
  print "\nl[::-2]... \n%s" % l[::-2]

  print "\nUsing splices, we can also delete things such as... "

  del l[::2]
  print "\"del l[::2]...\"\n%s" % l

if __name__ == '__main__':
  Main()
