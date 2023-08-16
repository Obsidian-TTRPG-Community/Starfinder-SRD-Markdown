---
aliases: 
tags: 
---
# STARSHIP ARMOR
Armor protects a ship from direct-fire weapons (see Type on page 303), deflecting their energy and preventing damage to critical ship systems. It grants an armor bonus to a ship’s AC. Armor’s cost depends on the bonus it grants and the ship’s size category (for the purpose of this calculation, Tiny = 1, Small = 2, Medium = 3, Large = 4, etc.). Armor is a passive system and does not require any PCU to remain functional. It provides protection primarily through mass, which can affect a ship’s maneuverability (making it harder to turn) and make it easier for opponents using tracking weapons to lock on to the ship— these effects are listed in the Special column of the table below.

## ABLATIVE ARMOR

**Source** _Starship Operations Manual pg. 20_  
By layering inexpensive metal and composite plates over existing bulkheads, a ship can absorb initial damage to its hull before its essential components become vulnerable to attack or hostile environments. However, thicker plates are bulky and interfere with the maneuverability and handling of starships. Ablative armor grants a starship temporary Hull Points to each quadrant, usually distributed evenly. When a starship would take damage to its Hull Points, it first reduces its temporary Hull Points from ablative armor in that quadrant. Once a starship’s temporary Hull Points in a quadrant are reduced to 0, any further damage to that quadrant not absorbed by [[Starship Shields|shields]] is applied to the ship’s Hull Points. The loss of temporary Hull Points does not count toward the starship’s critical threshold, though for all other effects, any attack that reduces a starship’s temporary Hull Points is treated as though it had dealt Hull Point damage to the target.

In most cases, ablative armor is applied evenly, distributing its temporary Hull Points between all four quadrants. However, a starship can support uneven distribution at the cost of the starship’s handling, though the vessel can add only a limited amount of extra armor to smaller hulls. If a starship’s ablative armor is not installed evenly across all four quadrants, reduce the starship’s base frame Piloting modifier by 1 (minimum –3). Reduce the Piloting modifier by 1 if the temporary Hull Points granted by ablative armor exceed the starship’s Hull Point total. A starship cannot support ablative armor if its temporary Hull Points exceed twice its standard Hull Point total.

Ablative armor can be restored only when the starship undergoes repairs, and it is repaired at the same rate and cost as standard Hull Points. A starship’s Hull Points must be fully repaired before making repairs to any temporary Hull Points provided by ablative armor.

``` dataview
TABLE
BPCost as BP-Cost, PCU
FROM "Codex/Gear, Weapons, Vehicles & more/Vehicles/Starships/Starship Armor"
SORT BPCost ASC
WHERE file.name != "Starship Armor"
```