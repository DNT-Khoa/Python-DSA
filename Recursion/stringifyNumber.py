'''
stringifyNumbers
Write a function called stringifyNumbers which takes in an object and finds all of the values which are numbers and converts them to strings. Recursion would be a great way to solve this!

Examples

obj = {
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}
 
stringifyNumbers(obj)
 
{'num': '1', 
 'test': [], 
 'data': {'val': '4', 
          'info': {'isRight': True, 'random': '66'}
          }
}
'''

obj1 = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}


def stringifyNumbers(obj):
    temp_obj = {}

    for key in obj:
        if type(obj[key]) is int or type(obj[key]) is float:
            temp_obj[key] = str(obj[key])
        elif type(obj[key]) is dict:
            temp_obj[key] = stringifyNumbers(obj[key])
        else:
            temp_obj[key] = obj[key]

    obj = temp_obj
    return obj


stringifyNumbers(obj1)
print(obj1)
