Today we will be learning about a built methods and their built in ability to "parse" strings.

Lets jump into it:
------------------------------------------------------------------------------

mp = "I'm a lumberjack and I'm okay. I sleep all night and I work all day."

print(mp)

print(mp.split())

------------------------------------------------------------------------------

The default character to split a string on is " " But we can specify what we want to break the string apart.

------------------------------------------------------------------------------

print(mp.split('.'))

print(mp.split('a'))

------------------------------------------------------------------------------

What do you notice about the object that is returned from the split method? Let us test it.

-----------------------------------------------------------------------------

print(type(mp))
print(type(mp.split()))
