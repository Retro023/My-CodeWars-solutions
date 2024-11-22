fn make_negative(num: i32) -> i32 {
    if num > 0 {
        -num
    } else {
        num
    }
}

fn main() {
    println!("{}", make_negative(1));   
    println!("{}", make_negative(-5));  
    println!("{}", make_negative(0));   
}

// first we check if a number is negative by seeing if its greater then 0 and as anything greater then 0 is not negative we slap a - on it to,
//Make it a negative and if its less then 0 then it will have a - already as anything less then 0 is already negative



///////TASK///////


//In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

//Examples
//make_negative(1);  # return -1
//make_negative(-5); # return -5
//make_negative(0);  # return 0
//Notes
//The number can be negative already, in which case no change is required.
//Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.
