# print("hello world")
age = -21
salary=25000
name="tanvir akon"
print(name,'got a job',salary)
print(type(age))

#get user input
name=input('Enter your name: ')
print('Hello Mr. ',name)
salary =int (input('enter your salary: '))
print(type(salary))

a=5+2j
print(type(a))
type(a)

name1=input('first name')
name2=input('last name')
print(name1+' '+name2)

name='''
kibe
              hala
'''
print(name)


'''
multiline
comment
'''
number=int(input('number dw'))
if number==102:
  print('pizza')
elif number==103:
  print('vat')
else:
  print('sobji')

for i in range(0, 10, 2):
    print(i, end=' ')

i=0
while i>10:
  print(i)
  i+=1

def factorial(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factorial(n-1)

# print(factorial(5))
while True:
  n=int(input('number dw '))
  if n==0:
    break;
  fact=factorial(n)
  print(fact)