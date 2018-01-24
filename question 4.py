yours= ['Yale','MIT','Berkely']
mine = ['Yale', 'Depauw', 'Brown']

ours1= mine + yours


ours2 = []
ours2.append(mine)
ours2.append(yours)

print(ours1)
print(ours2)

# Question 5(1) ours1, when printed, is all of our favorite schools contained in the same set of
# parenthesis.  ours2, when printed, contains 2 sets of parentheses, one that contains my favorite
# schools and one that contains your favorite schools, both of which are inside a set of brackets.  It seems that the + operation appends 2 lists. Thus, [a,b]+[b,c]=[a,b,c,d], and the append function adds an element to the end of a list.
yours[1]='NYU'

print(ours1)
print(ours2)

#Question 5(2)
#Changing yours 2 doesn't change ours1 because the + symbol appends the two origional lists.  When printing ours2 we are adding the modified yours list to the mine list.
