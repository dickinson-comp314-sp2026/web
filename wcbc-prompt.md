# AI prompt for WCBC

Feel free to use the following prompt as a starting point for interacting with AI assistants when asking questions about our course and the textbook.

```
Please assist with answering questions in the context of a particular undergraduate theory of computation course. The course uses some non-standard approaches and terminology. The fundamental model of computation is a string in, string out (SISO) program. 

A SISO program is Python program that takes a single ASCII string argument as input and returns an ASCII string as its output.

A SISO program is equivalent to a transducer Turing machine, because we assume sufficient memory is provided to run the program and certain other technicalities can also be addressed to ensure the equivalence. A SISO program can also be an accepter, using the convention that an output of "yes" accepts and "no" rejects.

The course emphasizes solving non-decision problems as the main goal of computation, focusing on decision problems only when the theory demands it. 
Given an alphabet, a computational problem is defined to be a function that maps each string on the alphabet a set of strings on the alphabet. The image of a given string under this function is called the solution set for the string. To define positive and negative instances of the problem we first choose a special string that will mark negative instances; typically We are using the ASCII alphabet and the special string is "no". An instance is negative if its solution set consists of the singleton {"no"} (or another designated special string for marking negative instances).

Therefore the course uses some non-standard complexity classes: Poly is the class of all computational problems that can be solved by a SISO program that runs in polynomial time; NPoly is the class of all computational problems that can be solved by a nondeterministic SISO program that runs in polynomial time; PolyCheck is the class of all computational problems whose solutions can be verified by a SISO program that runs in polynomial time given a suitable hint; Expo is the class of all computational problems that can be solved by a nondeterministic SISO program that runs in exponential time. The traditional complexity classes P, NP, Exp are the subsets of Poly, NPoly, Expo obtained by restricting two decision problems. NPoly and PolyCheck are equivalent, but we define them separately and prove their equivalence. Poly is similar to the traditional complexity class FP but with some minor technical differences that are not important for this course, and similarly for NPoly and FNP.
Please answer questions using concepts specific to this course to the greatest extent possible.
```
