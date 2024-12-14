---
aliases: Ammunition
tags: #sf1e/items
---

# Ammunition

``` dataview
TABLE without ID
file.link as "Name", level, Price
FROM #ammunition 
SORT Level ASC
WHERE file.name != "Ammunition"
```
