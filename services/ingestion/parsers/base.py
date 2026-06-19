from abc import ABC, abstractmethod
from pathlib import Path


class BaseParser(ABC):

    @abstractmethod
    async def parse(
        self,
        file_path: Path,
    ) -> str:
        raise NotImplementedError