#  CONDITIONAL STATEMENT


# weather = input("what is the weather? ");

# if weather == 'rainy' : 
#     print("grab an umbrella");
    
# elif weather == 'cloudy' :
#     print("get your jacket");
    
# elif weather == 'thurnderstorm' :
#     print("stay in the house");
    
# else :
#     print("get your sun glasses");

# score = int(input("Please enter your MARKS: ")) ;

# if score >= 90 :
#     print("A");
    
# elif score >= 80 :
#     print("B");
    
# elif score >= 70 :
#     print("C");
    
# elif score >= 60 :
#     print("D");
    
# elif score < 60 :
#     print ("E");
    
# else : 
#     print ("F");

# score =  int(input("Enter your marks: "));

# if 60 <= score <= 100 :
#     print ("you hve passed");
    
# else :
#     print("you have failed");


# FUNCTIONS


# def say_my_name (name) :
    
#     print(name)
    

# say_my_name ("joseph")    
    
# multi argument

# def greeting ( greet, name) :
    
#     print (f'{greet}, {name}')
    
# greeting ('wemwega', 'joseph')    

# def sum ( a, b) :
    
    
    
#     return a + b

# print (sum ( 30,  40))

#  lambda >>>= anonymous function

# sum2 =lambda a, b : a + b
# print(sum2(10,30))

# greet = lambda greet , name : f"{greet}, {name}"

# print(greet('hello!', 'kirika'))

# ARRAYS >>>>>= LIST

# fruits = ['mango','banana','apple', 'orange']

# print(fruits)

# fruits.append('berry')

# print (fruits)

# SLICING

# print(fruits [0:2])

# DICTIONARIES

# person = {
#     'name' : 'KIRIKA',
#     'shirt' : 'blue',
#     'laptop' : 'apple',
#     'age' : '20'
#           }



# def introducer ():
    

#    person = {
#     'name' : 'KIRIKA',
#     'shirt' : 'blue',
#     'laptop' : 'apple',
#     'age' : '20'
#           }
#    print(f"my name is {person['name']}, my shirt is  {person['shirt']} in color  and i use an {person['laptop']} laptop, my agee is {person['age']}")
   
         
         
# introducer ()

 
#  LIST & SET

# list1 = ['Ruby','javascript','sql']
# list2 = ['python','java','c++']
# programming_languages = set( list1 + list2)
# print(programming_languages)
    
# ONOTHER SET FUNCTION

# def unique (languages):
#    return list (set (languages))
# print(unique(['ruby','ruby','python']))

# LOOPS
   
   # ONOTHER TRIAL

# fruits = ['apple', 'mango', 'orange']
# for _ in range(5):
#    fruits.append('banana')

# print(fruits)

# WHILE LOOP
# counter = 0
# while counter <= 10 :
#    print(counter)
#    counter += 1
   
# PRACTICE FUNCTION , LIST AND APPEND

# def double (numbers : list) -> list:
#    results = []
#    for number in numbers :
#       results.append(number * 2)
      
#    return results
      
# print(double([2,3,4]))

# ONOTHER PRACTICE

# def count_words (greetings ) :
#    print (len(greetings.split()))
   
# count_words ('hi my name is joseph and i am a revere software engineer')

# my repractice
# def registration () :
#    name = input("Enter your name: ");
#    gender = input("Enter your gender: ");
#    account_No = input("Enter your account number: ");
  
#    name == name and gender == gender and account_No == account_No
#    print("\n")
   
#    if name == '' and gender == '' and account_No >= 7:
#       print(f"_________________Welcome to the platform, {name}____________________")
#    else:
#       print("_________________please try again tommorrow____________")
# registration ()

# WHILE LOOPS
# counter = 0
# while counter <= 10 :
#    print(counter);
#    counter += 1

# PRACTISE 
# def double (numbers: list) :
#    result = []
#    for number in numbers :
#       result.append(number * 2) 
      
  
#    return result 
   
# print(double([1,2,3,4]))

# ONOTHER ONE
# def sum_list (numbers) :
#    count = 0
#    for number in numbers :
     
#      count += number
     
#    return count

# print(sum_list([1,2,3,4]))

# FINDMAX

# print(min ([1,3,5,9]))

# PRACISE

# def dictionaries () :
#    person = {
#       'name':'joseph kirika',
#       'nationallity':'Kenyan',
#       'age': 20
#    }
   
#    print(f"{person['']}")
   
# dictionaries()   
   
 
# FUNCTIONS
# def greet(greetings):
#    print(greetings)
# greet('hi joseph')   

# LIST AND SETS

# list1 = ['java', 'ruby', 'sql']
# list2 = ['flask','ruby','java']


# print(list1 + list2)

# list
# def sum_list (numbers) :
#    count = 0
#    for number in numbers :
     
#      count += number
     
#    return count

# print(sum_list([1,2,3,4]))

# MINE
# def sumlist (numbers) :
   
#    count = 0
#    for number in numbers :
      
#       count += number
      
#    return count
      
# print(sumlist([1,2,3,4]))

# WORD FREQUENCY
# def word_frequency (phrase) :
#    result = {}
#    words = phrase.split()
#    for word in words:
#       if word not in result:
#          result [word] = 1
         
#    return result

# print(word_frequency(input("PLEASE ENTER YOUR PHRASE : ")))  

# PRACTISE
# def sum_list (numbers) :
#    count = 0
#    for number in numbers:
   
#     count += number
      
#    return count
# print(sum_list ([1,2,3,4]))

# PRACISE AGAIN

# def word_frequency (phrase):
#    result = {}
#    words = phrase.split()
#    for word in words:
#       if word  not in result:
#          result [word] = 1
         
#    return result
# print(word_frequency(input("Please enter your phrase: ")))  

# HIGHER ORDER FUNCTIONS
# def double_number(numbers):
   
#    return numbers * 2

# SAME CONTENT

# print(list(map(lambda num : num ** 2, [1,2,3,4])))

#FILTER METHOD 
# filterring even and old numbers
# numbers = [1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda num : num % 2 == 1, numbers)))

# LIST COMPREHESSIONS

# filter and give me even numbers.

# numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
# print([number for number in numbers if number % 2 == 1])

# map and double all numbers

# print([number * 2 for number in numbers])

# PROJECT
