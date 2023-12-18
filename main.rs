use num::complex::Complex;                                                                                                                                                         
use rust_xlsxwriter::*; 

//Defines how many times f will be applied to itself
const ITERATION_COUNT: usize = 1000;
//Defines the sqaure of when the function diverges
const DIV_NUM: f64 = 4.0;

//Sets plotting window size
const WINDOW_HEIGHT: usize = 1080;
const WINDOW_WIDTH: usize = 1440;

//The function over which we will iterate (f_c(z) = z^2 + c)
fn f(z: Complex<f64>, c: Complex<f64>) -> Complex<f64>{
    return z*z + c;
}

//Applies f to itself until either the value diverges or the function hits the maximum number of iterations. Returns the iteration on which the function exited
fn iterated_f(c: Complex<f64>) -> usize {
    let z_0: Complex<f64> = Complex::new(0.0, 0.0); 
    let mut value: Complex<f64> = f(z_0, c);
    let mut iter: usize = 0;
    while iter < ITERATION_COUNT{
        if value.norm_sqr()  > DIV_NUM{
            break;
        }
        value = f(value, c);
        iter = iter + 1
    }
    return iter; 
}

/* Useful if you choose to work with the vector and not the file
//Returns the Euclidean division result of x/y
fn div_rem(x: usize, y: usize) -> (usize, usize){
    let q = x / y;
    let r = x % y;
    return (q, r);
}
*/

fn main() {
    //Sets the starting value for the complex input (Centered at zero with a 4:3 aspect ratio)
    let z_0 = Complex::new(-2.0, -1.5);
    let TOT_PIXELS = WINDOW_HEIGHT * WINDOW_WIDTH;

    //Sets the increment between rows and cols
    let y_resolution = -(2.0 * z_0.im)/(WINDOW_HEIGHT as f64);
    let x_resolution = -(2.0 * z_0.re)/(WINDOW_WIDTH as f64);

    /* Use if you want to work with the data directly in Rust
    //1D vector which will hold all of the iteration values, reserved for the total number of values
    let mut state: Vec<usize> = Vec::new();
    state.reserve(TOT_PIXELS);

    //Creates a vector of zeros
    for _i in 0..TOT_PIXELS{
        state.push(0);
    }
    */

    //Creates the output xlsx file
    let mut workbook = Workbook::new();
    let worksheet = workbook.add_worksheet();

    //Starts the changing complex number at the initial
    let mut z: Complex<f64> = z_0;

    //iterates through each row
    for i1 in 0..WINDOW_HEIGHT{
        //resets the real part when it jumps down a row
        z.re = z_0.re;

        //iterates through each col, adding the iteration count of each pixel to the state vector
        for i2 in 0..WINDOW_WIDTH{
            //let absolute_index: usize = i1 * WINDOW_WIDTH + i2;
            let iter_count = iterated_f(z);
            //state[absolute_index] = iter_count;
            worksheet.write((WINDOW_HEIGHT - i1) as u32, i2 as u16, iter_count as u64);
            z.re = z_0.re + x_resolution * (i2 as f64);
        }
        z.im = z_0.im + y_resolution * (i1 as f64);
    }

    workbook.save("mandelbrot_output.xlsx");

}
