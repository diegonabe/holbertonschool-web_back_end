#!/usr/bin/env python3
""" Tasks de paginación"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ Devuelve el inicio y el final de index
     correspondiendo al rango de de index's """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
