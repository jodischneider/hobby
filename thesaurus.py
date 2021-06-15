FILE = "authors.txt"
#Read input file, assume it's Unicode with return-separated names

f=open(FILE).readlines()

# Normalize
## Get rid of trailing spaces
## Non-destructively lowercase

entries = []
for line in f:
	line = str.lower(line.strip())
	print(line)
	entries.append(line)

#Sort
entries = sorted(entries)
print(entries)

#Iterate through the list of names
# Optimization: Check itertools.combinations

for outerentry in entries:
	for innerentry in entries:
		#do some heuristic here

#Identify possible matches
### Various functions

##Levenshein distance

## Get rid of all spaces
## Keep the first space, remove subsequent spaces
## Keep the first space, keep one letter after the first space
### Split at the first space, if everything before the space matches, propose it as a duplicate
## Remove accents from both candidates
## Consider distance metrics like the Hamming distance


## Heuristic - return TRUE or FALSE



#Output structure

## Preferred form - longest string, includes accents

#Save output file with groups of potential duplicates
# GROUP 1 (list of names)
