from steampill import app
from steampill import log
from steampill import version


if __name__ == '__main__':
    logger = log.configure_logging('steampill.log')
    logger.info("Starting matrix-steampill version {}.{}.{}".format(
        *version.VERSION
    ))

    app.run()
