result = ['{:#04x}'.format(x) for x in range(256)
          if x % 2 == 0
          ]

print(result)
