# if print integer then only use ()
# if print stringer then use "" and ()

print (1+1)
print (3-1)
print ("hi 2016")

# to check the type, put type in () 

print (type(7+8))
print (type("I'm here"))

# Conditionals and Loops
# the way that python knows to only excute print, is because of the indented part, and it's part of clause.
# the indent is part of this clause
# the way python knows that there are new clauses forming is because of the colon
# if want to print something else that's not related to a, the just take it out of the clause by getting rid of the indentation
a = 12
b = a * a - a - 1
c = a * b - b
if (a<0):
    print ("a<0")
    print (c)
else:
    print ("a>=0")
    print (c-a)

print ("we are done with the calculation") 


