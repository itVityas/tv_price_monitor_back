from enum import Enum


class FilterOperators(str, Enum):
    EQ = "eq"                       # равно
    NE = "ne"                       # не равно
    GT = "gt"                       # больше
    GTE = "gte"                     # больше или равно
    LT = "lt"                       # меньше
    LTE = "lte"                     # меньше или равно
    CONTAINS = "contains"           # содержит (регистронезависимый)
    ICONTAINS = "icontains"         # содержит (регистронезависимый)
    STARTSWITH = "startswith"       # начинается с
    ENDSWITH = "endswith"           # заканчивается на
    IN = "in"                       # в списке
    NOT_IN = "not_in"               # не в списке
    IS_NULL = "is_null"             # is null
    IS_NOT_NULL = "is_not_null"     # is not null
