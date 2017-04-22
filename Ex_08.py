'''*********************************************************************************************************************************
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
The function should print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.
'''
def make_shirt(size,message):
    print("In " + str(size) + " shirt " + " with tag of " + message.title() + "!")
#Calling function with positional arguments
make_shirt("small","i luv paki team")
#Calling function with keyword arguments
make_shirt(message="i luv paki team ",size = "small")


'''*********************************************************************************************************************************
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
Make a large shirt and a medium shirt with the default message,
and a shirt of any size with a different message.
*********************************************************************************************************************************'''
# make_shirt() function so that shirts are large by default with a message that reads I love Python.
def make_shirt(size="large",message="i luv python" ):
    print("In " + str(size) + " shirt " + " with tag of " +  message.title() +"!")
make_shirt()
#Make a large shirt and a medium shirt with the default message,
make_shirt('medium', message = "i luv python")
# A shirt of any size with a different message.
make_shirt("small","i luv DataScientist")

'''*********************************************************************************************************************************
8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich.
The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number of arguments each time.
*********************************************************************************************************************************'''
def sandwiches(*items):
    print("person wants on a sandwich " + str(items))
sandwiches('cheese', 'pimiento', 'peanut', 'butter', 'jams ', 'jellies')
sandwiches('creamed cheese', 'marmalades','butter', 'jams ', 'jellies')
sandwiches('pimiento', 'peanut', 'butter', 'jams ')

'''*********************************************************************************************************************************
8-17. Printing Models: Put the functions for the example print_models.py in a
separate file called printing_functions.py . Write an
import statement at the top
of print_models.py, and modify the file to use the imported functions
*********************************************************************************************************************************'''
import pizzas
pizzas.make_pizza(13,"with extra cheese")
pizzas.make_pizza(12,"mashroom","extra cheese", "green papers", "pepperoni")

'''*********************************************************************************************************************************
PROJECT EULER:
Largest prime factor
Problem :03
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
*********************************************************************************************************************************'''
def prime_factor(n=600851475143):
    for bigest in range(2,100000):
        while n % bigest == 0:
            n  //= bigest
            print("yay, %d is a factor , now we should test %d" % (bigest,n))
            if n == 1 or n == bigest:
                return bigest
prime_factor()

