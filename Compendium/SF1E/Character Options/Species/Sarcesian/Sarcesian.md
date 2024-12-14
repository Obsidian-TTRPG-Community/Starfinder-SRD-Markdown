---
abilitymodifiers: "+2 Dex, +2 Cha, -2 Str"
blurb:
cssclasses: 
date created: Tuesday, August 22nd 2023, 4:01:13 pm
date modified: Wednesday, August 21st 2024, 7:56:18 pm
hitpoints: "4"
size: "large"
sizeandtype: "Sarcesians are Large humanoids with the sarcesian subtype and a space and reach of 10 feet."
tags: []
type: "humanoid (sarcesian)"
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
# Sarcesian

> [!infobox|left n-th clean]
>  [[Sarcesian.png|Spielern zeigen!]]
> Supposedly descended from the inhabitants of the two planets whose destruction long ago formed the Diaspora asteroid belt, sarcesians have adapted to low-gravity and thinair environments. Standing between 10 and 15 feet tall with bulbous eyes and spindly, elongated limbs, a sarcesian is able to adapt her physiology to survive in space by suspending her respiration and growing a pair of butterfly-like wings made of pure light. The wings act as solar sails, catching currents of radiation to propel her between the handful of inhabited asteroids and space platforms within the Diaspora.
>
Thanks to arcane engines left behind by the sarcesians’ ancestors, the race has long managed to maintain creche worlds—asteroids with enough magical atmosphere, gravity, and warmth for the inhabitants to live comfortably and raise offspring. Compared to some other planets in the Golarion system, sarcesian creche worlds are beautiful and idyllic. They contain fields, forests, hills, lakes, and bucolic towns whose populations number in the low thousands. Many of these sanctuaries are linked by the River Between, an unusual body of water that actually flows between and through the asteroids; the water is prevented from floating off into space by a tube-shaped force field crafted by unknown hands.

Sarcesians who leave the asteroid belt are sometimes hired as mercenaries specializing in surveillance and marksmanship, as they are accustomed to operating at vast distances from their targets. These sarcesians hone their innate patience even further in order to lie in wait for their marks for days atop bluffs, in dilapidated apartments, or even in the vacuum of space outside docking slips. Employers tend to pay well for this degree of dedication, making sarcesian snipers a highly sought-after commodity in certain areas of the galaxy.

**Ability Modifiers** +2 Dex, +2 Cha, -2 Str
**Hit Points** 4

## Size and Type

Sarcesians are Large humanoids with the sarcesian subtype and a space and reach of 10 feet.

## Low-light Vision

Sarcesians can see in dim light as if it were normal light.

## Skilled

Sarcesians gain an additional skill rank at 1st level and each level thereafter.

## Void Flyer

Sarcesians can go 1 hour without breathing and can exist in a vacuum without suffering the associated environmental effects. When in a vacuum, they automatically grow wings made from pure energy that grant them a supernatural fly speed of 60 feet (average maneuverability) but that work only in a vacuum.

# Vital Stats

**Average Height** (height:: 10-15 ft.)
**Average Weight** (weight:: 400–500 lbs.)
**Age of Maturity** (maturity:: 20 years)
**Maximum Age** (age:: 140+3d20 years)
