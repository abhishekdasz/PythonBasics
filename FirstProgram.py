print("Hello WOrld");
a = 10;
print(a);
b = "Wow, Great!"
print(b);
print(type(a));
c = 20;
print(a+c);
d = '10'
e = '10'
print(d+e);
f = 'hello';
print(f);
print(f.capitalize());
print(f.find('e'));
print(f.find('o'))
print(f.upper());
print(f.lower());

items = [1, 2, 3, 4, 5];
print(items);
print(type(items));
items[0] = 7;
print(items);

tupl1 = (1, 2, 3);
print(tupl1);
print(type(tupl1));
# can't change the value of a tuple
# tupl1[0] = 5;

dict1 = {}
dict1['Virat'] = 100;
dict1['Sachin'] = 110;
print(dict1);
print(dict1['Virat']);
print(dict1.get('Virat'));
print(dict1.items());
print(dict1.keys());
print(dict1.values());


# user input by default in String
# user_input = input();
# print(user_input);

# user_input2 = input("Enter your Age:");
# print('Your age is:',user_input2);

# converting to int
# user_input3 = int(input());
# print(user_input3);

# user_input4 = input("Enter a number:");
# print('Your choosen number is:' ,int(user_input4));

age = int(input('Enter your Age:'));
if(age<18) :
    print('You are a Minor');
elif(age>18 and age<60) :
    print('You are an adult');
else :
    print("You are a senior citizen");

print('for loop')
for number in range(0,5):
    print(number);

print('while loop')
nums = 0;
while nums < 5:
    print(nums, end=" ")
    nums+=1

# function
def add_numbers(a,b):
    res = a+b
    return res
print();  #add a gap
sum = add_numbers(10, 5);
print(sum);
print(add_numbers(5,6));


# username = 'das'
try:
    print(username);
except Exception as e:
    print(e);
# will show the exception message that name 'username' is not defined, 
# if before printing username, I declare the username='das' 
# then I will not get the exception message, it will print the output


f = open('hello.txt', 'w')
f.write("Hello World, This is Abhishek Das")
f.close();

f = open('hello.txt', 'r')
content = f.read()
f.close()
print(content);