from fastapi import FastAPI
import uvicorn
from app.api.v1.endpoints.articles import router as articles_router
from app.api.v1.endpoints.users import router as users_router
from app.api.dependencies.database import Base,engine,SessionLocal
from app.api.models import article, user

app = FastAPI()


# Create all tables
article.Base.metadata.create_all(bind=engine)
user.Base.metadata.create_all(bind=engine)


# Routers
app.include_router(articles_router, prefix="/articles", tags=["articles"])
app.include_router(users_router, prefix="/users", tags=["users"])

@app.middleware("http")
async def db_session_middleware(request, call_next):
    request.state.db = SessionLocal()
    response = await call_next(request)
    request.state.db.close()
    return response




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

