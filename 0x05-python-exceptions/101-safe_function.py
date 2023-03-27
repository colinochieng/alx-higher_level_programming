#!/usr/bin/python3

def safe_function(fct, *args):
    import sys
    result = 0
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result
