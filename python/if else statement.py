# mark=int(input("Enter marks"))
# if mark>=80 and mark<=100:
#     print("You have an A")
# elif mark>=60 and mark<=79:
#     print("You have a B")
# elif mark >=40 and mark<=59:
#     print("You have a C")
# elif mark >=0 and mark<=39:
#     print("You have failed terribly")
# else:
#     print("Wrong inputs,check your marks")



a=int(input("Enter number a"))
b=int(input("Enter number b"))
c=int(input("Enter number c"))
d=int(input("Enter number d"))
if a>b and a>c and a>d:
    print(f"{a} is greater than {b,c,d}")
elif b>a and b>c and b>d:
    print(f"{b} is greater than {a,c,d}")
elif c>a and c>b and c>d:
    print(f"{c} is greater than {a,b,d}")
elif d>a and d>b and d>c:
    print(f"{d} is greater than {a,b,c}")