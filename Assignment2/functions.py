# You'll need to write a function to find the answer for question 2
INPUT = [
('_', 7),
('.-*`\\', 7),
('.-`_  )', 8),
('. .` :  .', 7),
("\\  '   _ :", 7),
('_.-*`   ._ `* ;', 7),
(".-`          '-.-`", 7),
('.`       `       ;', 9),
('\\        .       .:', 9),
(".   '-.   :   .  \\ .", 9),
(":      '  ;  ;.+`  '", 9),
(".-;       ;    |  '  :", 9),
("; *`._     :-`: :   ' ;", 9),
("'*`  '+ -`*. ; '*.  / '*. ]gub[", 0),
("'*-*`  *-*`   *-*`", 6),
]
def ReverseAndIndent (shape,number):
    return " " * number + ''.join(reversed(shape))
# You'll have to write the ReverseAndIndent function yourself
# It should take two parameters: the string and the number of leading spaces
# First your function should reverse the string, then it should add the right
# number spaces in front of it. Finally, return the resulting string.

# I've done the first line, but you need to do this for each element of INPUT without repeating the code
" " * 7 + ''.join(reversed('_'))

for line, indent in INPUT:
  print(ReverseAndIndent(line, indent))
