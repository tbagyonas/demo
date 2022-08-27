ele = []
count = int(input("how many elements?"))
for n in range(count):
    number = int(input("Enter the elements:"))
    ele.append(number)
print(ele)
for i in range(count-1, -1, -1):
    # ele.append(i)

    print(ele[i], end=',')
# string formatting using the f.
age = 34
print(f"\nyou are {age}")
name = "yohannes"
greetings = f"how are you, {name}"
print(greetings)
# advanced string formatting using curly brackets
name = "judi"
final_greetings = "how are you, {}?"
judi_greeting = final_greetings.format(name)
print(judi_greeting)
name = "Yohannes"
yohan_greetings = final_greetings.format(name)
print(yohan_greetings)

age = int(input("enter your age:"))
months = age*12
age_seconds = age*31536000
print(f"you have lived for {months} months")
print(f" you have lived of {age_seconds} seconds")

# program for printing prime numbers
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} *{n//x}")
            break
    else:
        print(f"{n} is a prime number")

