from utilities import custom_logger, parser


def main_algorithm():
    custom_logger.start_logger()

    parser.parse()

if __name__ == "__main__":
    main_algorithm()