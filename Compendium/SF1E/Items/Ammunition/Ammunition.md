---
aliases: Ammunition
tags: #sf1e/items
---

# Ammunition

``` dataview
TABLE without ID
link(file.path, aliases) as Name,
level, price, type
FROM #sf1e/items/ammunition 
SORT Level ASC
WHERE file.name != "Ammunition"
```
