def descending_order(num):
    # Bust a move right here
    """
    _________________________________________________________________
                      |
                      |            .'
                  \   |   /
               `.  .d88b.   .'
                  d888888b
      --     --  (88888888)  --
                  Y888888Y
              .'   `Y88Y'   `.
                  /       \
           .'         !        `.


       .,,-~&,               ,~"~.
      { /___/\`.             > ::::
     { `}'~.~/\ \   ` `     <, ?::;
     {`}'\._/  ) }   ) )     l_  f
      ,__/ l_,'-/  .'.'    ,__}--{_.
     {  `.__.' (          /         }
      \ \    )  )        /          !
       \-\`-'`-'        /  ,    1  J;
  ` `   \ \___l,-_,___.'  /1    !  Y
   ) )   k____-~'-l_____.' |    l /
 .'.'   /===#==\           l     f
      .'        `.         I===I=I
    ,' ,'       `.`.       f     }
  ,' ,'  /      \ `.`.     |     }
.'^.^.^.'`.'`.^.'`.'`.^.   l    Y;
           `.   \          }    |
            !`,  \         |    |
            l /   }       ,1    |
            l/   /        !l   ,l
            /  ,'         ! \    \
           /  /!          !  \    \
    ' '   / ,f l          l___j.   \
   ( (   (_ \l_ `_    ,.-'`--(  `.,'`.
    `.`.  Y\__Y`--'   `-'~x__J    j'  >
                                ,/ ,^'
                               f__J cred > mab'95
    """
    
    
    str_digits = list(str(num))
    str_digits.sort(reverse=True)
    return int("".join(str_digits))

# We turn the list of numbers into string then save it to a variable then we sort that list use then sort(),
#Method and set reverse to true which will turn the sort from asc to desc then we turn the strs back into ints,
#And remove the whitespace using joinh then we return it
#.p.s hope you like the ascii(:




####TASK#####

#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. 
#Essentially, rearrange the digits to create the highest possible number.

#Examples:
#Input: 42145 Output: 54421

#Input: 145263 Output: 654321

#Input: 123456789 Output: 987654321
