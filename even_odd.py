from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def even_odd(n:int):
    if n%2==0:
        return "Even"
    else:
        return "Odd"