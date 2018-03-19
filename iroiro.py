from short import *
from variables import *

# Here I have some lists for iroiro2
# I dunno if you need it, but anyway
# it must be language-independent, but surely depends of recording system

def get_VCVs_CV(): 
    # like "VCV,CV"
    global oto, suffix
    ren_tan = ""
    for line in oto.replace(suffix,"").replace("\n\n",br).split(br):
        if line.find(" ")!= -1:
            vcv = line.split(".wav=")[1]
            vcv = vcv.split(",")[0]
            cv = vcv.split(" ")[1]
            if cv == "r": cv = "rr"
            if vcv[-1] == "R": cv = "-"
            ren_tan += vcv + "," + cv + br
    f = open("iroiro2\Replace\VCV-CV\VCVs to CVs [RUS].txt", "w")
    f.write(ren_tan)
    f.close()

    
def get_CV_VCVs():
    #like "CV,V "
    global aliases
    tan_ren1 = [["R","-"],["-","-"]] # important
    tan_ren2 = []
    for v in aliases["V"]:
        try: 
            diftong_vowels.index(v)
            tan_ren1.append([v,v])
        except ValueError:
            tan_ren2.append([v,v])
    for cv in aliases["CV"]:
            try:
                vowels.index(cv[-2:])
                v = cv[-2:]
            except ValueError:
                v = cv[-1]
            if  (cv[0] == "y" or cv[0] == "ch" or cv.count("'") > 0) and v == "i":
                v = "'i"
            try: 
                diftong_vowels.index(v)
                tan_ren1.append([cv,v])
            except ValueError:
                tan_ren2.append([cv,v])
    tan_ren_text = ""
    for pair in tan_ren1:
        tan_ren_text += pair[0] + "," + pair[1] + " \n"
    for pair in tan_ren2:
        tan_ren_text += pair[0] + "," + pair[1] + " \n"
    f = open("iroiro2\Replace\CV-VCV\CV to VCVs [RUS].txt", "w")
    f.write(tan_ren_text)
    f.close()

    
def get_VCVs_fix(): 
    #like "wrong,right"
    global vowels
    tikan = ""
    for v in vowels:
        tikan += v + " rr," + v + " r\n"
        tikan += v + " " + v + " R," + v + " R\n"
        tikan += v + " -,"+ v + " R\n"
    tikan += "- rr,- r\n"
    f = open("iroiro2\Replace\Tikan\CV to VCVs fix.txt", "w")
    f.write(tikan)
    f.close()

    
def get_CVC1_to_VCVs():
    global aliases
    CVC1_to_VCVs = ""
    VCVs_to_CVC1 = ""
    VCVs_to_CVC1_presamp = ""
    for alias_type in aliases.keys():
        for alias in aliases[alias_type]:
            new_alias = alias
            
            new_alias = new_alias.replace("y","~")
            new_alias = new_alias.replace("ts","c")
            new_alias = new_alias.replace("zh","j")
            new_alias = new_alias.replace("sh","w")
            new_alias = new_alias.replace("oa","a")
            new_alias = new_alias.replace("ei","e")
            new_alias = new_alias.replace("i","y")
            new_alias = new_alias.replace("'y","'i")
            new_alias = new_alias.replace("ch","4'")
            
            if alias_type == "VV" or alias_type == "VCV":
                new_alias = new_alias.split(" ")[1]
                
            if alias_type == "VC":
                VCVs_to_CVC1_presamp += alias + comma + new_alias.split(" ")[1] + br
                
            new_alias = new_alias.replace(" R","-")
            new_alias = new_alias.replace(" ","")            
            
            if alias_type == "VC" or alias_type == "V-":
                new_alias = new_alias.replace("'i","i")
                
            if alias_type == "VC":
                CVC1_to_VCVs += new_alias + comma + "#DELETE_______________" + br
                CVC1_to_VCVs += new_alias + "-" + comma + alias.split(" ")[1] + br
                VCVs_to_CVC1 += alias + comma + new_alias + "-" + br
                
            if alias_type == "V":
                CVC1_to_VCVs += new_alias*2 + comma + alias + br
            
            if alias_type == "-V":
                g_alias = new_alias.replace("-","`")
                CVC1_to_VCVs += g_alias + comma + alias + br
                
            if alias_type == "V-":
                g_alias = new_alias.replace("-","`")
                CVC1_to_VCVs += g_alias + comma + alias + br
                
            if alias_type == "C":
                g_alias = new_alias + "-"
                CVC1_to_VCVs += g_alias + comma + alias + br
            
            if alias_type != "VCV" and alias_type != "VV" and alias_type != "VC":
                if alias != new_alias: 
                    CVC1_to_VCVs += new_alias + comma + alias + br
                
            new_alias = new_alias.replace("3","e")
            new_alias = new_alias.replace("x","a")
                
            if alias != new_alias: 
                VCVs_to_CVC1 += alias + comma + new_alias + br
                
            if alias_type == "V-":
                new_alias = "R"
            else:
                new_alias = new_alias.replace("-","")                
                
            if alias_type != "VC":
                if alias != new_alias: 
                    VCVs_to_CVC1_presamp += alias + comma + new_alias + br
    
    f = open("iroiro2\Replace\Tikan\CVC1_to_VCVs.txt", "w")
    f2 = open("iroiro2\Replace\Tikan\VCVs_to_CVC1.txt", "w")
    f3 = open("iroiro2\Replace\Tikan\VCVs_to_CVC1_presamp.txt", "w")
    f.write(CVC1_to_VCVs)
    f2.write(VCVs_to_CVC1)
    f3.write(VCVs_to_CVC1_presamp)
    f.close()
    f2.close()
    f3.close()

    
def get_CVC2_to_VCVs():
    # iroiro can't delete notes (VC), so probably I should write my own plugin. Some day
    global aliases
    CVC2_to_VCVs = ""
    VCVs_to_CVC2 = ""
    for alias_type in aliases.keys():
        for alias in aliases[alias_type]:
            new_alias = alias
            
            new_alias = new_alias.replace("oa","x")
            new_alias = new_alias.replace("ei","3")
            new_alias = new_alias.replace("zh","j")
        
            if alias_type == "VV" or alias_type == "VCV":
                new_alias = new_alias.split(" ")[1]
            
            if alias_type == "VC":
                CVC2_to_VCVs += "'" + new_alias + comma + "#DELETE_______________" + br
                CVC2_to_VCVs += new_alias + comma + "#DELETE_______________" + br
                
            if alias_type == "V":
                CVC2_to_VCVs += new_alias*2 + comma + alias + br
            
            if alias_type != "VCV" and alias_type != "VV" and alias_type != "VC":
                if alias != new_alias: 
                    CVC2_to_VCVs += new_alias + comma + alias + br
                
            new_alias = new_alias.replace("- ","")
            new_alias = new_alias.replace("3","e")
            new_alias = new_alias.replace("x","a")
                
            if alias != new_alias: 
                VCVs_to_CVC2 += alias + comma + new_alias + br
    
    f = open("iroiro2\Replace\Tikan\CVC2_to_VCVs.txt", "w")
    f2 = open("iroiro2\Replace\Tikan\VCVs_to_CVC2_presamp.txt", "w")
    f.write(CVC2_to_VCVs)
    f2.write(VCVs_to_CVC2)
    f.close()
    f2.close()
    
def get_iroiro_stuff(aliases_, oto_):
    global aliases, oto
    aliases = aliases_
    oto = oto_
    get_CV_VCVs()
    get_VCVs_CV()
    get_VCVs_fix()
    get_CVC1_to_VCVs()
    get_CVC2_to_VCVs()
        