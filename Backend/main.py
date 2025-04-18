import uvicorn
from fastapi import FastAPI

from Backend.routes.CartItems import router as CartItemsRouter
from Backend.routes.Category import router as CategoryRouter
from Backend.routes.Orders import router as OrdersRouter
from Backend.routes.Products import router as ProductsRouter
from Backend.routes.User import router as UserRouter

app = FastAPI()

@app.get("/")
def welcome():
    return {"message": "Hello"}

app.include_router(UserRouter)
app.include_router(ProductsRouter)
app.include_router(CategoryRouter)
app.include_router(CartItemsRouter)
app.include_router(OrdersRouter)

if __name__ == "__main__":
    uvicorn.run(app=app, port=8080)
