import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f' {func.__name__} with args={args}, kwargs={kwargs} ')
        result = func(*args, **kwargs)
        logging.info(f' {func.__name__} returned {result} ')
        return result
    return decorated


# @log_function_call
def my_function(a ,b):
    return a + b




# print(my_function(1, 2))
print(log_function_call(my_function)(1, 2))


"""
Output :
3
"""