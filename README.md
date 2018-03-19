URSEG – Utau Recording System Extended Generator. Generate reclist, base oto, comments and other things

I made it for my russian VCVs reclist. It has no CC, so you need to add this part, if you need them; URSEG is not-so-hard to be changed for any language or recording system. May be some day it becomes absolutely universal, but now you need to change some code for your needs.

It's under GPLv3, so feel free use/change for whatever.
You may offer some stuff to make this script more universal, but I can't promise any reaction, just for a case. I'd like you to credit me, it's not obligatory.

Doesn't requires anything but Python 3(.4) itself "record pack", "atlas" and "iroiro" (for replacement lists) folders nearby.

Contains:
1. main.py – main
2. utils.py – some universal funtions
3. variables.py – instead of config file
4. rules.py – functions that depend on language and/or recording system
5. short.py - just some abbreviations
6. iroiro.py – here I generated my replacement and CV-VCV lists. Change it and use for your needs if necessary

Current version is: 0.1