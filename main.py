from redis_like import Redis
import re

r = Redis()

# considering that wont have any '<' or '>' in paramter value, just as param delimiter
# considering all inputs will be user input raw data, as string
no_param_pattern = "^(END|BEGGIN|ROLLBACK|COMMIT)$"
one_param_pattern = "^(GET|UNSET|NUMEQUALTO) <([^<>;]*)>$"
two_param_pattern = "^(SET) <([^<>;]*)><([^<>;]*)>$"

valid_pattern = re.compile(f"({no_param_pattern}|{one_param_pattern}|{two_param_pattern})")

def is_valid_input(input_value):
    # Big O = N
    # N: input_value lenght 
    return True if valid_pattern.match(input_value) else False

def get_parameters(input_value):
    # Big O = N
    # N: input_value lenght 
    params = input_value.split("<")
    if len(params) == 2:
        return [params[1][:len(params[1])-1]]
    else:
        return [params[1][:len(params[1])-1], params[2][:len(params[2])-1]]

def process_input(input_value):
    # Big O = N
    # N: input_value lenght 
    if "GET" in input_value:
        params = get_parameters(input_value)
        print(r.get(params[0]))
    
    elif "UNSET" in input_value:
        params = get_parameters(input_value)
        r.unset(params[0])
        print()
    
    elif "NUMEQUALTO" in input_value:
        params = get_parameters(input_value)
        print(r.num_equal_to(params[0]))
    
    elif "SET" in input_value:
        params = get_parameters(input_value)
        r.set(params[0], params[1])
        print()
    
    elif "BEGGIN" in input_value:
        r.beggin()
    
    elif "COMMIT" in input_value:
        r.commit()
    
    
    elif "ROLLBACK" in input_value:
        r.rollback()



user_input = None
print()
print("Redis-like started!")
print()
while user_input != "END":
    user_input = input()
    is_valid = is_valid_input(user_input)
    if is_valid:
        process_input(user_input)
    else:
        print("ERRO")