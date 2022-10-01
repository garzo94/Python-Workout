def myxml(tagname, content='',**kwargs):
    kwargs.items()
    args = ' '.join([f'{key}={value}' for key, value in kwargs.items()])
    print(args)
    return print(f'<{tagname} {args} >{content}</{tagname}>')

myxml('tagname', 'hello', a=1, b=2, c=3)