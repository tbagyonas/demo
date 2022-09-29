def power_of_two():
    user_input=input('Enter the number:')
    try:
        n=float(user_input)
        power = n ** 2
        return power
    except ValueError:
        print('invalid input.')
        return 0


print(power_of_two())
print(power_of_two())