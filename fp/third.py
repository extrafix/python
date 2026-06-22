from pymonad.tools import curry

@curry(2)
def tag(tag_name, value): 
    return f"<{tag_name}>{value}</{tag_name}>"
    
def bold(value): 
    return tag("b")(value)
    
def italic(value): 
    return tag("i")(value)
    
print(bold("Title"))

print(italic("And sm-a-a-a-l opinion"))


@curry(3)
def tag(tag_name, arguments_dict, value):
    arguments = argumants_dictionary_to_str(arguments_dict)
    return f"<{tag_name} {arguments}>{value}</{tag_name}>"
    
# tag со списком аргументов

def argumants_dictionary_to_str(arguments_dict):
    arguments = ""
    for index, (key, value) in enumerate(arguments_dict.items()):
        if index >= 1:
            arguments = arguments + " " + (f"{key}=\"{value}\"")
        else:
            arguments = arguments + (f"{key}=\"{value}\"")
    return arguments


def bold(arguments_dict, value): 
    return tag("b")(arguments_dict)(value)
    
def italic(arguments_dict, value): 
    return tag("i")(arguments_dict)(value)
    
print(tag('li', {'class': 'list-group'}, 'item 23'))

# Out:
# <b>Title</b>
# <i>And sm-a-a-a-l opinion</i>
# <li class="list-group">item 23</li>

