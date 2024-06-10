import logging

def word_list_to_string(word_list: list): 
    delimiter = " "
    result = "" 

    for word in word_list: 
        result += word
        result += delimiter
        
    return result 


# innter args/kwards handle "self" being passed from class methods
def disable_logging(callback):
    def decorated(*args, **kwargs):
        logging.disable(logging.CRITICAL)
        callback(*args, **kwargs)
        logging.disable(logging.NOTSET)
    return decorated
    