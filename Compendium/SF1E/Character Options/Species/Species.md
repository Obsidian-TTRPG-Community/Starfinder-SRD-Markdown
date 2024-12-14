---
aliases: 
cssclasses: []
date created: Friday, January 12th 2024, 10:01:56 pm
date modified: Wednesday, August 21st 2024, 7:56:12 pm
tags: 
type:
---

## Core
```dataview
TABLE WITHOUT ID
file.link as "Species", hitpoints as "HP", abilitymodifiers as "mods", size, type
FROM "Compendium/SF1E/Character Options/Species"
WHERE section = "core"
```

## Legacy
```dataview
TABLE WITHOUT ID
file.link as "Species", hitpoints as "HP", abilitymodifiers as "mods", size, type
FROM "Compendium/SF1E/Character Options/Species"
WHERE section = "legacy"
```

## Alien Species
```dataview
TABLE WITHOUT ID
file.link as "Species", hitpoints as "HP", abilitymodifiers as "mods", size, type
FROM "Compendium/SF1E/Character Options/Species"
WHERE section = null
```

