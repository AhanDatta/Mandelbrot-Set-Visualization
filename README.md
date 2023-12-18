This project is a simple visualization of the Mandelbrot Set using Matplotlib and a simple but efficient algorithm to check for divergence. 
The solution in Rust is significantly faster and the output has a slight gradient to it, so I would suggest using that one. 
Also, if you want to work with the data in Rust directly, you can uncomment all the lines related to the "state" vector, and after the program runs, you'll have a 1D vector holding all of the iteration counts. 
There is an included Euclidean division function for when you need to convert from the absolute index of the vector to the two dimensional index used in the calculations. 

USAGE:
For the Python solution, just run the program and the result will display.
For the Rust solution, run the Rust program and then the Python graphing program after the Rust program finishes. Enjoy!
