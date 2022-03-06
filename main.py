from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()

#serializer
class Item(BaseModel):
    id:int
    car_model:str
    trim_level:str
    color:str
    price:int
    reserved:bool

    class Config:
        orm_mode=True

db=SessionLocal()

#View All Items
@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

#Search By ID
@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

#Search By Color
@app.get('/item/{item_color}',response_model=Item,status_code=status.HTTP_200_OK)
def get_item_color(item_color:str):
    item=db.query(models.Item).filter(models.Item.color==item_color).all()
    return item

@app.get("Pick a color")
def read_item(Color2: str, Available: Optional[str] = None):
    return {"Color": Color2, "Available": Available}


#Search By Model
@app.get('/item/{item_model}',response_model=Item,status_code=status.HTTP_200_OK)
def get_item_model(item_model:str):
    item=db.query(models.Item).filter(models.Item.car_model==item_model).all()
    return item




#Creat An Item
@app.post('/items',response_model=Item,status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(models.Item).filter(models.Item.id==item.id).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")

    new_item=models.Item(
        car_model=item.car_model,
        price=item.price,
        trim_level=item.trim_level,
        color=item.color,
        reserved=item.reserved
    )

    db.add(new_item)
    db.commit()

    return new_item

#Update Item
@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.car_model=item.car_model
    item_to_update.price=item.price
    item_to_update.trim_level=item.trim_level
    item_to_update.reserved=item.reserved
    item_to_update.color=item.color

    db.commit()

    return item_to_update
    
#Delete Item
@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Resource Not Found")

    db.delete(item_to_delete)
    db.commit

    return item_to_delete
