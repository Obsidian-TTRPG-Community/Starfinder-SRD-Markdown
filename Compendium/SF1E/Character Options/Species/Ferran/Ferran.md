---
abilitymodifiers: 
blurb:
cssclasses: 
hitpoints: 
portrait: 
size: 
sizeandtype: 
source: 
stats: 
tags: 
type:
---

>[!infobox|txt-s n-th]
>`= choice(this.blurb, "![[" + this.blurb + "]]", "")`
> # stats
>
>|||
> |----:|:----|
> |**hp**|`= this.hitpoints`|
> |**mods**|`= this.abilitymodifiers`|
> |**size**|`= this.size`|
> |**type**|`= this.type`|
> |**Source**|`=this.source`|
>
> # vitals
>
> |||
> |----|----|
> |Average Height| `= this.height`|
> |Average Weight| `= this.weight`| 
> |Age of Maturity| `= this.maturity` |
> |Maximum Age| `= this.age`|
>
>`= choice(this.stats, "![[" + this.stats + "|ws-med]]", "")`
>`= choice(this.portrait, "![[" + this.portrait + "|ws-med]]", "")`
