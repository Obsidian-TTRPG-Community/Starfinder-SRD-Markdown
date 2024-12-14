---
aliases: 
tags: 
---

# Basic Melee - One Handed

``` dataview
TABLE WITHOUT ID
file.link as "Weapon", Level, Price, Damage, Critical
FROM "Compendium/SF1E/Items/Armaments/Basic Melee/One-Handed - Basic Melee"
SORT Level ASC
WHERE file.name != "One-Handed - Basic Melee"
```