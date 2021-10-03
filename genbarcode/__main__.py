import asyncio
import logging

handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter(
        style="{",
        fmt="[{name}:{filename}] {levelname} - {message}"
    )
)

log = logging.getLogger("genbarcode")
log.setLevel(logging.INFO)
log.addHandler(handler)


def main():
    return
