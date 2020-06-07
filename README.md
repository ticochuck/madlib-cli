Resources:
https://pythonprogramming.net/multi-line-printing-python-3/
suggested by Aliya!

# Madlib

[Link to Latest PR](https://github.com/ticochuck/madlib-cli/pull/1)

## Description
Print a welcome message to the user, explaining the Madlib process and command line interactions
Read a template Madlib file (Example), and parse that file into usable parts.
You need to decide what components of this file are useful, and how to break those useful pieces apart
Once you know what parts of the template need user input, such as Adjective, prompt the user to submit a series of words to fit each of the required components of the Madlib template.
With the collected user inputs, populate the template such that each provided input is placed into the correct position within the template.
After the resulting Madlib has been completed, provide the completed response back to the user in the command line.
Write the completed template (Example)to a new file on your file system (in the repo).

## Usage

The function sum_series can be called in 2 different ways. 
To use this application, call the function sum_series with at least 1 parameter. This parameter will determine the nth number to return from the fibonacci or lucas series. If you call the sum_series function with 3 parameters, the first parameter will determine the nth number to return from the lucas series, and the next 2 parameter will be the first 2 number in the lucas series. The function only accepts parameters that are integers greater than 0. It it is called with a parameter that does not meet the requeriements, it will print an error message.

```
sum_series(6)
    returns Fibonacci of 6 is 8

sum_series(6, 1, 3)
    returns Lucas of 8 with 1 and 3 is 76

sum_series(6.3) or sum_series('one')
    return Parameter(s) must be intergers >= 0
```

## Challenges

- Earlier in the week I had issues installing poetry, but thanks to Roger I got poetry up and running before I had to work on this lab 

- It was confusing having to create the virtual enviorment for the first time

- Writing tests is interesting. I am not sure if I am missing any key points, but at least for this lab, it was not too hard 


## References

[Fibonacci](https://www.youtube.com/watch?v=Qk0zUZW-U_M)
After I had already completed my code, I watched this video and it looks like is is a better way to get the nth value. However, I wanted to keep it the way I had it originally because I can pass high values without needing to import lru_cache to be efficient. 

## Lab02 - Modules, Containers, and Testing

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160025)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)
