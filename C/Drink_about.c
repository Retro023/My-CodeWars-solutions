//    do not allocate memory:
//    return a string literal

const char *people_with_age_drink(unsigned age) {

if (age < 14){
  return "drink toddy";
}
else if (age < 18){
  return "drink coke";
}
else if (age < 21){
  return "drink beer";
}
else if (age >= 21){
  return "drink whisky";
}
else {
   return "age unknown drink coke";



/*  
Challenge

    Kids drink toddy.
    Teens drink coke.
    Young adults drink beer.
    Adults drink whisky.

Make a function that receive age, and return what they drink.

Rules:
    Children under 14 old.
    Teens under 18 old.
    Young under 21 old.
    Adults have 21 or more.

Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"




*/
