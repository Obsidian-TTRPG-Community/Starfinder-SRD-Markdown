---
abilitymodifiers: "+2 Dex, +2 Cha, –2 Str"
blurb:
cssclasses: 
date created: Tuesday, August 22nd 2023, 4:01:13 pm
date modified: Wednesday, August 21st 2024, 7:56:16 pm
hitpoints: "4"
size: "medium"
sizeandtype: "Kitsune are Humanoids with the kitsune and shapechanger subtype."
tags: []
type: "humanoid (kitsune, shapechanger)"
---

>[!infobox|right wsmed]
>`= choice(this.blurb, "![[" + this.blurb + "]]", "")`
> # `= this.file.name`
>
> |stats|
> |----|----|
> |hp|`= this.hitpoints`|
> |mods|`= this.abilitymodifiers`|
> |size|`= this.size`|
> |type|`= this.type`|
>
>
> |vitals|
> |----|----|
> |Average Height| `= this.height`|
> |Average Weight| `= this.weight`| 
> |Age of Maturity| `= this.maturity` |
> |Maximum Age| `= this.age`|
>
>`$= dv.page(dv.current().file.name).file.name + "-Card-Stats.jpg" ? dv.fileLink(dv.current().file.name + "-Card-Stats.jpg", true) : ""`
>
>`$= dv.page(dv.current().file.name).file.name + "-Card-Portrait.jpg" ? dv.fileLink(dv.current().file.name + "-Card-Portrait.jpg", true) : ""`
>
**Source**:: _Starfinder Alien Character Deck pg. 0_

[[Species_Kitsune.png|Zeigen!]]
Kitsune are a species of shapechangers with two forms: an anthropomorphic fox (their true form) and an attractive humanoid. Kitsune have a well-deserved reputation as duplicitous tricksters, but they are good-natured and value friendship and loyalty.

**Ability Modifiers** +2 Dex, +2 Cha, –2 Str
**Hit Points** 4

## Size and Type

Kitsune are Humanoids with the kitsune and shapechanger subtype.

## Agile

Kitsune gain a +2 racial bonus to Acrobatics and Athletics checks.

## Change Shape

As a standard action, a kitsune can assume the appearance of a specific single Medium humanoid. The kitsune always takes this specific form when using this ability. The kitsune gains a +10 racial bonus to Disguise checks to appear as that type of humanoid. This ability otherwise functions as disguise self, except that the kitsune can remain in this form indefinitely.

## Kitsune Magic

Kitsune gain the following spell-like abilities: 3/day—_dancing lights_, At will—_token spell_. The caster level for these effects is equal to the kitsune’s character level.

## Low-light Vision

Kitsune have low-light vision.
