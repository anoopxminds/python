#create a recursive function to calculate the sum of numbers from 0 to 10.

def recursive_fun(n):
    if n <= 1:
        return n;
    return n + (recursive_fun(n - 1))


def main():
    n = 5;
    print(recursive_fun(n));

main();
