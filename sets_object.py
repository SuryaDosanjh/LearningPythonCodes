# Set Initiation
x = set('abcde') #Make a set by calling its type/function
y = {99,'b','y','d',1.2} # Make a set by literal
z = {1,*'abc',*[1,2,3]} #Literal star unpacking

#Operations
x = set('abcd')
y = set('bdxy')
z = x-y #Difference: in x, not in y result = {'a','c'}
z = x|y #Union result = {'y','d','x','c','a','b'}
z = x&y #Intersection result = {'d','b'}
z = x^y #Symmetric difference: not  in both result {'y','x','c','a'}
z = x<y,x>y #Superset, subset tests results = (False,False)

# In 
'd' in 'code' # Result True

# More Methods
x = {'a','b','c','d'}
y = {'x','y','z','c','d'}
z = x.intersection(y) # Same as x & y
z.add('Hack') #Result = {'Hack','c','d'}
z.update(set(['x','y']))
z.remove('x')

# Set comprehensions
z = {x**2 for x in [1,2,3,4]}


