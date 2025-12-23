'''a=int(input('enter the age:'))
   
if a <= 18:
       print('you are a minor')
else:
     print('you are eligible for voting') '''


'''a=int(input('enter the amount:'))

if a >= 10000:
      print('you can go to goa')
elif a>=8000:
      print('you can go to local place')
elif a>=5000:
      print('you can go a dinner outside')
else:
      print('you can go to nearby park')'''

'''a=int(input('enter the age:'))
b=str(input('enter did you applied for voter id yes/no: '))
if a>=18:
      print('you are eligible for voting')
      if b=='yes':
            print('you can vote now')
      else:
            print('please apply for voter id first')
else:
      if a<18:
            print('you are a minor you are not eligible for voting')
      else:
            print('you are eligible for voting')'''

a=input('enter the username:')
b=input('enter the password:')
if a=='admin':
      if b=='1234':
        print('login successful')
      else:
        print('incorrect password')
else:
      print('invalid username')