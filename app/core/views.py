# Framework imports.
from fastapi import FastAPI

# Prefix Import
from .. import API_PREFIX


# Import First Admin Registration Route
from .first_access import route as first_access_route

# Import Login Core
from .auth import route as auth_router

# Import Core Routes
from app.routes import route as core_router

# Import Project Info Routes
from app.modules.users.routes import route as user_router

# Import Provider Routes
from app.modules.providers.routes import route as provider_router

# Import Product Router
from app.modules.products.routes import route as product_router

# Import Product Router
from app.modules.transactions.routes import route as transaction_router


def create_routes(app: FastAPI) -> None:
    """
    Include routes.
    """
    # Include Core Router
    app.include_router(core_router, tags=['Core'], prefix=API_PREFIX)

    # Include First Admin User Registration Router
    app.include_router(first_access_route, tags=['First Access'], prefix=API_PREFIX)

    # Import Login Core
    app.include_router(auth_router, tags=['Authentication'], prefix=API_PREFIX)

    # Include Project Info Router
    app.include_router(user_router, tags=['Users'], prefix=API_PREFIX+'/admin')

    # Include Provider Router
    app.include_router(provider_router, tags=['Providers'], prefix=API_PREFIX)
    
    # Include Product Router
    app.include_router(product_router, tags=['Products'], prefix=API_PREFIX)
    
    # Include Transaction Router
    app.include_router(transaction_router, tags=['Transaction'], prefix=API_PREFIX)
