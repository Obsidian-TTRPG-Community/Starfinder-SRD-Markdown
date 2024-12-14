---
aliases: 
tags: 
---

# Spells Level 3

``` dataview
TABLE
School, Mystic as MYS, Precog as PRE, Technomancer as TM, Witchwarper as WW
FROM "Compendium/SF1E/Spells/Spells Level 3"
SORT file.name ASC
WHERE !contains(file.name, "Spells")
```