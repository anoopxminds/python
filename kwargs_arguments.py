#Using the Python kwargs Variable in a function concatenate and print all the string arguments passed (Understanding **kwargs)

def print_kwargs(**kwargs):
    print(kwargs);

    for key,value in kwargs.items():
        print("This value of {} is {}". format(key, value));


print_kwargs(args_1="Shark", args_2= 6.5, args_3=True);