# Mongodb commands


## Insert a document into a collection

The collection could not exist, but if it does not exist, MongoDB will create it.

```bash
db.people.insertOne({"name":"Jhon",age:33});
```

## Finf all documents in a collection

```bash
db.people.find()
```

## Find documents with a filter

```bash
db.people.find({"name":"Jhon"})
```
## Delete a document

```bash
find_one_and_delete
```
