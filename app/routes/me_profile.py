
from fastapi import HTTPException, Request
import app


@app.get('/me')
async def read_my_profile(request: Request):
    user_data = request.state.user
    if user_data is None:
        raise HTTPException(status_code=401,detail='Unauthorized')
    return {'message': f'Welcome, user {user_data['sub']}'}