print("This is a program that gives the solutions for an equation of second degree")
print("Please give a b c on each line.")
a =int(input())
b =int(input())
c =int(input())

if a == 0 :
    if b == 0 :
        if c == 0 :
            print("All solutions are possible.")
        else :
            print("No solution is possible.")
    else :
        x1 = float(-c/b)
        print("Solution is ", x1)
else :
    delta = float(b*b - 4 * a * c)
    if delta < 0 :
        x1 = complex(((-b-1j* pow(-delta,0.5))/2 * a))
        x2 = complex(((-b+1j* pow(-delta,0.5))/2 * a))
        print(F"x1 = {x1}, x2 = {x2} ")
    elif delta == 0 :
        x = -b/ 2 * a
        print(F"One solution, x = {x}") 
    else :
        x1 = float((-b-pow(delta,0.5))/2 * a)
        x2 = float((-b+pow(delta,0.5))/2 * a)
        print(F"x1 = {x1}, x2 = {x2} ")
          





