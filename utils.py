from short import *
from variables import *
from rules import *

# There are some functions, which don't depends of language and recording system

def add(*stuff):
    # not very genius, it just made the other code shorter.
    text = ""
    for A in stuff:   
        text += A
    text += br
    return text

def cyr_replace(line): 

    # Get a cyrillic by sequence of replacing
    global cyrillic
    for (lat, cyr) in cyrillic:
        line = line.replace(lat, cyr)
    return line

def oto_line(line, alias, options, mora):
    global oto, suffix
    
    oto_line = line + ".wav=" + alias + suffix
    for op in options:
        oto_line += comma + str(op)
    return oto_line + br

    
def get_alias(phonemes, alias_type):
    # well, get alias.
    global alias_format, aliases
    
    # May be you want make some replacing before you format alias
    phonemes = alias_pre_replacing(phonemes, alias_type)
        
    alias = alias_format_dict[alias_type] % tuple(phonemes)
    
    # and may be there are some replacing after.
    # Like, for japanese you could replace romaji to hiragana for CV, VCV and V in this function
    alias = alias_post_replacing(alias, alias_type)
        
    return alias_format_dict[alias_type] % tuple(phonemes)
    
def get_oto_options(alias_type, mora):
    
    global offset, step
    
    # if i don't do "list", it changes the original dict
    options = list(oto_options[alias_type]) 
    
    if alias_type == "-C":
        # I distract a "consonant"
        options[0] = options[0] + offset + step*mora - options[1] 
    else:
        # I distract a "preutterance"
        options[0] = options[0] + offset + step*mora - options[3] 
        
    return options
                

def get_moras(phonemes):
    # may differ, so
    global vowels
    n = 0
    for v in vowels:
        n += phonemes.count(v)
    return n
    
def add_alias(aliases, alias, alias_type):
    # Here I  collect a dictionary of aliases
    if alias_type in aliases.keys():
        aliases[alias_type].append(alias)
    else:
        aliases[alias_type] = []
        aliases[alias_type].append(alias)
    return aliases
    
def add_alias_map(alias_map, alias, phonemes):
    # I don't use it, but you may need it, e.g. for presamp.ini or autoCVVC list generating
    # (I made my presamp.ini manually, though)
    alias_map[alias] = phonemes