import pprint
import inspect
import logging
import functools

logging.basicConfig(level=logging.DEBUG)


def debug(function):
    """
    debug decorator print function information and parameters.
    """

    @functools.wraps(function)
    def _debug(*args, **kwargs):
        result = None
        try:
            result = function(*args, **kwargs)
        finally:
            # extract the signarture from the function
            signature = inspect.signature(function)
            # fill the arguments
            arguments = signature.bind(*args, **kwargs)
            arguments.apply_defaults()

            logging.debug(
                "%s(%s): %s"
                % (
                    function.__qualname__,
                    ", ".join(
                        "%s=%r" % (k, v)
                        for k, v in arguments.arguments.items()
                    ),
                    pprint.pformat(result) if result is not None else "",
                )
            )

    return _debug


@debug
def spam(a, b=123):
    return "this message is a spam"


spam(1)
spam(1, 456)
spam(b=1, a=456)
