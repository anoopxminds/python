#.Create a function in such a way that we can pass any number of integer numbers as arguments to this function, and the function should return the average of these integer numbers.

def avg_fun(*num):
      sum = 0;
      for i in num:
            sum = sum + i;
      avg = sum/len(num);
      print("Average : " + str(avg));
      return avg;


avg_fun(2, 6, 4, 8);
