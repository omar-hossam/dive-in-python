import logging

def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    logging.info("🚀 App started!")
    logging.warning("something went wrong!")
    logging.error("Oh no! it broke!")
    
if __name__ == '__main__':
    main()
