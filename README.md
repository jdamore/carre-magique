# carre-magique
Solution to the TW magic square problem

##Requirements

With a positive integer x as input, build and print the magic square of order x (hence all the numbers from 1 to x^2 in a grid with equal

We will be looking for:
- Clean code
- Evidence of TDD
- A go script
- A readme

- we need to manipulate matrices
- will output a x-matrix
- will take an integer x as an input (will return error if not a positive integer)
- command line based as our MVP. Looking at Django server-based setup if we go further
- arbitrarily, we will support a response time of less than 10 seconds for a number up to 10M


##Development

###Prerequisites
```
	Git
	An Internet Connection
```

###CLI

Bootstrap command for MacOSX - will install Python3 and the required modules
```
	./bin/bootsrap
```

Run the tests
```
	./bin/test
```

Run the program
```
	./bin/run <dimension>
```
e.g.
```
	./bin/run 20
```
