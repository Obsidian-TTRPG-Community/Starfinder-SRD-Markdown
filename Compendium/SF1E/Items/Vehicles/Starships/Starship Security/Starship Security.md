---
aliases: 
tags: 
---

# Starship Security

The additions below help to prevent unwanted scoundrels from absconding with a starship. Security systems require an operational power core to function, but they consume a negligible amount of PCU. The cost of each option is listed in the table below.


``` dataview
TABLE
BPCost as BP-Cost, PCU
FROM "Starfinder-SRD/Compendium/Items/Vehicles/Starships/Starship Security"
SORT BPCost ASC
WHERE file.name != "Starship Security"
```