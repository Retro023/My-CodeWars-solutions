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