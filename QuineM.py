#-------------------------------------------------------------------------------
# Name:        Quine McCluskey
# Purpose:     Simplify Truth Table to simplest sum of products
#
# Author:      Darrell
#
# Created:     24/10/2013
# Copyright:   (c) Darrell 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    pass

if __name__ == '__main__':
    main()

def check1bit(b1, nbits):
	print("Checking \n%7d %12s" %(b1, str(bin(b1))[2:].zfill(nbits)))
	c1 = str(bin(b1)).count('1')
	for n in range(b1+1, 2**nbits):
		if str(bin(n)).count('1') == (c1+1):
			bpos = math.log(n-b1,2)
			if not(bpos%1):
				binout = str(bin(n))[2:].zfill(nbits)
				print('%2d %4d %12s' %(bpos, n, binout), end=" ")
				rt = binout[int(nbits-bpos):]
				lt = binout[:int(nbits-bpos)-1]
				x = lt + 'X' + rt
				print("%12s" %(x))

def groupNbits(Tvals):
	"""Create a nested list grouped by number of bits in values."""
	nbits = math.floor(math.log(Tvals[len(Tvals)-1],2))+1
	DecList = []
	BinList = []
	for i in range(nbits+1):
		TmpDecList = []
		TmpBinList = []
		for T in Tvals:
			if str(bin(T)).count('1') == i:
				TmpDecList.append(T)
				TmpBinList.append(str(bin(T))[2:].zfill(nbits))
		if len(TmpDecList) > 0:
			DecList.append(TmpDecList)
			BinList.append(TmpBinList)
	return [DecList, BinList]

def match(word1, word2):
	"""Compare two strings.  If an 'X' in one string doesn't have matching 'X'
	in the same postion in the other string it returns 'False'.  If a '0' or
	'1' in one string doesn't have a matching '0' or '1' in the other string
	an 'X' will be placed in that position in the string that is returned."""
	result = [True, ""]
	wmatched = ""
	numchanged = 0
	for w in range(len(word1)):
		ch1 = word1[w:w+1]
		ch2 = word2[w:w+1]
		if((ch1 == 'X' and ch2 != 'X') or (ch2 == 'X' and ch1 != 'X')):
			result[0] = False
			break
		if ch1 != ch2:
			numchanged += 1
			if numchanged > 1:
				result[0] = False
				break
			else:
				result[1] = word1[:w] + 'X' + word1[w+1:]
	if numchanged == 0:
		result[0] = False
	return result

def removedups(duplist):
	for ind, testval in enumerate(duplist):
		print("......")
		for cpind, cpval in enumerate(duplist[ind+1:]):
			if testval == cpval:
				duplist[ind+cpind+1] = ''
				print("Testing: ", testval, cpval)
				print(duplist)
	for uval in duplist:
		if uval == '':
			duplist.remove('')

def flatlist(L1, R1):
	"""Accept a Nested List (L1) and append all objects in the nested list to
	a flattened list (R1).  Empty strings are not appended.
	This is a recursive function"""
	for item in L1:
		if isinstance(item,list):
			flatlist(item, R1)
		else:
			if item != '':
				R1.append(item)

def boolvars(QMlist):
	boolexpression = ""
	for term in QMlist:
		chcode = 65
		tmpTerm = ''
		for char in range(len(term)):
			if term[char:char+1] == '1':
				tmpTerm = tmpTerm + chr(chcode)
			elif term[char:char+1] == '0':
				tmpTerm = tmpTerm + '!' + chr(chcode)
			chcode += 1
		boolexpression += tmpTerm + " + "
	return boolexpression[:len(boolexpression)-3]

##print('%7d %12s\n' %(b1, str(bin(b1))[2:].zfill(nbits)))
##for b in Tvals:
##	check1bit(b, nbits)
##	print()

print()

Tvals = [0, 1, 3, 4, 7, 9, 11, 14, 15]
#Tvals = [0, 3, 5, 7, 9, 11, 13, 15]
Uvals = list(Tvals)
# Get bit width of the largest number in the list
Tvals.sort()
nbits = math.floor(math.log(Tvals[len(Tvals)-1],2))+1

