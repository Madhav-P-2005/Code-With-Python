'''
⭐) Regular expressions, or "regex" for short, are a powerful tool for working with strings and text data in Python. They allow you to match and manipulate strings based on patterns, making it easy to perform complex string operations with just a few lines of code.

'''


# Metacharacters in regular expressions  ? 

'''

[]   -   Represent a character class

^    -   Matches the beginning

$    -   Matches the end

.    -   Matches any character except newline

?    -   Matches zero or one occurrence.

|    -   Means OR (Matches with any of the 
characters  separated by it.

*    -   Any number of occurrences (including 0 occurrences)

+    -   One or more occurrences

{}   -   Indicate number of occurrences of a preceding RE to match.

()   -   Enclose a group of REs

'''


import re


pattern = "Bruce"

pattern2 = r"[A-Z]+yclone"

text = '''

“Why do we fall, Bruce? So we can learn to pick ourselves up.”, Thomas Wayne

=> For me, this is the best quote and probably the best moral to a movie. Although he’s the hero, batman fails many times
and often choose the wrong way. The thing is, only by failing does he learn how to overcome his failure — only by
falling does he learn how to pick himself up. I think this is the best mantra a movie has ever given to me. We all fall,
that’s natural. But what makes a person successful is his/her ability to fall, understand the situation and figure out
the way to stand up, and go on, stronger and smarter than before. Whenever I feel frustrated from my failures (and
there’s a bunch), I try to remember this quote and act according to it. cyclone Dyclone Cyclone

'''


# match = re.search(pattern , text)

# print(match)            # Output :- <re.Match object; span=(19, 24), match='Bruce'>


matches = re.finditer(pattern2 , text)

# for match in matches:
#     print(match)


'''

Output :- 

<re.Match object; span=(751, 758), match='Dyclone'>
<re.Match object; span=(759, 766), match='Cyclone'>

'''

# for match in matches:
#     print(match.span())


'''

Output :- 
(751, 758)
(759, 766)

'''

# for match in matches: 
#     print(type(match.span()))


'''

Output :- 

<class 'tuple'>
<class 'tuple'>

'''

for match in matches:
    print(text[match.span()[0] : match.span()[1]])


'''

Output :- 

Dyclone
Cyclone

'''


# Advanced Learning :- https://www.ibm.com/docs/en/rational-clearquest/9.0.1?topic=tags-meta-characters-in-regular-expressions