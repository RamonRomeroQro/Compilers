# This is a
# comment
puts "This program contains a single word/line comment"


=begin
THIS IS
A MULTILINE
COMMENT
=end
puts "This program contains a multiline comment"


# Variables are defined by name, assign and value

my_num = 25

puts my_num



# Constants begin with an uppercase letter. 

Debug = 4
puts Debug



# String declaration and use

full_name = "Ramon"
puts "My name is "+full_name


# entero, booleano, cadena

first_arg = true
secorn_arg = false
boolean_eval = (first_arg and secorn_arg)

n=0
n=n+1

name = "Ramon " + "Romero"

puts "Bool, int and string" 
puts boolean_eval 
puts n 
puts name








puts "Cycle, if, else" 

a=1
while a<11 do
    print "\n" 

    print a
    
    if a%2 == 0 
        print " Romero" 
    else
        print " Ramon" 
    end
    a = a + 1
end


puts "\nWhat is you name ?"
name = gets.chomp

puts "Hola! "+ name 

puts "Age?"
n = gets.chomp.to_i
n = n+1
# (n.to_s)
print "\nnext year you will have " 
print n 
print "\n"


