# jab bahut varible ko pass karna ho argument me  tab ye keyword var lenght argument ka use karte hai **
# yaha dict for me value hold karta hai

# def Add(**n):
#     print(n)
#     print(type(n))

# res = Add(z=10 , e=20 , f=30 , t =10)

# print(res)



# def Add(**kwards):
#     print(kwards)
#     print(type(kwards))
# res = Add(z=10 , e=20 , f=30 , t =10)
# print(res)



# def Add(**kwards):
#     for i in kwards.items():
#      print(i)
# diction = eval(input("Enter A Dictionary : "))
# res = Add(**diction)


# def Add(**kwards):

#     for k,v in kwards.items():
#       print(k)
#       print(v)
# diction = eval(input("Enter A Dictionary : "))
# res = Add(**diction)

# print(res)




def Add(**kwards):

    for k,v in kwards.items():
      print(f'My {k} is : {v}')
      print(type(kwards))


diction = eval(input("Enter A Dictionary : "))
res = Add(**diction)

print(res)

# {"Name":"Vineet","Course":"B-Tech"}