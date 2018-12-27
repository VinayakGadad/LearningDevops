# Write FizzBuzz.  This is a function that prints out the numbers 1 to 100, and 
# whenever a multiple of 3 is reached, print ‘fizz’, when a multiple of 5 is 
# reached, print ‘buzz’, and whenever a number that is a multiple of both is 
# reached print ‘fizzbuzz’.

# Tags: [basic]

def fizzbuzz(val):
  for i in range(val):
    if (i%3 == 0 ):
      print('Fizz')
    elif (i% 5 == 0):
      print('Buzz')
    elif (i%3 ==0 & i%5 ==0 ):
      print('FizzBuzz')
    else:
      print(i)

fizzbuzz(20)
