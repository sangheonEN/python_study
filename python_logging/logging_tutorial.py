import logging
import traceback


def a():
    return 1/0


def b():
    a()


if __name__ == "__main__":
    level = logging.ERROR

    # Initialize the logging configuration with the specified level
    log_format = 'Test: %(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(level)  # Set the root logger's level

    # Create a file handler and set its level
    file_handler = logging.FileHandler('test.log')
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(log_format))

    # Create a console handler and set its level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter(log_format))

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    try:
        b()
    except Exception as e:
        print("오류가 발생했습니다.")
        tb_str = traceback.format_exc()
        # logging.error(f"b function call error: {e}\n")
        logging.error(f"Traceback: {tb_str}\n")
        logging.info("Attempting to call b function...\n")
