

1. Functional Programming with map(). Given a pair of identically
sized lists, say [1, 2, 3, ...], and ['abc', 'def',
'ghi', ...], merge both lists into a single list consisting of
tuples of elements of each list so that our result looks like:
{[(1, 'abc'), (2, 'def'), (3, 'ghi'), ...}.

2. Functional Programming with filter(). 

Determine whether an year is leap year or not by following the definition.
Determine whether a given year is a leap year,
using the following formula: a leap year is one that is divisible
by four, but not by one hundred, unless it is also divisible by
four hundred. For example, 1992, 1996, and 2000 are leap
years, but 1967 and 1900 are not. The next leap year falling
on a century is 2400.

Update your code so that it is a function if you have not done so
already. Then write some code to take a list of years and
return a list of only leap years. Then convert it to using list
comprehensions.


3. Functional Programming with filter(). 

In the Unix file system, there are always two special files in each folder/
directory: '.' indicates the current directory and '..' represents
the parent directory. Given this knowledge, take a look
at the documentation for the os.listdir() function and
describe what this code snippet does:
files = filter(lambda x: x and x[0] != '.', os.
listdir(folder))

4. Functional Programming with map(). Write a program that
takes a filename and “cleans” the file by removing all leading
and trailing whitespace from each line. Read in the original
file and write out a new one, either creating a new file or
overwriting the existing one. Give your user the option to
pick which of the two to perform. Convert your solution to
using list comprehensions.
