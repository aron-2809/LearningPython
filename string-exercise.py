s = "Hey there! what should this string be?"

print("Length of s = %d" % len(s))

# Find index of First occurence of "a"
print("The first occurence of the letter a = %d" % s.index("a"))

print("a occurs %d times" % s.count("a"))
# print (f"e occurs {s.count('e')} times")

print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[5:10])
print("The thirteen character is '%s'" % s[12])
print("The characters with odd index are '%s'" %s[1::2])

print("Split the words of the string: %s" % s.split(" "))
