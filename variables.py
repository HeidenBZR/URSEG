from short import *

#######################################
#######################################
#######################################
# Here I define vowels and consonants
# All things below must be rewritten in a conf file. Some day

#######################################
#######################################
#######################################
# It's actually MUCH easier to remove a suffix with "find-replace" 
# than make two versions or even add a suffix with hands, so I add one by default
# and add a prefix.map with it
suffix = "_M"
vowels = "a i u e o ei oa 'i".split(" ")
# Vowels with 2 symbols, they have priority when I decide "which vowel it is"
diftong_vowels = "ei oa 'i".split(" ")

# Russian consonants has two models of behavior:
# 1. They may be hard and soft, and it matters in case of "i" and "'i" consonant,
# so you can't just make "everything with everything" transitions. Sadly
# 2. They may be voiceless and voiced consonants, and shit is what voiced may become unvoiced.
# It matters in case of CC: "voiced C" and "unvoiced C" pair becomes two unvoiced pair.
# And, like if those wasn't enough, not all consonants had hard-soft pair,
# and not all had voiced-unvoiced pair. 
# Actually I should made Class for consonant, but, I'm lazy and I don't have CC here,
# so I just have some arrays and I will compare with them, if I need.

# cons4 -- all of them have voiced-unvoiced and soft-hard pairs
cons4_ = "k-g s-z t-d f-v p-b".split(" ")
cons4 = []
for pair in cons4_:
    c1, c2 = pair.split("-")
    cons4.append(c1)
    cons4.append(c1+m)
    cons4.append(c2)
    cons4.append(c2+m)
# cons2 -- only have voiced-unvoiced OR soft-hard pairs
cons2_ = "l m n r h".split(" ")
cons2 = []
for c in cons2_:
    cons2.append(c)
    cons2.append(c+m)
# cons3 -- well you see
cons3 = "sh sh' zh".split(" ")
# cons1 -- totally unique
cons1 = "ts y ch".split(" ")
# now lets join it
consonants = [""]
consonants.extend(cons4)
consonants.extend(cons2)
consonants.extend(cons3)
consonants.extend(cons1)

#######################################
#######################################
#######################################
# I make cyrillic by replacing. It's actually pretty old list,
# And I added things much times, so this is not the most short and effective
# sequence of replacing, but it works, so I don't care >:D

cyrillic = [
    ("_hh",''),
    ('sh\'', 'щ\''),
    ('sh', 'ш'),
    ('ts', 'ц'),
    ('ch', 'ч\''),
    ('zh', 'ж'),
    ('b', 'б'),
    ('v', 'в'),
    ('g', 'г'),
    ('d', 'д'),
    ('z', 'з'),
    ('k', 'к'),
    ('l', 'л'),
    ('m', 'м'),
    ('n', 'н'),
    ('p', 'п'),
    ('r', 'р'),
    ('s', 'с'),
    ('t', 'т'),
    ('f', 'ф'),
    ('h', 'х'),
    ('y', 'й\''),
    ('oa', '(о)'),
    ('\'ei', '(е)'),
    ('ei', '(э)'),
    ('\'a', 'я'),
    ('\'e', 'е'),
    ('\'i', 'и'),
    ('\'o', 'ё'),
    ('\'u', 'ю'),
    ('a', 'а'),
    ('e', 'э'),
    ('i', 'ы'),
    ('o', 'о'),
    ('u', 'у'),
    ("'", 'ь'),
    ('йя', 'я'),
    ('йе', 'е'),
    ('йё', 'ё'),
    ('йю', 'ю'),
    ("шы",'ши'),
    ("жы",'жи'),
    ("йь",'й'),
    ("щь",'щ'),
    ("чя",'ча'),
    ("чю",'чу'),
    ("чё",'чо'),
    ("ь(о)","(я)")
]  

#######################################
#######################################
#######################################
# Here a put a templates. I had various

