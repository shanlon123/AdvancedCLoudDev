

def mortgage(annual_salary:float, deduction:float):
    deduction = annual_salary * deduction
    return deduction

an_salar = float(input(f' Please enter your annual salary after tax: '))
deduction = float(input(f' Please enter your percentage deduction in decimal: '))

deduct_rate = mortgage(an_salar, deduction)
print(f' Your annual mortgage deduction is : {deduct_rate}')
