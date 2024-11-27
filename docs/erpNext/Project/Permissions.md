### Fields with permisison level higher than 0

```sql
SELECT parent, fieldname, label, permlevel, fieldtype
FROM tabDocField
WHERE  permlevel <> 0;
```


| Job 1                      |
|----------------------------|
| Permissions as per docType |

In Project docTYpe thee is no field with permission level other than 0.

| parent            | role             | permlevel | idx | if_owner | amend | cancel | create | delete | email | export | import | print | read | report | select | share | submit | write |
|-------------------|------------------|-----------|-----|----------|-------|--------|--------|--------|-------|--------|--------|-------|------|--------|--------|-------|--------|-------|
| Project           | Projects User    |         0 |   1 |        0 |     0 |      0 |      1 |      1 |     1 |      0 |      0 |     1 |    1 |      1 |      0 |     1 |      0 |     1 |
| Project           | Desk User        |         1 |   2 |        0 |     0 |      0 |      0 |      0 |     0 |      0 |      0 |     0 |    1 |      1 |      0 |     0 |      0 |     0 |
| Project           | Projects Manager |         0 |   3 |        0 |     0 |      0 |      1 |      1 |     1 |      1 |      0 |     1 |    1 |      1 |      0 |     1 |      0 |     1 |
| Project           | Employee         |         0 |   4 |        0 |     0 |      0 |      0 |      0 |     1 |      1 |      0 |     1 |    0 |      1 |      1 |     1 |      0 |     0 |
| Project Template  | System Manager   |         0 |   1 |        0 |     0 |      0 |      1 |      1 |     1 |      1 |      0 |     1 |    1 |      1 |      0 |     1 |      0 |     1 |
| Project Type      | System Manager   |         0 |   1 |        0 |     0 |      0 |      1 |      1 |     1 |      1 |      0 |     1 |    1 |      1 |      0 |     1 |      0 |     1 |
| Project Type      | Projects Manager |         0 |   2 |        0 |     0 |      0 |      1 |      1 |     1 |      1 |      0 |     1 |    1 |      1 |      0 |     1 |      0 |     1 |
| Project Type      | Projects User    |         0 |   3 |        0 |     0 |      0 |      0 |      0 |     1 |      1 |      0 |     1 |    1 |      1 |      0 |     1 |      0 |     0 |
| Project Update    | Projects User    |         0 |   1 |        0 |     0 |      0 |      1 |      1 |     1 |      1 |      0 |     1 |    1 |      1 |      0 |     1 |      1 |     1 |
| Projects Settings | System Manager   |         0 |   1 |        0 |     0 |      0 |      1 |      1 |     1 |      0 |      0 |     1 |    1 |      0 |      0 |     1 |      0 |     1 |

| Job 2              |
|--------------------|
| Custom Permissions |

| parent            | role            | permlevel | idx | if_owner | amend | cancel | create | delete | email | export | import | print | read | report | select | share | submit | write |
|-------------------|-----------------|-----------|-----|----------|-------|--------|--------|--------|-------|--------|--------|-------|------|--------|--------|-------|--------|-------|
