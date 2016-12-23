#By: Cory Sollberger  COS 451  Homework 4

#A function (FSM) that will take the input and determine the conclusion
#Input a 5-tuple (Q, Sigma, Delta, q0, F)
#Where Q = Finite set of states, Sigma = finite set of input symbols,
#Delta = Transition function, q0 = starting state, and F = set of final states.
def FSM(Q, Sigma, Delt, Q0, F, sInput):
    currentState = Q0 #Starting state
    for x in sInput:
        nextState = set() #empty set
        for y in currentState: #For each state in the currentState, plug back into FSM
            for z in Delt:
                if (z[0] == y and z[1] == x):
                    for a in range(len(z))[2:]: #Add all iterative states
                        nextState.add(z[a])
        currentState = nextState
    if (len(currentState.intersection(F))>0): #check if a final state
        return True
    else:
        return False


#Read the desired information from a file
def readFSM(fileName):
    f = open(fileName, 'r') #opens file to read the 5 elements of the NDFA
    inpLines = []
    for line in f:
        inpLines.append(line.rstrip('\n'))

    count = 0
    for x in inpLines:
        if count == 0:
            q.clear()
            for a in inpLines[count]:
                q.add(a)
        elif count == 1:
            S.clear()
            for a in inpLines[count]:
                S.add(a)
        elif count == 2:
            delt.clear()
            s = ""
            for a in inpLines[count]:
                if a != ',':
                    s = s + a
                else:
                    tempTuple = ()
                    for t in s:
                        temp = (t,)
                        tempTuple = tempTuple + temp
                    delt.append(tempTuple)
                    s = ""
        elif count == 3:
            q0.clear()
            for a in inpLines[count]:
                q0.add(a)
        elif count == 4:
            F.clear()
            for a in inpLines[count]:
                F.add(a)
        count = count + 1
      
#Initialize the Variables for the FSM
q = set()
S = set()
delt = []
q0 = set()
F = set()

#Tests for Homework 4
#Problem 3A
readFSM("prob3A.txt")
print ("Problem 3A: input 'ba'")
print (FSM(q, S, delt, q0, F, "ba")) #true
print ("Problem 3A: input 'bac'")
print (FSM(q, S, delt, q0, F, "bac"))#false
print ("Problem 3A: input 'babacabacbabcbabcccabcba'")
print (FSM(q, S, delt, q0, F, "babacabacbabcbabcccabcba"))#true
#Problem 3B
readFSM("prob3B.txt")
print ("Problem 3B: input 'baca'")
print (FSM(q, S, delt, q0, F, "baca"))#true
print ("Problem 3B: input 'babc'")
print (FSM(q, S, delt, q0, F, "babc"))#false
print ("Problem 3B: input 'bbbbaababababbacaaabaa'")
print (FSM(q, S, delt, q0, F, "bbbbaababababbacaaabaa"))#true
#Problem 3C
readFSM("prob3C.txt")
print ("Problem 3C: input 'ccca'")
print (FSM(q, S, delt, q0, F, "ccca"))#true
print ("Problem 3C: input 'ccaccbccaccbcc'")
print (FSM(q, S, delt, q0, F, "ccaccbccaccbcc"))#false
print ("Problem 3C: input 'bbbbaababcccbbacaaabaa'")
print (FSM(q, S, delt, q0, F, "bbbbaababcccbbacaaabaa"))#true
#Problem 4
readFSM("prob4.txt")
print ("Problem 4: input '010'")
print (FSM(q, S, delt, q0, F, "010"))#true
print ("Problem 4: input '010101010101'")
print (FSM(q, S, delt, q0, F, "010101010101"))#true
print ("Problem 4: input '100000001100101010101'")
print (FSM(q, S, delt, q0, F, "100000001100101010101"))#false
#Problem 5
readFSM("prob5.txt")
print ("Problem 5: input '0'")
print (FSM(q, S, delt, q0, F, "0"))#true
print ("Problem 5: input '1'")
print (FSM(q, S, delt, q0, F, "1"))#true
print ("Problem 5: input '0010011'")
print (FSM(q, S, delt, q0, F, "0010011"))#true
print ("Problem 5: input '10'")
print (FSM(q, S, delt, q0, F, "10"))#false
#Problem 5DFA
readFSM("prob5DFA.txt")
print ("Problem 5DFA: input '0'")
print (FSM(q, S, delt, q0, F, "0"))#true
print ("Problem 5DFA: input '1'")
print (FSM(q, S, delt, q0, F, "1"))#true
print ("Problem 5DFA: input '0010011'")
print (FSM(q, S, delt, q0, F, "0010011"))#true
print ("Problem 5DFA: input '10'")
print (FSM(q, S, delt, q0, F, "10"))#false

