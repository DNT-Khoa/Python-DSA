'''
reverse
Write a recursive function called reverse which accepts a string and returns a new string in reverse.

Examples

reverse('python') # 'nohtyp'
reverse('appmillers') # 'srellimppa'
'''


def reverse(string):
    if len(string) == 1:
        return string[0]

    return string[-1] + reverse(string[:-1])


print(reverse('appmillers'))
