import codecs
from short import *
from variables import *
from utils import *
from rules import *
from iroiro import *


def get_reclist():
    global consonants, reclist, l, reclist, reclist_extra
    for C in consonants:
        reclist += add(get_masked(reclist_mask, C)) + br
    reclist += reclist_extra
    
    f = open('record pack/reclist.txt', 'w')
    f.write(reclist)
    f.close()
    
    reclist = reclist.replace(br*2,br)
    
    # if you would like to add lines number like "myreclist (553).txt", use it
    l = len(reclist.split(br))
        

def get_comments():
    # totally language depending, you know
    global consonants, cyrillic, comments, reclist
    comments = ""
    rec = reclist.split(br)
    cyr = [cyr_replace(line) for line in rec]
    for i in range(len(rec)):
        comments += add(rec[i],tab,cyr[i])
    comments += br
    
    with codecs.open('record pack/oremo-comment.txt', 'w', "utf-8-sig") as f:
        f.write(comments)
        f.close()
        

def get_oto():
    global consonants, oto, reclist, suffix, aliases
    
    for line in reclist.split(br):
    
        C = get_C(line)
        phonemes = phoneme_split(line, C)
        moras = get_moras(phonemes)
        
        to_alias = extract_aliases(line, moras, phonemes, C)
        
        for parameters in to_alias:
            line, phonemes, alias_type, mora = parameters
            alias = get_alias(phonemes, alias_type)
            options = get_oto_options(alias_type, mora)
            oto += oto_line(line, alias, options, mora)
            add_alias(aliases, alias, alias_type)
            add_alias_map(alias_map, alias, phonemes)
        oto += br
    
    oto = oto_post_replacing(oto)
    
    f = open('record pack/oto.ini', 'w')
    f.write(oto)
    f.close()
    
    
def get_atlas():
    # Info about this recoding system for some plugin
    global aliases, vowels, consonants, alias_format
    text = ""
    text += "[MAIN]" + br
    text += "vowels=" + ",".join(vowels) + br
    text += "consonants=" + ",".join(consonants)[1:] + br
    text += "[ALIAS]" + br
    for alias_type in aliases.keys():
        text += alias_type + "="
        for alias in aliases[alias_type]:
            text += alias + ","
        text += br
    text = text.replace(",\n","\n")
    text += "[FORMAT]" + br
    text += alias_format
    
    f = open("atlas/VCVs 0.2.ini", "w")
    f.write(text)
    f.close()
        

# just init
text = ""
reclist = ""
oto = ""
aliases = {}
alias_map = {}

# now let's get all this things
get_reclist()
get_comments()
get_oto()
get_atlas()
get_iroiro_stuff(aliases, oto)