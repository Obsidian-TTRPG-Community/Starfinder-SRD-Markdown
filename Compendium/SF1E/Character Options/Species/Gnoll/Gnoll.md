---
abilitymodifiers: "+2 Str, +2 Con, –2 Int"
blurb:
cssclasses: 
date created: Tuesday, August 22nd 2023, 4:01:13 pm
date modified: Wednesday, August 21st 2024, 7:56:15 pm
hitpoints: "6"
size: "medium"
sizeandtype: "Gnolls are Medium Humanoids with the gnoll subtype."
tags: []
type: "humanoid (gnoll)"
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

[[Species_Gnoll.png|Zeigen!]]

Gnolls are hyena-headed humanoids with a reputation as bloodthirsty raiders, scavengers, and cannibals. They are capable hunters who respect power and strength over station or role, and most gnolls would believe their own survival takes precedence over any kind of morality.

**Ability Modifiers** +2 Str, +2 Con, –2 Int
**Hit Points** 6

## Size and Type

Gnolls are Humanoids with the gnoll subtype.

## Blindsense (scent)

Gnolls have blindsense (scent) with a range of 30 feet.

## Darkvision

Gnolls have darkvision with a range of 60 feet.

## Natural Weapons

Gnolls can attack with a special unarmed strike that deals lethal damage, doesn’t count as archaic, and threatens squares. Gnolls gain a special version of the Weapon Specialization feat with this unarmed strike at 3rd level, allowing them to add 1-1/2 × their character level TO their damage rolls for this unarmed strike (instead of just adding their character level, as usual).

## Rugged Travel

Each time they move, gnolls can move through the first square of nonmagical difficult terrain at their normal speed.

## Self-sufficient

Gnolls gain a +2 racial bonus to Survival checks.
