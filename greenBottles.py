##10 GREEN BOTTLES RHYME##
import time
bottles = 10
for z in range(bottles,0,-1):
    print("{0} green bottles on the wall, {0} green bottles on the wall.".format(z))
    time.sleep(0.5)
    print("And if one should fall, they'll be {0} green bottles on the wall.".format(z,-1))
