---
abilitymodifiers: "+2 Int, +2 Wis, –2 Con"
blurb:
cssclasses: 
date created: Tuesday, August 22nd 2023, 4:01:13 pm
date modified: Wednesday, August 21st 2024, 7:56:17 pm
hitpoints: "4"
size: "medium"
sizeandtype: "Samsarans are Humanoids with the samsaran subtype."
tags: []
type: "humanoid (samsaran)"
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
# Samsaran

> [!infobox|right]
>  [[Samsaran.jpeg|Spielern zeigen!]]
>
**Source**:: _Starfinder Alien Character Deck pg. 0_
Samsarans are mysterious humanoids who experience an endless cycle of birth to death to rebirth. When a samsaran dies, they reincarnate into a young samsaran to live a new life. The memories of their past lives are hazy and indistinct, but most samsarans seek lives of balance and enlightenment to ensure their continuing rebirth.

**Ability Modifiers** +2 Int, +2 Wis, –2 Con
**Hit Points** 4

## Size and Type

Samsarans are Humanoids with the samsaran subtype.

## Lifebound

Samsarans gain a +2 racial bonus to saving throws against death effects, saving throws to remove negative levels, and Constitution checks for long-term stability.

## Low-light Vision

Samsarans have low-light vision.

## Samsaran Magic

Samsarans gain the following spell-like abilities: 1/day—_comprehend languages, share memory, stabilize_. The caster level for these effects is equal to the samsaran’s character level.

## Shards of the past

As a legacy of their past lives, samsarans gain a +2 racial bonus to any two skills of their choice.
