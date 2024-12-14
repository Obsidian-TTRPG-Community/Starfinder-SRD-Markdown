---
aliases: []
abilitymodifiers: "+2 Con, +2 Int, -2 Str"
blurb:
cssclasses: 
date created: Tuesday, August 22nd 2023, 4:01:13 pm
date modified: Wednesday, August 21st 2024, 7:56:19 pm
hitpoints: "4"
size: "medium"
sizeandtype: "Verthani are Medium humanoids with the verthani subtype."
tags: []
type: "humanoid (verthani)"
---

>[!infobox|right wsmall relative]
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

`$= dv.page(dv.current().file.name).file.name + "-Card-Portrait.jpg" ? dv.fileLink(dv.current().file.name + "-Card-Portrait.jpg|wsmall relative left", true) : ""` `$= dv.page(dv.current().file.name).file.name + "-Card-Stats.jpg" ? dv.fileLink(dv.current().file.name + "-Card-Stats.jpg|center wsmall relative", true) : ""`

# Verthani

Verthani, the primary inhabitants of Verces, were some of the earliest humanoids in the Pact Worlds system to build spacefaring vessels—a response to the struggle to survive in the harsh conditions of their tidally locked planet.

Verthani stand 8 feet tall on average, with delicate features and long limbs. Their eyes are pure-black orbs, protruding from their heads in half domes like the eyes of a mouse, and they can change the pigment of their skin at will to have complex patterns. Nearly all verthani learn to control these color changes by the time they reach puberty, but babies and children display bright, expressive patterns and colors that reflect their current mood. Some adults also refuse to control them, seeing in their random patterns hints of prophecy.

Long ago, verthani society was split into three castes: the Augmented, the Pure Ones, and the God-Vessels. A verthani’s caste is chosen during adolescence. Though few verthani today bind themselves strictly by the system’s rules, the traditions still carry a measure of cultural pride, and some verthani proudly wear the labels.

The Augmented are verthani who modify their bodies with technology, usually cybernetic augmentations. This caste was particularly popular with those who piloted early aetherships (the elegant vessels verthani first sailed through the stars), and Augmented verthani pilots are still renowned as some of the most skilled in the Pact Worlds.

In contrast, Pure Ones traditionally eschewed all technological augmentation and were responsible for supporting other castes, farming, and governing. While many modern Pure Ones have accepted at least some modest cybernetic or biotech improvements to their bodies, these verthani remain proud of their traditional caretaker roles.

God-Vessels serve faithfully as living avatars of their deities, displaying this status by branding holy symbols called devotionals into their chests using either acid or flame. God-Vessels never cover up these distinctive marks, despite the fact that the scar tissue around them never fully heals and can no longer change color.

Verthani culture is a model of independent, democratic cooperation. Forced to live on a cramped sliver of their planet, surrounded by nearly inhospitable lands on either side, verthani learned how to work together without violence or subjugation, and they choose to harness technology to increase resources rather than battle one another over scraps. Verces’s Ring of Nations remains a shining example of a one-world government in which citizens remain protected yet free to go their own way, and in many ways the Pact Worlds system itself was directly inspired by this aspect of verthani culture.

**Ability Modifiers** +2 Con, +2 Int, -2 Str
**Hit Points** 4

## Size and Type

Verthani are Medium humanoids with the verthani subtype.

## Easily Augmented

Verthani have spent a long time implanting devices into their bodies. A verthani can install an additional augmentation (cybernetics only) into one system that already has an augmentation.

## Low-light Vision

Verthani have low-light vision.

## Skill Focus

Verthani are highly skilled, though individually they tend to focus on a particular discipline. Verthani gain Skill Focus as a bonus feat.

## Skin Mimic

Verthani can manipulate the pigments in their skin at will and with astonishing precision, creating bright decorative patterns or deceptive camouflage. A verthani who stays stationary for 1 round gains a +10 racial bonus to Stealth checks (this bonus doesn’t stack with the _invisibility_ spell or similar effects). If the verthani takes any action, he loses this bonus until he once again spends 1 round remaining still. A verthani wearing clothing or armor that covers more than one-quarter of his body can’t use this ability. 

# Vital Stats

**Average Height** (height:: 7-9 ft.)
**Average Weight** (weight:: 200–350 lbs.)
**Age of Maturity** (maturity:: 16 years)
**Maximum Age** (age:: 80+3d20 years)
