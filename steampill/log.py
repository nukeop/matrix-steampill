import logging
import logging.handlers


def configure_logging(filename=None):
    """Configures the root logger.
    """
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(levelname)s] - %(asctime)s - %(name)s -"
                                  " %(message)s")

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    root.addHandler(console)

    if filename is not None:
        rfhandler = logging.handlers.RotatingFileHandler(
            filename,
            maxBytes=2 * 1024 * 1024,
            backupCount=3
        )
        rfhandler.setLevel(logging.DEBUG)
        rfhandler.setFormatter(formatter)
        root.addHandler(rfhandler)

    return root
