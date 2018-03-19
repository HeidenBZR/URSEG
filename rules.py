from short import *
from variables import *

# Implementation of these functions depends of language and recoding system
# You probably need to change them the whole if you gonna make you own recording system

def get_masked(reclist_mask, C):

    # Get real reclist from mask
    masked = reclist_mask.format(C)
    if len(C) > 0:
    
        if C[-1] == "'":
            # in "'" lines, I want get transitions like "c'i ca c'i ci c'i cu c'i cec" 
            # OR "ci c'a ci c'i ci c'u ci c'ec'"
            # so if I have a hard consonant, after formating mask 
            # I'm getting "c'i ca c'i ci c'i cu c'i cec"  and that's OK
            # and if I have a soft consonant, after formating mask 
            # I'm getting "c''i c'a c''i c'i c''i c'u c''i c'ec'"
            # so I only need to do a thing below and TA-DAA I'll get "ci c'a ci c'i ci c'u ci c'ec'"
            masked = masked.replace("''","")
            
        elif C == "ts" or C == "zh":
        
            # as far as they don't have a sort pair...
            masked = reclist_mask.replace("{0}'","k'").format(C)
        elif C == "ch" or C == "y":
        
            # as far as they don't have a hard pair...
            masked = reclist_mask.replace("{0}'","k").format(C)
    return masked
    

def phoneme_split(line, C): 

    # get an array of phonemes from a string line
    # this is very difficult. There must be another way, but.
    global vowels
    if C == "":
    
        # Vowel line
        return line.replace(br,"").split("_")
    else:
    
        old_line = line
        
        # to simplify splitting, I must have all the vowels to be single-character
        line = line.replace("oa", "O").replace("ei", "E").replace("'i", "I")
        
        # here I add spaces to split with them later
        for v in vowels:
        
            # again, must be single-character
            v = v.replace("oa", "O").replace("ei", "E").replace("'i", "I")
            
            # I want "k'i" to be "k' 'i", not "k 'i" or "k' i", for correct alias naming
            if v == "I":
                line = line.replace(v, "' "+v+" ")
            else:
                line = line.replace(v, " "+v+" ")
                
            # Some superfluous spaces I don't need
            line = line.replace("  ", " ")
        
        # in my "format" I have spaces because it's easier to read with them while you making a template
        # but in reclist I need underlines
        line = line.replace(br,"").replace("_","")
        
        # again, I need everything to be single-character. 
        # So soft consonants temporary become uppercases and loses apostrophe
        C = C.replace("'", "")
        
        line = line.replace(C+"'",C.upper())
        
        # in case of zh and ts line, "k'" appears too, so I must replace to uppercase it too
        line = line.replace("k'","K")
        
        # well you see
        line = line.replace("ch i","ch I").replace("y i","y I")
        
        # and now I add more spaces
        line = line.replace(C, " "+C+" ").replace(C.upper(), " "+C.upper()+" ")
        
        # and now kick superfluous ones
        line = line.replace("  ", " ").replace("  "," ")
        
        # TA-DA I have all phonemes separated by one space character
        
        # So I do back character replacing now
        line = line.replace("O", "oa").replace("E", "ei").replace("I", "'i")
        line = line.replace(C.upper(),C+"'")
        line = line.replace("K","k'")
        
        # Kick spaces in start and end of line
        line = line.strip()
        
        # PHEW that's all
        return line.split(" ")
        
