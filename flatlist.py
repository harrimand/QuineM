#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Darrell
#
# Created:     04/11/2013
# Copyright:   (c) Darrell 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


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

print(chr(65))


L1 = [99, [1,2,3], [[7, 8],[[11,12], [13, ""]]], [4, 5]]
flist = [999, "Darrell"]
flatlist(L1, flist)
print(L1)
print(flist)

primelist = ['0000', 'XX10', 'X0X1', '1XX1']

print(boolvars(primelist))

astr = "abc"
astr +="bcd"
print("astr = ", astr)

