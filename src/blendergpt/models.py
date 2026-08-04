from dataclasses import dataclass, field
from typing import Any
from enum import Enum

@dataclass
class Task:
    id: int
    name: str
    description: str
    tool: str
    parameters: dict[str, Any]
    dependencies: field(default_factory=True)
    status: TaskStatus
    priority: TaskPriority
    result: Any
    error: str


class TaskStatus(Enum):
    pending=1
    running=2
    completed=3
    


class TaskPriority(Enum):
    high=1
    medium=2
    low=3
