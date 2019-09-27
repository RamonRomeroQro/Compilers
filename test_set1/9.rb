# This is a comment
print "This program contains a single word/line comment";


=begin
THIS IS
A MULTILINE
COMMENT
=end
print "This program contains a multiline comment";



# Variables are defined by name, assign and value

my_num = 25;

print my_num;



=begin
A Ruby constant is like a variable except that its value is
supposed to remain constantfor the duration of the program
The Ruby interpreter does not actually enforce the constancy of constants
=end
Cons = 22;
print Cons;




# String declaration and use

full_name = "Ramon";
print "My name is " + full_name;


# entero, booleano, cadena

print "Bool, int and string";


first_arg = true;
secorn_arg = false;
boolean_eval = first_arg or secorn_arg;

n=0;
n=n+1;

name = "Ramon " + "Romero";

print boolean_eval ;
print n ;
print name;








print "Cycle, if, else" ;

a=1;
while a<11 do
    print "\n" ;
    print a;
    if a%2 == 0 then
        print " Romero" ;
    else
        print " Ramon" ;
    end
    a = a + 1;
end


print "\nWhat is you name ?";
name = gets.chomp;

print "Hola! "+ name ;

print "Age?";
n = gets.chomp.to_i;
n = n+1;

print "\nnext year you will have " ;
print n ;
print "\n";


