for i in range(19):
    if i == 0:
        print(i)
    elif i % 3 == 0 and i % 5 == 0:
        print('fizzBuzz')
    elif i % 3 == 0:
                print('fizz')
    elif i % 5 == 0:
            print('buzz')
    else: print(i)


fizz_buzz activity

part 1
def fizz_buzz():
      print(0)
      for i in range(1, 16):
          if i % 3 == 0 and i % 5 == 0:
            print('fizzBuzz')
          elif i % 3 == 0:
            print('fizz')
          elif i % 5 == 0:
            print('buzz')
          else:
            print(i)
fizz_buzz()

part 2
def fizz_buzz(i = 15):
      x = 1
      print(0)
      while x <= i:
        if x % 3 == 0 and x % 5 == 0:
            print('fizzBuzz')
        elif x % 3 == 0:
            print('fizz')
        elif x % 5 == 0:
            print('buzz')
        else:
            print(x)
        x += 1    
fizz_buzz()

part 3 
def fizz_buzz(i = 15):
        x = 0
        list = []
        list.append(tuple((x, str(x))))
        while x < i + 1:
                # print(x) 
            if x % 3 == 0 and x % 5 == 0:
                list.append(tuple((x,'fizzBuzz')))
                # print('fizzBuzz')
            elif x % 3 == 0:
                list.append(tuple((x,'fizz')))
                # print('fizz')
            elif x % 5 == 0:
                list.append(tuple((x,'buzz')))
                # print('buzz')
            else:
                list.append(tuple((x, str(x)))) 
                # print(x)
            x += 1
        print(list)
fizz_buzz()
