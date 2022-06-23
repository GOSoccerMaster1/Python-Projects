# Goal here is to allow for someone to enter what shape they want to find the area for. For example like square or triangle

print('Calculator is starting... ')
raw_input = input

preoption = raw_input('Enter C for circle. Enter T for triangle. Enter S for square. Enter R for rectangle ')

option = preoption.upper()

if option == 'C':
  radius = float(raw_input("Enter radius: "))
  area = 3.14159 * radius**2
  print ("Area: %f" % area)
elif option == 'T':
    base = float(raw_input('Input base '))
    height = float(raw_input('Input height '))
    area = base * height * 0.5
    print('Area: %f' % area)

elif option == 'S':
    side = float(raw_input('Input side '))
    area = side * side
    print('Area: %f' % area)

elif option == 'R':
    length = float(raw_input('Input length '))
    width = float(raw_input('Input width '))
    area = length * width
    print('Area: %f' % area)

else:
    print('Error! Please try again')


print('Exiting...')
