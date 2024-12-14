---
aliases:
abilitymodifiers: 
blurb:
cssclasses: 
hitpoints: 
size: 
sizeandtype: 
tags: []
type: 
---

>[!cards]
>
>`$= dv.page(dv.current().file.name).file.name + "-Card-Portrait.jpg" ? dv.fileLink(dv.current().file.name + "-Card-Portrait.jpg", true) : ""`
>
>`$= dv.page(dv.current().file.name).file.name + "-Card-Stats.jpg" ? dv.fileLink(dv.current().file.name + "-Card-Stats.jpg", true) : ""`
>
>>[!infobox|right wsmed]
>> # `= this.file.name`
>>`= choice(this.blurb, "![[" + this.blurb + "]]", "")`
>> # stats
>>
>>|||
>> |----|----|
>> |hp|`= this.hitpoints`|
>> |mods|`= this.abilitymodifiers`|
>> |size|`= this.size`|
>> |type|`= this.type`|
>>
>> # vitals
>> |||
>> |----|----|
>> |Average Height| `= this.height`|
>> |Average Weight| `= this.weight`| 
>> |Age of Maturity| `= this.maturity` |
>> |Maximum Age| `= this.age`|
>>