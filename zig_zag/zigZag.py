import time, sys

indent = 0
indentIcreasing = True

try:
  while True:
    print(' ' * indent, end='')
    print('********')
    time.sleep(0.1)

    if indentIcreasing:
      indent += 1
      if indent == 20:
        indentIcreasing = False
    else:
      indent -= 1
      if indent == 0:
        indentIcreasing = True

except KeyboardInterrupt:
  sys.exit()