# Ans 1 :- 
class TwoDVector:
    def __init__(self, i , j):
        self.i= i
        self.j = j
    
    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j")
        

class ThreeDVector(TwoDVector):
    def __init__(self, i ,j , k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The Vector is {self.i}i + {self.j}j + {self.k}k ")


a = TwoDVector(1,2)
b = ThreeDVector(5,2,3)

a.show()
b.show()




# Ans 2 :- 
class Animals:
    def info(self):
       print("This is Animals Class . I am Parent Class ")

class Pets(Animals):
    def info(self):
      print("This is Pets Class . I am Child class")


class Dog(Pets):
    
    def bark(self):
        super(Pets , self).info()    # Output :- This is Animals Class . I am Parent Class.
        super().info()               # Output :- This is Pets Class . I am Child Class .
        print("I am Dog from Dog class . bowwwbohwww......  . Child of Parent Pets Class ")


D = Dog()
D.bark()





# Ans 3 :- 
class Employee:
    def __init__(self, salary , Increment):
        self.salary = salary
        self.Increment = Increment

    @property 
    def Increment(self):
        return self._Increment
        

    @Increment.setter
    def Increment(self, value):
        self._Increment=value


    @property
    def salaryAfterIncrement(self):
     if(self.salary>=0 and self.salary>=20000):
        if(self.salary>=20000 and self.salary<50000):
            return self.salary + 20000
        elif(self.salary>=50000 and self.salary<80000):
            return self.salary + 40000
        else:
            print("Increment session Ended")
            return self.salary
     else:
        print("Invalid Input or Please Your salary should be more than 20K or ==20k ")


print("Enter your Salary :-  ")
salary_input = int(input())
E = Employee(salary_input , 0)
new_salary = E.salaryAfterIncrement
print(f"New Salary :-  {new_salary}")



# OR



class Employee:
    def __init__(self , salary , Increment):
         self.salary = salary
         self._Increment = Increment    # Internal Attribute 

    @property
    def Increment(self):
            return self._Increment

    @Increment.setter
    def Increment(self   , value):
        if value > 0:
            self._Increment = value
        else:
            raise ValueError("Increment must be Positive")

    @property
    def salaryAfterIncrement(self):
            return self.salary + self.Increment


# Usage 
print("Enter your salary :-  ")
salary_input = int(input())
print("Enter your Increment :- ")
increment_input = int(input())
E = Employee(salary_input  , increment_input)

new_salary = E.salaryAfterIncrement
print(f"New Salary :-  ",{new_salary})

# Updating the increment using the property setter
print("Update your Increment :-  ")
new_Increment = int(input())
E.Increment = new_Increment

updated_salary = E.salaryAfterIncrement
print(f"Update Salary :-  {updated_salary}")

# OR 

class Employee:
    salary = 234
    increment=20

    # Getter for salaryAfterIncrement
    @property   # helps to return something 
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))  # This property method calculates the salary after applying the increment as a percentage.



    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self , salary):
        self.increment = ((salary/self.salary) -1)*100   # This setter method allows you to set a new salaryAfterIncrement, and it calculates the increment needed to reach that new salary.
       
        # Breaking it down :- 

        #  280.8 / 234 = 1.2
        #  1.2 - 1 = 0.2
        #  0.2 * 100 = 20.0
        #  So, self.increment is set to 20.0.



e = Employee()
print(e.salaryAfterIncrement) 
# e.salaryAfterIncrement = 280.8
print(e.increment)  # output :- 19.999999999999996

print()



'''

1) Current and New Salary :-

 a) self.salary :-  Current salary.
 b) salary :-  New salary after increment.

 
2) Calculate Ratio :- 

 a) salary / self.salary: This gives the ratio of the new salary to the current salary.
 b) Example: If the current salary is 234 and the new salary is 280.8, then 280.8 / 234 = 1.2.

 
3) Subtract 1 :- 

 a) 1.2 - 1: This subtracts 1 to find the increase in terms of the original salary. Example :-  1.2 - 1 = 0.2.

 b) This step is crucial because we are interested in the fraction of the increase. Subtracting 1 converts the ratio (1.2) to the actual increment proportion (0.2).

4) Convert to Percentage :- 

a) 0.2 * 100: This converts the fraction to a percentage. Example: 0.2 * 100 = 20.


# Without the -1, the formula would not accurately represent the percentage increment. It would instead give a number that includes the original 100%, not just the increment.


1) Suppose the current salary is 234.

2) The new desired salary is 280.8.

3) The ratio is 280.8 / 234 = 1.2.

If you don't subtract 1 :- 

increment = 1.2 * 100 = 120. 
This would incorrectly imply a 120% increase, rather than the correct 20%.


By including the -1 :- 

increment = (1.2 - 1) * 100 = 20
This correctly calculates a 20% increase, which accurately reflects the change from 234 to 280.8.


'''

# Ans 4 :- 
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
       
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.real} + {self.imag}j"

# Create Complex objects
C1 = Complex(1, 2)   # Real part
C2 = Complex(3,4)   # Imaginary part

# Perform operations
result_add = C1 + C2
result_mul = C1 * C2

# Print the results
print(f"Addition Result: {result_add}")  # Expected: 5 + 3j
print(f"Multiplication Result: {result_mul}")  # Expected: 15j (since 5 * 3j)

# Formula Breakdown  :-

'''

# When multiplying two complex numbers, let's denote them as :- 

1) (a + bi) :-  where a is the real part, and b is the imaginary part of the first number.

2) (c + di) :-  where c is the real part, and d is the imaginary part of the second number.

The product of these two complex numbers is calculated as follows :- 
                          (a + bi) x (c + di)

                          
Distributive Property :- 
                      = a x c + a x di + bi x c + bi x di

Combining Like Terms :- 
                     = (ac) + (adi) + (bci) + (bdi2)


Using i2 = -1 :-   
                     = ac + adi + bci + bd(-1)
                      = ac + adi + bci - bd
 

Grouping Real and Imaginary Parts :- 
                     = (ac - bd) + (ad + bc)i


'''  


   

# Ans 5 :- 



# Ans 6 :- 
