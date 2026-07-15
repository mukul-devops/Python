
n : int = 5

name: str = "Harry"


def  sum(a: int, b: int) -> int:
    return a+b

from typing import List, Union, Tuple, Dict
number : List[int] = [1,2,4,5,3,4,23,34,22]
person: Tuple[str, int] = ("Alice", 30) 
scores: Dict[str, int] = {"Alice": 90, "Bob": 85} 
dentifier: Union[int, str] = "ID123" 
identifier = 12345  # Also valid 
