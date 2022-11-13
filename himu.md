# AssetType
```json
{
    "id" : Int,
    "name" : String, //Laptop, Phone, Etc
    "service_tag" : String, //Serial Number or Sim Number, etc
    "active" : Boolean, //Availablilty
    "model" : String //POCO F3
}
```

# AssetReturnCondition Object
```json
{
    "id" : Int,
    "condition" : String //Good, Bad, Nosto, Halka Nosto etc
}
```

# Employee Object

```json
{
    "id" : Int,
    "name" : String,
    "email" : String,
    "phone" : String
    //Add other required fields
}
```

# AssetTracks Object
```json
{
    "id": Int,
    "asset" : AssetObject, //Link to specific asset object
    "taken_by": EmployeeObject, //Link to specific employee object who got the asset/device
    "take_out_time": DateTimeField,
    "returned_time" : DateTimeField,
    "returned_condition": AssetReturnCondition, //Link to return condition object
    "has_defined_time": Boolean //If a asset check out and return time pushed initially, this should be `true`.
}
```

# Inventory Object
```json
{
    "id" : Int,
    "asset_type" : AssetType, //Link to sepcific asset type object
    "currently_in_stock" : Int, //Define the quantity of this asset available in the inventory
    "left_for_check_out" : Int //It should be updated when there is a new log to the `AssetTracks` object. For both checkout and return
}
```
