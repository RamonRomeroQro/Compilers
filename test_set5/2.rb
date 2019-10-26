
=begin

class Customer
    @@no_of_customers = 0
    def initialize(name)
    @cust_name = name
    end
    def printName()
        print @cust_name
    end
end

cust1 = Customer.new("Juan")
print "\n"
print cust1.printAge()
print "\n"

=end

