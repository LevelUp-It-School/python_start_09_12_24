from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Случайный совет API")

class Advice(BaseModel):
    text: str

advice_list = ["Пейте больше воды",
               "Делайте перерывы во время работы",
               "Не забывайте физическую активность",
               "Читайте каждый день",
               "Чистите зубы утром и перед сном",
               "Учитесь чему-то новому каждый день"]

@app.get("/advice", summary="Получить случайный совет")
def get_random_advice():
    return {"advice": random.choice(advice_list)}

@app.get('/', summary="Главная страница")
def read_root():
    return {"message":"Добро пожаловать в API случайных советов! Перейдите на /advice для получения совета"}

@app.post("/advice", summary='Добавить новый совет')
def add_advice(advice: Advice):
    if advice.text in advice_list:
        raise HTTPException(status_code=400, detail='Такой совет уже есть')
    advice_list.append(advice.text)
    return {'message': "Совет успешно добавлен"}

###
#Написать fastapi приложение
# / GET "Отправьте текст и я его повторю по ссылке /echo"
# /echo POST повторяет сообщение
