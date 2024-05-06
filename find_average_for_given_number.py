#.Create a function in such a way that we can pass any number of integer numbers as arguments to this function, and the function should return the average of these integer numbers.
list = []
def take_numbers(default_range = 3):
    for i in range(default_range):
            number = input('Enter number for find avarege : ');
            print(str(int(number)));
            list.append(int(number));
    return list;

#print(take_numbers());

def findAverage(number):
      if len(number) == 0 :
            print("Enter a valid number");
      else :  
            average = len(number)/sum(number);
            return average;

def main() :
      list = take_numbers();
      print("Average of given number is : "+ str(findAverage(list)));

main();
