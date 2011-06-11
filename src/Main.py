#!/usr/bin/python
'''
Created on Jun 10, 2011

@author: BMAllred
'''

import FibonacciBinet
import FibonacciDjikstra
import FibonacciGenerator
import FibonacciIteration
import FibonacciLucas
import FibonacciMatrix
import FibonacciMemory
import FibonacciRecursive
from StopWatch import StopWatch

def displayMenu():
    stopWatch = StopWatch()
    
    while True:
        print
        print "Fun with Fibonacci!!!"
        print
        print "Select your poison:"
        print
        print "\t1. Binet's formula"
        print "\t2. Djikstra's method"
        print "\t3. Iteration"
        print "\t4. Lucas' numbers"
        print "\t5. Matrix"
        print "\t6. Memory"
        print "\t7. Recursive (intensive)"
        print "\t-------------------------"
        print "\t0. Exit"
        print
        
        # Retrieve the user menu choice.
        choice = raw_input("Option: ")
        
        # Exit early if at all possible.
        if choice == "0":
            break
        
        # Let the user pick which number to find.
        n = -1
        while n < 0:
            n = int(raw_input("Number: "))
        
        # Start the timer.
        stopWatch.Start()
        answer = "Not available."
        
        try:
            # Perform the necessary method.
            if choice == "1":
                answer = FibonacciBinet.fib(n)
            elif choice == "2":
                answer = FibonacciDjikstra.fib(n)
            elif choice == "3":
                answer = FibonacciIteration.fib(n)
            elif choice == "4":
                answer = FibonacciLucas.fib(n)
            elif choice == "5":
                answer = FibonacciMatrix.fib(n)
            elif choice == "6":
                answer = FibonacciMemory.fib(n)
            elif choice == "7":
                answer = FibonacciRecursive.fib(n)
        except:
            pass
        
        # Stop the timer.
        stopWatch.Stop()
        
        # Give the user some feedback and statistics.
        print
        print "Answer:\t\t{0}".format(answer)
        print "Time Elapsed:\t{0}".format(stopWatch.TimeElapsed())
        print
        
        # Prepare the stop watch for the next iteration.
        stopWatch.Reset()
        
        raw_input("Press ENTER to continue...")
    
    print
    print "Hope you had as much as I did!"
    print

if __name__ == '__main__':
    displayMenu()