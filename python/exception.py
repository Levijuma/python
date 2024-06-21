# myname="eMobilis"
#
# for i in myname:
#     if i !=="k":
#         print(i)

# a = ["Python", "Exceptions", "try and except"]
# try:
#     #looping through the elements of the array a, choosing a range that goes beyond the length of the array
#      for i in range( 4 ):
#         print( "The index and element from the array is", i, a[i] )
# #if an error occurs in the try block, then except block will be executed by the Python interpreter
# except:
#     print ("Index out of range")
try:
     #code that might raise exception
     results=1/0
     print(1/0)
except ZeroDivisionError as e :
   #code to handle exception
   print("An error has occurred{e}")
finally:
  #code that run no wat
  print("this will be printed")

# jina = ["banana", "mangoes", " apples"]
#
# for i in range( 5 ):
#
#     print ('i,jina[i]')