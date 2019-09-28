# This is a comment

print "\nThis program contains a single word/line comment\n"




=begin
THIS IS
A MULTILINE
COMMENT
=end

print "\nThis program contains a multiline comment\n"




# Variables are defined by name, assign and value

my_num = 25

print my_num



=begin
Un programa sencillo con la definición de una constante.
A Ruby constant is like a variable except that its value is
supposed to remain constan tfor the duration of the program
The Ruby interpreter does not actually enforce the constancy of constants
=end

Const = 22
print Const
print "\n"



# String declaration and use

full_name = "Ramon\n"
print "\nMy name is " + full_name


# entero, booleano, cadena

print "\nBool, int and string\n";


first_arg = true
secorn_arg = false
boolean_eval = first_arg or secorn_arg
Cons = 42
n=0
n=n+1


name = "Ramon " + "Romero"

print boolean_eval 
print "\n"
print n 
print "\n"
print Cons
print "\n"
print name








print "\nCycle, if, else\n" 

a=1
while a<11 do
    print a
    if a%2 == 0 then
        print " Romero" 
    else
        print " Ramon" 
    end
    a = a + 1
    print "\n" 

end



print "\nWhat is you name ? ->"
name = gets.chomp

print "Hola! "+ name +"\n"

print "Age? ->"
n = gets.chomp.to_i
n = n+1

print "\nnext year you will have " 
print n 
print "\n"



