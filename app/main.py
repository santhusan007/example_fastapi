
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from .import models
from .routers import post ,users ,auth,votes
from .config import settings


#models.Base.metadata.create_all(bind=engine)
app=FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
        )

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get("/")

def root():
    return {"message": "Welcome to my API"}





'''
my_posts=[{"title":"title of post1","content":"content of post 1","id":1},
            {"title":"title of post2","content":"content of post 2","id":2}]
            
            

# Testing program

@app.get("/sqlalchemy")
def test_post(db: Session = Depends(get_db)):
    post=db.query(models.Post).all()
    return {"data":post}

#functions made before connecting to database

def find_post(id):
    for p in my_posts:
        if p['id']==id:
            return p
        

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i



            
            '''



