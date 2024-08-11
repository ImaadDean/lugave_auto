from fastapi import FastAPI
from routes.car_routes import router as car_router
from routes.user_routes import router as user_router
from routes.sale_routes import router as sale_router
from routes.payment_routes import router as payment_router
from routes.payment_schedule_routes import router as payment_schedule_router
from routes.customer_routes import router as customer_router
from routes.expense_routes import router as expense_router
from routes.auth_routes import router as auth_router
app = FastAPI()

app.include_router(car_router, prefix="/cars")
app.include_router(user_router, prefix="/users")
app.include_router(sale_router, prefix="/sales")
app.include_router(payment_router, prefix="/payments")
app.include_router(payment_schedule_router, prefix="/payment_schedules")
app.include_router(customer_router, prefix="/customers")
app.include_router(expense_router, prefix="/expenses")
app.include_router(auth_router, prefix="/auth" )
