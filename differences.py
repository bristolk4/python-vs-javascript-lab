# Get Name
# Write a method that accepts a name from the user and then returns it. Here’s the javascript:

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

def getName():
    name = input("Type your name: ")
    return name


# Reverse It
# Write a method that reverses a string. Here’s the javascript:

# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };

def reverseIt():
    string = "boo ba bee bo bo"
    reverse = ""

    for i in range(len(string)):
        #for each loop, the LETTER at the index "len(string) - (i+1)" is +='d to "reverse" which is just empty at first
        reverse += string[len(string) - (i + 1)]
    
    print(reverse)

reverseIt()


# Swap Em
# Write a method that swaps the values of two variables around. Here’s the javascript:

# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };

def swapEm():
    a = 10
    b = 30

    temp = b
    b = a
    a = temp

    print("a is now " + str(a) + ", and b is now " + str(b))

swapEm()


# Multiply Array/List
# Write a method that multiplies all numbers in a given array/list and returns the final product. Here’s the javascript:

# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

def multiplyArray(array):
    if len(array) == 0:
        return 1
    total = 1
    # total = array[0]

    for i in range(len(array)):
        total *= array[i]

    return total

print(multiplyArray([2, 3, 4]))


# Fizz Buzzer
# Write a method that takes a number argument and returns “fizz” if the number is divisible by three, “buzz” if the number is divisible by five, and “fizzbuzz” if it’s divisible by both. Here’s the javascript:

# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }

def fizzbuzzer(x):
    if x % (3*5) == 0: <-- x modulo 15 == 0 means x is divided by 15 with no remainder (decimal)
        return "fizzbuzz"
    elif x % 3 == 0:
        return "fizz"
    elif x % 5 == 0:
        return "buzz"
    else:
        return "archer"
    
print(fizzbuzzer(15))


# Nth Fibonacci
# Write a method that finds the fibonacci number at the nth position and returns it. Here is the javascript:

# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

def nthFibonacciNumber():
    fibs = [1, 1]
    num = input("which fibonacci number do you want? ")

    while len(fibs) < int(num):
        nextFib = fibs[-2] + fibs[-1] # <-- fibs[-2] is fibs length -2
        fibs.append(nextFib)

    print(str(fibs[-1]) + " is the fibonacci number at position " + str(num))

nthFibonacciNumber()


# Search Array/List
# Write a method that searches through an array/list for a value and returns true or false depending on whether or not the value is present in the array/list. Here is the javascript:

# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };

def searchArray(array, value):
    for i in range(len(array) - 1):
        if array[1] == value:
            return True
    return -1

print(searchArray([2, 3, 4], 5))


# Palindrome
# Write a method that checks whether or not a string is a palindrome. Here is the javascript:

# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# };

def isPalindrome(str):
    for i in range(int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

print(isPalindrome("racecar"))


# hasDupes
# Write a method that checks whether or not an array/list has any duplicates. Here is the javascript:

# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def hasDupes(arr): #arr is list
    obj = {} #obj is dictionary
    for i in arr: #loop through arr
        if i in obj: #check if i is already in dictionary, return TRUE
            return True
        else:
            obj[i] = True #i is added to dictionary and marked true
    return False

print(hasDupes([1, 2, 3, 3]))