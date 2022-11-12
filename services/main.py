import uvicorn
from fastapi import FastAPI
import api_data
from Models.Character_Model import CharacterModel as model


app = FastAPI()

@app.get("/")
def index():
    return{
        "message" : "Hello World"
    }

@app.get(f"/character/{id}",response_model=model)
async def character_getter(id:int):
    character = await api_data.get_characterById(id)
    return character.dict()


if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=80)