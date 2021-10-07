
class ListDivideException(Exception):
    pass


def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisible
    by divide.

    :param numbers:
    :param divide:
    :return:
    """
    if divide == 0:
        raise ListDivideException()

    results = [x for x in numbers if x % divide == 0]
    return len(results)
