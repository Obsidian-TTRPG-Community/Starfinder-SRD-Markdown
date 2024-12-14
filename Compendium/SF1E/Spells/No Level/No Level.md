---
aliases: 
tags: 
---

# No Level Spells

``` dataview
TABLE
School, Mystic as MYS, Precog as PRE, Technomancer as TM, Witchwarper as WW
FROM "Compendium/SF1E/Spells/No Level"
SORT file.name ASC
WHERE !contains(file.name, "No")
```