# Tuple 

my_tuple = ("mango","berry","baannana",(1,2,45,7))
print(len(my_tuple))
print(my_tuple[1:4])

my_tuple2 = "apple"
print(my_tuple+(my_tuple2,))

# Tuple Methods
print(my_tuple.count("mango"))
print(my_tuple.index("berry"))

# sets
my_sets = {"carrot","binish","finger chipps"} #sets is unorder
print(my_sets)


# set operation
num1 = {1,3,6,5,}
num2 = {7,3,8,10}
print(num1 | num2) 
print(num1 & num2)
print(num1 - num2)

# sets methods
my_sets.add("animal")
print(my_sets)
my_sets.remove("binish")
print(my_sets)
my_sets.pop()
print(my_sets)


