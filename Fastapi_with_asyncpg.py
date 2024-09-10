import os
import datetime

import uvicorn
import asyncpg
from fastapi import FastAPI, HTTPException, status
import dotenv

dotenv.load_dotenv()


app = FastAPI(debug=True)

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
db = os.getenv("DB_NAME")


async def db_conn():
    return await asyncpg.connect(
        dsn=f"postgres://{user}:{password}@localhost:5432/{db}",
        command_timeout=60,
    )


@app.get("/user/{id_}")
async def get_user(id_: int):
    conn = await db_conn()
    result = await conn.fetchrow("SELECT * FROM users WHERE id=$1", id_)
    await conn.close()
    if result:
        print(result)
        return {"item_id": result.get("id"),
                "name": result[1],
                "date": result.get("dob")}
    else:
        raise HTTPException(status_code=404, detail="Item not found")


@app.post("/user/{name}", status_code=status.HTTP_201_CREATED)
async def add_user(name: str):
    conn = await db_conn()
    await conn.execute('''
            INSERT INTO users(name, dob) VALUES($1, $2)
        ''', name, datetime.date.today())
    await conn.close()

    return {"name": name}


if __name__ == "__main__":
    uvicorn.run(f"{__name__}:app", reload=True)