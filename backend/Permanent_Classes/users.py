from typing import Any, Optional
from pydantic import BaseModel
from ..DAO.DAOObjects import *

class User(BaseModel):
    name : str
    email: str
    phone_num : int
    password: str
    gender: str
    photo: Optional[str]
    
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
    def register(self):
        pass

class Admin(User):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        return DAOAdmin().save(self)
        
class Learner(User):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        return DAOLearner().save(self)
        
class Expert(Learner):
    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
    
    def register(self):
        return DAOExpert().save(self)

