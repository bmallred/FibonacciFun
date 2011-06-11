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
    while True:
        print
        print "Fun with Fibonacci!!!"
        print
        print "Operations:"
        print
        print "\t1. Find a specific number"
        print "\t2. Benchmark"
        print "\t-------------------------"
        print "\t0. Exit"
        print
        
        # Retrieve the user menu choice.
        choice = raw_input("Option: ")
        
        # Exit early if at all possible.
        if choice == "0":
            break
        
        if choice == "1":
            SingleTest()
        elif choice == "2":
            Benchmark()
        else:
            print "Incorrect selection."
        
        raw_input("Press ENTER to continue...")
    
    print
    print "Hope you had as much as I did!"
    print

def Benchmark():
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
    print
    
    # Retrieve the user menu choice.
    choices = raw_input("Options (separated with spaces): ").split()
    
    # Let the user pick which number to find.
    n = -1
    while n < 0:
        n = int(raw_input("Number: "))
    
    # Start the timer.
    stopWatch = StopWatch()
        
    if "1" in choices:
        stopWatch.Start()
        completed = 0
        
        try:
            print
            print "Binet's formula"
            
            while completed < n:
                FibonacciBinet.fib(completed)
                completed += 1
        except:
            pass
        finally:
            print "\tCompleted: {0}% in {1} ms".format((1.0 * completed / n) * 100, stopWatch.TotalMilliseconds())
            print
    
    if "2" in choices:
        stopWatch.Start()
        completed = 0
        
        try:
            print
            print "Djikstra's method"
            
            while completed < n:
                FibonacciDjikstra.fib(completed)
                completed += 1
        except:
            pass
        finally:
            print "\tCompleted: {0}% in {1} ms".format((1.0 * completed / n) * 100, stopWatch.TotalMilliseconds())
            print
    
    if "3" in choices:
        stopWatch.Start()
        completed = 0
        
        try:
            print
            print "Iteration"
            
            while completed < n:
                FibonacciIteration.fib(n)
                completed += 1
        except:
            pass
        finally:
            print "\tCompleted: {0}% in {1} ms".format((1.0 * completed / n) * 100, stopWatch.TotalMilliseconds())
            print
    
    if "4" in choices:
        stopWatch.Start()
        completed = 0
        
        try:
            print
            print "Lucas' numbers"
            
            while completed < n:
                FibonacciLucas.fib(n)
                completed += 1
        except:
            pass
        finally:
            print "\tCompleted: {0}% in {1} ms".format((1.0 * completed / n) * 100, stopWatch.TotalMilliseconds())
            print
    
    if "5" in choices:
        stopWatch.Start()
        completed = 0
        
        try:
            print
            print "Matrix"
            
            while completed < n:
                FibonacciMatrix.fib(n)
                completed += 1
        except:
            pass
        finally:
            print "\tCompleted: {0}% in {1} ms".format((1.0 * completed / n) * 100, stopWatch.TotalMilliseconds())
            print
    
    if "6" in choices:
        stopWatch.Start()
        completed = 0
        
        try:
            print
            print "Memory"
            
            while completed < n:
                FibonacciMemory.fib(n)
                completed += 1
        except:
            pass
        finally:
            print "\tCompleted: {0}% in {1} ms".format((1.0 * completed / n) * 100, stopWatch.TotalMilliseconds())
            print
    
    if "7" in choices:
        stopWatch.Start()
        completed = 0
        
        try:
            print
            print "Recursive (intensive)"
            
            while completed < n:
                FibonacciRecursive.fib(n)
                completed += 1
        except:
            pass
        finally:
            print "\tCompleted: {0}% in {1} ms".format((1.0 * completed / n) * 100, stopWatch.TotalMilliseconds())
            print

def SingleTest():
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
    print
    
    # Retrieve the user menu choice.
    choice = raw_input("Option: ")
    
    # Let the user pick which number to find.
    n = -1
    while n < 0:
        n = int(raw_input("Number: "))
    
    # Start the timer.
    stopWatch = StopWatch()
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
    print "Time Elapsed:\t{0} ms".format(stopWatch.TotalMilliseconds())
    print
    
    # Prepare the stop watch for the next iteration.
    stopWatch.Reset()

if __name__ == '__main__':
    displayMenu()