def extract_aliases(line, moras, phonemes, C):
    # It's pretty big because I don't want any alias wherever it possible,
    # like get "- k" from any lines which contains it, only one instance of each alias. 
    # A tip for reading: look for alias naming first, and then read which condition it has.
    
    is_a_line = is_it_a_line(phonemes)
    is_i_line = is_it_i_line(line, C)
    
    to_alias = []
    
    # For vowel lines
    if C == "":
        if line != "e_'i":
            to_alias.append([line, [phonemes[0]], "-V", 0])
            to_alias.append([line, [phonemes[0]], "V", 0])
        for i in range(moras-1):
            to_alias.append([line, [phonemes[i],phonemes[i+1]], "VV", i+1])
        if line != "e_'i":
            to_alias.append([line, [phonemes[moras-1]], "V-", moras])
    
    # For another lines
    else:    
        if is_a_line and not is_i_line:
            to_alias.append([line, [phonemes[0]], "-C", 0])
            to_alias.append([line, [phonemes[0]], "-C~", 0])
        if not is_i_line:
            to_alias.append([line, [phonemes[0],phonemes[1]], "-CV", 0])
            to_alias.append([line, [phonemes[0],phonemes[1]], "CV", 0])
            for i in range(moras-1):
                to_alias.append([line, [phonemes[i*2+1],phonemes[i*2+2],phonemes[i*2+3]], "VCV", i+1])
                
        else:        
            for i in range(moras//2-1):
                to_alias.append([line, [phonemes[i*4+1],phonemes[i*4+2],phonemes[i*4+3]], "VCV", i*2+1])
            if not( phonemes[-4]+phonemes[-2] == "ii" or 
                    phonemes[-5]+phonemes[-3] == "ii" or 
                    phonemes[-4]+phonemes[-2] == "'i'i" or 
                    phonemes[-5]+phonemes[-3] == "'i'i"):
                to_alias.append([line, [phonemes[moras*2-3],phonemes[moras*2-2],phonemes[moras*2-1]], "VCV", moras-1])
                
        if not (is_i_line and (phonemes[-2] == "e" or phonemes[-3] == "e")):
            to_alias.append([line, [phonemes[moras*2-1],phonemes[moras*2]], "VC", moras])
            to_alias.append([line, [phonemes[moras*2-1],phonemes[moras*2]], "VC~", 1])
        if is_a_line and not is_i_line:
            to_alias.append([line, [phonemes[0]], "C", moras])
            to_alias.append([line, [phonemes[0]], "C~", moras])
            to_alias.append([line, [phonemes[0]], "C~-", moras])
            
    return to_alias

def get_C(line):
    # Actually I should rewrite it like"for C in consonants, if C in line", but I'm too lazy
    global consonants
    if line[1]+line[4:6] == "e'i":
        return line[0]
    try:
        # 3 symbol consonant
        consonants.index(line[-3:]) 
        return line[-3:]
    except ValueError:
        try:
            # 2 symbol consonant
            consonants.index(line[-2:]) 
            return line[-2:]
        except ValueError:
            try:
                # 1 symbol consonant
                consonants.index(line[-1]) 
                return line[-1]
            except ValueError:
                return "" # vowel line

def is_it_i_line(line, C):
    # For russian.
    # i line only gives VCV from 'i to hard consonants or from 'i to soft ones
    if cons1.count(C) > 0: 
        # ts ch y
        is_i_line = line.find("k") != -1
    elif C.find("'") == -1: 
        # soft consonant
        is_i_line = line.find(C+"'i") != -1 or line.find(C+"'i"+C) != -1
    else: 
        # hard consonant 
        C_ = C.replace("'", "")
        is_i_line = line.find(C_+"i") != -1 or line.find(C_+"i"+C) != -1
    return is_i_line
    
def is_it_a_line(phonemes):
    # because some aliases like "C" are taken only from a-line
    return phonemes[1] == "a"
    
def alias_pre_replacing(phonemes, alias_type):

    # I don't want things like "k''i" or "a k''i"
    if alias_type in ["VCV", "CV", "-CV"]:
        phonemes[-1] = phonemes[-1].replace("'", "")
        
    return phonemes
        
def alias_post_replacing(alias, alias_type):
    
    alias = alias.replace("ch'i","chi")
    alias = alias.replace("y'i","yi")
    
    return alias
    
def oto_post_replacing(oto):
    
    oto = oto.replace("=r%s," % suffix, "=rr%s," % suffix)
    return oto;