##for n in range(len(Tvals)):
##    check1bit(Tvals[n], nbits)
##
##print('\nSorted Values: ', Tvals, '\n')

groupedByBits = groupNbits(Tvals)
groupInts = groupedByBits[0]
groupB = groupedByBits[1]

##print('Values grouped by number of bits: ', groupInts)
##print("Binary Values: ", groupB)

groupP = groupNbits(Uvals)[1]

#-----------------------------------------------------------------------------
##word1 = "010X11"
##word2 = "010X01"
##MatchedPair = match(word1, word2)
##print(MatchedPair[0])
##
##print("%10s: %10s" %("Word1", word1))
##print("%10s: %10s" %("Word2", word2))
##print("%10s: %10s" %("Wmatched", MatchedPair[1]))
##print()
###-----------------------------------------------------------------------------
##word3 = str(bin(11))[2:].zfill(4)
##word4 = str(bin(15))[2:].zfill(4)
##MatchedPair2 = match(word3, word4)
##print(MatchedPair2[0])
##
##print("%10s: %10s" %("Word3", word3))
##print("%10s: %10s" %("Word4", word4))
##print("%10s: %10s" %("Wmatched", MatchedPair2[1]))
##print()
#-----------------------------------------------------------------------------
#Testing Functions
print(Tvals)
print(groupInts)
print(groupB)

##print(id(groupB), "\n")
##print(groupP)
##print(id(groupP), "\n")
matched = []

for g in range(len(groupB)-1):
	for h, hb in enumerate(groupB[g]):
		for j, jb in enumerate(groupB[g+1]):
			wmatch = match(hb, jb)
			if wmatch[0]:
				groupP[g][h] = ""
				groupP[g+1][j] = ""
				print("g: ", g, " hb: ", hb, " jb: ", jb, wmatch[1])
				matched.append(wmatch[1])
##				print(id(groupP[g][h]), end="  ")
##				print(id(groupB[g][h]), end="  ")
##				print(id(groupP[g+1][j]), end="  ")
##				print(id(groupB[g+1][j]))
			else:
				print("g: ", g, " hb: ", hb, " jb: ", jb)

print(groupP)



print(matched)
nomatches = list(matched)
tmpmatch = []
matchfound = True

while matchfound:
	matchfound = False
	for i in range(len(matched)-1):
		for iw, w in enumerate(matched[i+1:]):
			wmatch = match(matched[i], w)
			if wmatch[0]:
				tmpmatch.append(wmatch[1])
				nomatches[i] = ''
				nomatches[i+iw+1] = ''
				matchfound = True
				print(matched[i], w, wmatch[1])
			else:
				print(matched[i], w)
	print("----------------------------------------------")
	matched = list(tmpmatch)
	removedups(matched)

print(matched)
print(matchfound)
print()

print(matched)
print(tmpmatch)
print(nomatches)
print()
print(groupP)
print(nomatches)
print(matched)

primelist = []
flatlist(groupP, primelist)
flatlist(nomatches, primelist)
flatlist(matched, primelist)
print()
print(primelist)
booleanEXP = boolvars(primelist)
print()
Blist = []
flatlist(groupB, Blist)
SOP = boolvars(Blist)
print(SOP)
print("Simplified Sum of Products: " + booleanEXP)

##print()
##TList = [3, 14, 1, 9, 6, 13, 2]
##UList = [4, 7, 11, 13, 15]
##TList.sort()
##print(TList, TList[len(TList)-1])
##
##MList = []
##MList.append(TList)
##MList.append(UList)
##print(MList)
##
##print()



##match = [ "", True]
##match[0] = "011X10"
##print(match)
##match[0] = "010X10"
##match[1] = False
##print(match)

##b2 = 15
##print(bin(b1), bin(b2))
##l1= math.log(b2-b1,2)%1
##print(l1)
##c1 = str(bin(b2)).count('1')
##print(c1)

##print(n, "  ", str(bin(n))[2:].zfill(nbits))
