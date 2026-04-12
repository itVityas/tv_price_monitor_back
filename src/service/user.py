from abc import ABC, abstractmethod
from typing import Optional, List

from src.controllers.model.user import UserResponse


class UserService(ABC):
    @abstractmethod
    def get_users(self,
                  page: int = 1,
                  pagesize: int = 10,
                  filters: Optional[dict] = None) -> List[UserResponse]:
        pass
