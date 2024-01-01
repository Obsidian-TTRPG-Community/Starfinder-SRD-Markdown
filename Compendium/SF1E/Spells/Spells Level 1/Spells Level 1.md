---
aliases: 
tags: 
---

# Spells Level 1

``` dataview
TABLE
School, Mystic as MYS, Precog as PRE, Technomancer as TM, Witchwarper as WW
FROM "Starfinder-SRD/SF1E/Compendium/Spells/Spells Level 1"
SORT file.name ASC
WHERE !contains(file.name, "Spells")
```