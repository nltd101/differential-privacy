from condition.logic_gate_condition import LogicGateCondition
from condition.comparative_condition import ComparativeCondition
from errors import *
from condition.condition import Condition, comparative_condition, logic_gate_condition, List


def createCondition(conditions_str: str) -> Condition:
    """Create Condition by type and the list of the arguments

    Args:
        conditions_str (str): condition in the string format

    Raises:
        Exception: Invalid operator when a argument is unknown

    Returns:
        Condition: A condition was created
    """
    if conditions_str[0] != "{" or conditions_str[-1] != "}":
        raise QueryException(INVALID_SYNTAX)
    conditions_str = conditions_str[1:-1]
    type_condition, parameters_str = conditions_str.split(":", 1)
    if (type_condition in comparative_condition.keys()):
        return ComparativeCondition(comparative_condition[type_condition], parameters_str)
    elif (type_condition in logic_gate_condition.keys()):
        return LogicGateCondition(logic_gate_condition[type_condition], parameters_str)
    else:
        raise QueryException(INVALID_OPERATOR)
