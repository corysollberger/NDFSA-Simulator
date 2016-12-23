Python Program: Created by Cory Sollberger 2/24/16

The following program simulates a non-deterministic finite state automaton with sample files that construct various
automatons to test regular expressions.

The following regular expressions are accessed:

3a) The set of all strings ending in "ba"
3b) The set of all strings that contain "bac" as a substring
3c) The set of all strings that contain "ccc" as a substring

4) A DFA defined with the following table, -> Indicating start state, * Indicating final states
 ______________________
|______|___|__0__|__1__|
|__->*_|_A_|__B__|__C__|
|____*_|_B_|__C__|__A__|
|______|_C_|__C__|__C__|

5) A DFA defined with the following table, -> Indicating start state, * Indicating final states
 ______________________
|______|___|__0__|__1__|
|__->__|_A_|{B,D}|_{B}_|
|____*_|_B_|_{C}_|{B,C}|
|______|_C_|_{D}_|_{A}_|
|____*_|_D_|_{}__|_{A}_|