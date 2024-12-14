---
aliases: 
tags: 
---

# Basic Melee - Two Handed

``` dataview
TABLE WITHOUT ID
file.link AS "Weapon", Level, Price, Damage , Critical
FROM "Compendium/SF1E/Items/Armaments/Basic Melee/Two-Handed - Basic Melee"
SORT Level ASC
WHERE file.name != "Two-Handed - Basic Melee"
```