VCV_mask_old_chaotic_and_scary = '''
ca ca ci ce coa ce ci cac
ci ci cu co ca co cu cic
cu cu ce cei ci cei ce cuc
ce ce co coa cu coa co cec
co co cei ca ce ca cei coc
cei cei coa ci co ci coa ceic
coa coa ca cu cei cu ca coac
c'i ca c'i ci c'i cu c'i cec
c'i co c'i cei c'i coa c'i c'ic
'''.strip().replace(" ","_").replace("c","{0}")

VCV_mask_new_beautiful_and_util = '''
ca coa ca ci ce ci ca cac
ci coa ci cu co cu ci cic
cu coa cu ce ca ce cu cuc
ce cei ce co ci cu ce cec
co cei co ca cu ca co coc
c'i cei c'i ca c'i ci c'i cec
c'i coa c'i co c'i cu c'i c'ic
cei cei ca cei ci cei cu ceic
coa coa ce coa co coa cei coac
'''.strip().replace(" ","_").replace("c","{0}")

# Unfortunately ONE VCV doesn't get into 8mora line. So I have it here,
# already formated.
VCV_ei = '''
ke k'i ge g'i se s'i ze z'i
te t'i de d'i fe f'i ve v'i
pe p'i be b'i le l'i me m'i
ne n'i re r'i he h'i she sh'i
e 'i
'''.strip().replace(" ","_")

VCV_mask_6mora_too_many_lines = '''
ca ca ci ca cu cac
ci ci cu ci ce cic
cu cu ce cu co cuc
ce ce co ce ca cec
co co ca co ci coc
cei ca cei ci cei ceic
cei cu cei co cei coac
coa ca coa ci coa coac
coa cu coa co coa ceic
c'i ca c'i ci c'i cec
c'i cu c'i co c'i c'ic
c'i coa ce coa c'ic
c'i cei ce cei c'ic
'''.strip().replace(" ","_").replace("c","{0}")


reclist_mask = VCV_mask_new_beautiful_and_util
VCV_mask_len = len(reclist_mask.split("\n"))
reclist_extra = VCV_ei

#######################################
#######################################
#######################################
# using offset and step, I can make base options applicable for any tempo
# So instead of recounting ALL the parameters for ANY alias type, 
# I only need to count these two.

# for bpm 160
# length from start to first mora vowel start (offset+preutterance, actually), ms
offset = 1120 
# length between moras, ms
step = 750 
oto_options = {

    # beginning C
    "-C": [0, 145, -150, 60, 30],
    
    # beginning singing C
    "-C~": [0, 60, -80, 50, 30],
    
    # beginning CV
    "-CV": [0, 450, -600, 140, 100],
    
    # CV
    "CV": [0, 450, -600, 140, 100],
    
    # V to CV
    "VCV": [0, 500, -650, 200, 50],
    
    # C
    "C": [0, 200, 10, 50, 50],
    
    # singing C
    "C~": [0, 50, -80, 50, 50],
    
    # singing C ending
    "C~-": [20, 200, 10, 30, 30],
    
    # open V to C, or ending V to C
    "VC": [-50, 300, 10, 50, 50],
    
    # closed V to C, or normal V to C
    "VC~": [-80, 80, -120, 50, 50],
    
    # beginning V
    "-V": [0, 400, -500, 120, 60],
    
    # V
    "V": [0, 400, -500, 120, 60],
    
    # ending V
    "V-": [0, 250, 10, 100, 50],
    
    # V to V
    "VV": [0, 400, -550, 100, 50]
}

#######################################
#######################################
#######################################
# To make aliases

alias_format = '''-C=- %s
-C~=- %s~
-CV=- %s%s
CV=%s%s
VCV=%s %s%s
C=%s
C~=%s~
C~-=%s~ R
VC=%s %s
VC~=%s %s~
-V=- %s
V=%s
V-=%s R
VV=%s %s'''
alias_format_dict = {}
for line in alias_format.split("\n"):
    alias_type, format = line.split("=")
    alias_format_dict[alias_type] = format