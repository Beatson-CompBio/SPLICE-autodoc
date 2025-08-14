import uuid

def main():
    return print(random_number())

def random_number() -> int:
    """
    This function generates a random UUID code.

    :param None:
    :return: uuid.
    :rtype: int
    """
    return uuid.uuid4()

if __name__ == "__main__":
    main()
