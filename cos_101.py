def physics_and_maths_operations_options() :
    print("\nphysics and maths operations option:")
    print("a. area of rectangle ")
    print("b. acceleration ")
    print("c. potential energy ")
    print("d. kinetic energy" )
    print("e. pressure" )
    print("f. end ")


physics_and_maths_operations_options()
options =input("pick an option from a to f")
if options =='a':

    length = int(input("enter height of rectangle "))
    breadth = int(input("enter width of rectangle "))
    area_of_rectangle = length * breadth
    print(area_of_rectangle)

elif options == 'b':
    velocity = int(input("enter velocity of object "))
    initial_velocity = int(input("enter the initial velocity of the object "))
    time_taken = int(input("enter time taken "))
    acceleration = velocity - initial_velocity / time_taken
    print(acceleration)

elif options == 'c':
    mass = int(input("enter the mass of the PE "))
    height = int(input("enter the height of the PE "))
    gravity = int(input("enter the gravity of the PE "))
    potential_energy = mass * gravity * height
    print(potential_energy)

elif options == 'd':
    mass = int(input("enter number "))
    velocity = int(input("enter number "))
    kinetic_energy= 0.5 * mass * velocity**2
    print(kinetic_energy)

elif options == 'e':
    force = int(input("enter number "))
    area = int(input("enter number "))
    pressure = force / area
    print(pressure)



