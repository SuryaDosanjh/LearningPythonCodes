# string literals
a = 'code"e' # single quotes
b = "cod'e" # double quotes
c = """ h
        u
        l  
        k
    """      # Multi line
d = "c\to\nd\0e" #escape sequences
e = r"C:\new\test.bin" # raw strings , doesn't consider escape sequences
f = b'co\x01de' #byte literals
g = 'h\u00c4ck' #Unicode literals

# Basic Operations

    # Concatenation
a = 'Surya ' + 'Dosanjh'
print(a)
b = 'Surya ' 'Dosanjh' #can be done without '+' sign aswell
print(b)

    # Repetation
print('abc'*3)

    #iteration
myjob = 'hacker'
for c in myjob:
    print(c,end=' ')    #Step through items and suppress newlines after each item

    # using 'in' expression operator
print('k' in myjob)
print('hack' in 'ABCDhacker')

    # Indexing and slicing
s = 'code' 
print(s[0],s[-2],s[1:3],s[:-1])
'code'[1:3]       #Slicing Syntax
'code'[slice(1,3)] # Slice objects with index syntax + object
'code'[::-1] # Reverses a string
'code'[slice(None,None,-1)] #Reverses a string with index syntax + object

    #String Conversion Tools
S = '62'
I = 1 
S + I # will result in an error as one is a string and other is a number
int(S) + I # will give 63 as an answer because we have converted string to an int 
S + str(I) # thsi will give '621'  as answer because we have converted the integer to string and then concatenated

    # character-code conversion
ord('h') # Output will be 104 because the built-in ord function this returns the numeric 'ordinal' value used to represent the corresponding character in memory
chr(104) # Output will be 'h' because the built-in chr function converts the ordinal value to its character

    # string comparisons
''' when we compare two text strings, Python automatically compares
them left to right, character by character, and lexicographically—that is, by the
same character code-point values returned by ord—until the first mismatch or
end of either string. In the following, for example, the code point of t is greater
than that of k, and the longer string at the end wins'''

    # changing a string - as strings are immutable we cannot directly change it but we do this by creating new string by concatenation , slicing and then asigning back to same variable
S = 'text'
S = S + 'ual!' # now s will print textual! as with contenation we made a new string and then re-assigned it
S = S[:4] + ' processing' + S[-1] # Now result will be 'text processing!'

S = S.replace('ex','hough') # replace method replaces ex with hough

# NOTE: String methods generate new string objects
# NOTE: The sytax for calling methods is object.method(arguements)
    # replace method
S = 'textly!'
r = S.replace('ly','ful') #Replace all 'ly' with 'ful' in S, optional third arguement that limits the number of replacements can be used to decide the limit
print(r)
    #Splitting
line = 'aaa bbb   ccc'
cols = line.split() #`str.split()` method chops up a string into a list of substrings around a delimiter string. 
# Output: ['aaa','bbb','ccc']
    # Drop Whitespace at end
line = "Python's srings are awesome!\n"
line.rstrip()
    # Converting to upper case
line.upper()
    # Checking suffix and prefix tests and returns bool5
line.endswith('awesome!\n')
line.startswith('Python')

# FORMATTING
    # Three Methods are 
'...%s...%s..' % (value,value)   # Formatting expression
'...{}..{}..'.format(value,value) # Formatting Method
f'...{value}...{value}..' # Formatting literal

    #String formatting expression 
'There are %d ways to %s!' % (3,'format') # Need to send tuples
# Output: 'There are 3 ways to format!'

'%(qty)s more %(tool)s' % {'qty':1, 'tool':'Formatter'} # we can also use dictionary aswell
# Output: '1 more formatter'
    
    #String formatting method
template = '{}, {}, and {}'
template.format('expr','method','fstring') #Relative Position
# Output: 'expr, method, and fstring'

template = '{0}, {1} and {2}' # Absolute position
template.format('expr','method','fstring')
# Output: 'expr, method and fstring'

template = '{first}, {second}, and {third}' # Keyword name
template.format(first='expr',second='method',third='fstring')

    # F-string formatting literal
what = 'coding'
tool = 'Python'
f'Learning {what} in {tool}'
#Output: 'Learning coding in Python'

