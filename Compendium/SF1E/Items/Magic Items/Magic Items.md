---
aliases: 
tags: 
---

# Magic Items

**Source**:: _Starfinder Core Rulebook pg. 222_  
While plenty of technology in Starfinder incorporates magical elements, some items operate solely through eldritch principles and thus follow different rules. This section covers magic items not addressed under another rules system (such as [[Weapon Fusions]] or [[Augmentations|augmentations]]). Magic items are often divided into held, worn, and consumable items. Held items (such as orbs and rods) must be held in a hand or similar appendage and activated manually like a weapon.  
  
Worn magic items are things like rings, cloaks, amulets, and gloves. Just as your [[Armor]] has a limited number of upgrade slots, you can only wear up to two magic items at once and have both function normally—beyond that, the magical fields start to interfere with each other. You can’t wear more than one of the same type of item (two cloaks, two hats, etc.) except for rings. If you put on an additional worn magic item beyond these first two, it does not function until you have no more than two total magic items worn. This limitation applies specifically to worn magic items, and does not apply to [[Armor]] upgrades, held items, [[Weapon Fusions]], [[Augmentations|augmentations]], magic [[Armor]], consumables, or other forms of magic, all of which function normally.  
  
Lastly, consumables are magic items like [[Serums]] or spell ampoules that create an immediate and temporary effect when ingested.  

## Charges

In a few rare cases, magic items require charges. However, such charged magic items function differently than charged [[Technological Items]], whose batteries must be recharged or replaced. A magic item’s charges are inherent to the construction of the item and can’t be replenished with generators or batteries. Charges for a magic item either refresh each day or never refresh, depending on the item.

``` dataview
TABLE
Level, Price, Bulk

FROM "Starfinder-SRD/SF1E/Compendium/Items"
SORT Level ASC
WHERE type = "Magic Item"
WHERE file.name != "Magic Items"
```
