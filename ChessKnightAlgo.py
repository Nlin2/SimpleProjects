print('This algorithm finds the number of possible positions a knight in an')
print('infinite chess board can be at after n moves')
print()
n = int(input('Enter number of moves: '))

# A list of sets made of tuples
sLst = [set([tuple([0, 0])])]
def moveOnce(l):
    st = set()
    for s in l:
        st.add(tuple([s[0] + 2, s[1] + 1]))
        st.add(tuple([s[0] - 2, s[1] + 1]))
        st.add(tuple([s[0] + 2, s[1] - 1]))
        st.add(tuple([s[0] - 2, s[1] - 1]))
        st.add(tuple([s[0] + 1, s[1] + 2]))
        st.add(tuple([s[0] - 1, s[1] + 2]))
        st.add(tuple([s[0] + 1, s[1] - 2]))
        st.add(tuple([s[0] - 1, s[1] - 2]))
    return st

for _ in range(n):
    sLst.append(moveOnce(sLst[-1]))
print(len(sLst[-1]))
#print(list(map(lambda x: len(x), sLst)))
