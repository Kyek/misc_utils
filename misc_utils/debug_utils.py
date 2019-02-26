import os

def is_debug():
    debug = os.getenv('DEBUG') 
    if debug is None or debug not in ["True", "False"]:
        return False
    return eval(debug)

def debug_print(data_name, data_to_print=None):
    if is_debug(): 
        try:
            bar = '=' * 20
            data_name = bar + data_name + bar
            if data_to_print is not None:
                print(data_name)
                print(type(data_to_print))
                print(data_to_print)
                print('=' * len(data_name))
            else:
                print(data_name)
                print('=' * len(data_name))
        except Exception as e:
            debug_print('Oops, I was not expecting this', e)
