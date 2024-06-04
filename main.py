from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
import uvicorn
from starlette.middleware.cors import *
from typing import Dict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Foco(BaseModel):
    latitude: float
    longitude: float
    nome: str


focos: Dict[int, Foco] = {
1: {"latitude": 23.75, "longitude": 46.47, "nome": "foco1"},
2: {"latitude": 23.96, "longitude": 47.08, "nome": "foco2"},
3: {"latitude": 23.18, "longitude": 46.66, "nome": "foco3"},
4: {"latitude": 23.12, "longitude": 46.81, "nome": "foco4"},
5: {"latitude": 23.70, "longitude": 46.48, "nome": "foco5"},
6: {"latitude": 23.91, "longitude": 47.00, "nome": "foco6"},
7: {"latitude": 23.84, "longitude": 46.95, "nome": "foco7"},
8: {"latitude": 23.13, "longitude": 46.44, "nome": "foco8"},
9: {"latitude": 23.09, "longitude": 46.32, "nome": "foco9"},
10: {"latitude": 23.44, "longitude": 46.82, "nome": "foco10"},
11: {"latitude": 23.16, "longitude": 47.03, "nome": "foco11"},
12: {"latitude": 23.87, "longitude": 47.12, "nome": "foco12"},
13: {"latitude": 23.44, "longitude": 47.01, "nome": "foco13"},
14: {"latitude": 23.05, "longitude": 46.79, "nome": "foco14"},
15: {"latitude": 23.04, "longitude": 46.83, "nome": "foco15"},
16: {"latitude": 23.71, "longitude": 46.48, "nome": "foco16"},
17: {"latitude": 23.43, "longitude": 46.45, "nome": "foco17"},
18: {"latitude": 23.80, "longitude": 46.27, "nome": "foco18"},
19: {"latitude": 23.61, "longitude": 46.57, "nome": "foco19"},
20: {"latitude": 23.69, "longitude": 46.82, "nome": "foco20"},
21: {"latitude": 23.08, "longitude": 47.18, "nome": "foco21"},
22: {"latitude": 23.40, "longitude": 46.88, "nome": "foco22"},
23: {"latitude": 23.34, "longitude": 46.57, "nome": "foco23"},
24: {"latitude": 23.76, "longitude": 46.25, "nome": "foco24"},
25: {"latitude": 23.43, "longitude": 46.89, "nome": "foco25"},
}



@app.get("/focos/{latitude}/{longitude}")
def listar_focos_proximos(latitude : float, longitude: float):
    focos_entram = []
    for foco in focos.values():
        print(foco)
        latitudes_retornada = abs(latitude - foco["latitude"])
        longitude_retornada = abs(longitude - foco["longitude"])
        if latitudes_retornada + longitude_retornada <= 0.5:
            focos_entram.append(foco)
    return focos_entram

@app.post("/criar_foco/{latitude}/{longitude}/{nome}")
def adicionar_foco(latitude: float, longitude: float, nome: str):
    novo_id = max(focos.keys()) + 1
    novo_foco = Foco(latitude=latitude, longitude=longitude, nome=nome)
    focos[novo_id] = novo_foco.model_dump()
    return novo_foco


if __name__ == "__main__":
    uvicorn.run(app, port=8080)
    
    '''
    if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
    '''