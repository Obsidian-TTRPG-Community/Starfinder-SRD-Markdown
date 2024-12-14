---
aliases: 
tags: 
---

# Longarms

``` dataview
TABLE WITHOUT ID
file.link AS "Weapon", Level, Price, Damage, Critical
FROM "Compendium/SF1E/Items/Armaments/Longarms"
SORT Level ASC
WHERE file.name != "Longarms"
```
