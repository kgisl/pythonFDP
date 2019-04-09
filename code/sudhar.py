import re

getInput = []
i = 0
x = 0
y = 0

# Creating a table
width, height = 5, 5;

table = [[0 for x in range(width)] for y in range(height)]

# Get the instructions
while True:
  string = input()
  getInput.append(str(string))
  if (getInput[i] == "REPORT"):
    break
  i = i + 1

#print (getInput)

#Regx to check if line 1 is to place the robot
matchPlace = re.search(r'^PLACE\s[01234],[01234],\D*$', getInput[0])

#Getting initial X Y positions
matchXY = matchPlace.group(0)
initX = int(matchXY[6])
initY = int(matchXY[8])

x = initX
y = initY

#Getting initial direction
matchDirection = re.search(r'\w*$',getInput[0])
botDirection = matchDirection.group(0)

'''
print (matchPlace)
print (matchXY)
print (str(initX) + "," + str(initY))
print (botDirection)
'''

#print (getInput)

for i in range(0, len(getInput)-1):

  #print ( str(i) + " " + getInput[i] + " " + botDirection )
  if (getInput[i] == matchXY ):
    #print ( "Robot Placed" )
    table[x][y] = 'R';
  
  # Move forward
  elif ( (getInput[i] == "MOVE") and (i >= 1) ):
    
    if ( botDirection == "NORTH") and ( x>=0 and y>=0 and x<=4 and y<4) :
      table[x][y] = 'X'
      y = y+1 #North Move
      table[x][y] = 'R'

    elif ( botDirection == "SOUTH") and ( x>=0 and y>0 ) :
      table[x][y] = 'X'
      y = y-1 #South Move
      table[x][y] = 'R'

    elif ( botDirection == "EAST") and ( x>=0 and y>=0 and x<4 and y<=4 ) :
      table[x][y] = 'X'
      x = x+1 #East Move
      table[x][y] = 'R'

    elif ( botDirection == "WEST") and ( x>0 and y>=0 ) :
      table[x][y] = 'X'
      x = x-1 #West Move
      table[x][y] = 'R'

  # Turn Left
  elif ( (getInput[i] == "LEFT") and (i>=0) ):

    if ( botDirection == "NORTH" ):
      botDirection = "WEST" #Left to West

    elif ( botDirection == "SOUTH" ):
      botDirection = "EAST" #Left to East

    elif ( botDirection == "EAST" ):
      botDirection = "NORTH" #Left to North

    elif ( botDirection == "WEST" ):
      botDirection = "SOUTH" #Left to South
      

  # Turn Right
  elif ( (getInput[i] == "RIGHT") and (i>=0) ):

    if ( botDirection == "NORTH" ):
      botDirection = "EAST" #Right to East

    elif ( botDirection == "SOUTH" ):
      botDirection = "WEST" #Right to West

    elif ( botDirection == "EAST" ):
      botDirection = "SOUTH" #Right to South

    elif ( botDirection == "WEST" ):
      botDirection = "NORTH" #Right to North


print(str(x) +","+ str(y) + "," + botDirection)

#print ( table )

