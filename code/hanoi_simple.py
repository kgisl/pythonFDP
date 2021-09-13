c = 0


def moveTower(height, fromPole, toPole, withPole):
    if height == 1:
        moveDisk(height, fromPole, toPole)
    else:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)


def moveDisk(disk, fp, tp):
    global c
    c += 1
    print("Step", c, ": moving Disk", tower[disk], "from", fp, "to", tp)


tower = ['', 'red  ', 'green', 'blue ']
moveTower(3, "Start", "Dest", "Middle")
