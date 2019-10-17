import logging

logging.basicConfig(level=logging.DEBUG)


def pay_developer(hours, user="Vasya"):
    logging.debug(f"We get {hours * 10} hours of work")

    if hours < 120:
        logging.warning(f"Too less {hours} hours for {user}")

    if not isinstance(hours, int):
        logging.error(f"Wrong type of hours {type(hours)}")
        return None

    result = hours * 50
    logging.info(f"We pay {result} money")
    return result


if __name__ == "__main__":
    pay_developer(100)
