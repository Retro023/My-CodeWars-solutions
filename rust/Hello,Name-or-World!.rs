fn hello(name: &str) -> String {
    // Format the name variable
    let mut chars = name.chars();
    let formatted_name = match chars.next() {
        Some(first) => first.to_uppercase().collect::<String>() + &chars.as_str().to_lowercase(),
        None => String::new(),
    };
     
    // handle empty
    if name.trim().is_empty() {
        return "Hello, World!".to_string();
    }

    format!("Hello, {}!", formatted_name)
}

/*
Challenge

Define a method hello that returns "Hello, Name!" to a given name, or says Hello, World! if name is not given (or passed as an empty String).

Assuming that name is a String and it checks for user typos to return a name with a first capital letter (Xxxx).

Examples:

* With `name` = "john"  => return "Hello, John!"
* With `name` = "aliCE" => return "Hello, Alice!"
* With `name` not given 
  or `name` = ""        => return "Hello, World!"





*/
