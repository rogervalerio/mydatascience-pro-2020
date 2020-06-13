class Dog:

    # Class Attribute
    species = 'xmammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
saramago = Dog ("Saramago", 7)


# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

# Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

# Output
print("The oldest dog is {} years old.".format(
get_biggest_number(philo.age, mikey.age, saramago.age)))


