---
aliases: 
tags: 
---

# Advanced Melee - One Handed

Any handheld weapon that must touch a target to damage it is considered a melee weapon. Advanced melee weapons require a degree of training and skill to use properly. Advanced melee weapons are divided into one-handed and two-handed weapons.


``` dataview
TABLE WITHOUT ID
file.link as "Weapon", Level, Price, Damage , Critical
FROM "Compendium/SF1E/Items/Armaments/Advanced Melee/One Handed - Advanced Melee"
SORT Level ASC
WHERE file.name != "One Handed - Advanced Melee"
```