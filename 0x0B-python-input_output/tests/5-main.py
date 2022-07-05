#!/usr/bin/python3
from .utils import CURRENT_DIR

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = CURRENT_DIR + "/my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filename)

filename = CURRENT_DIR + "/my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filename)

try:
    filename = CURRENT_DIR + "/my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filename)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
