import asyncio
from typing import Union

class Writer(asyncio.Protocol):
    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.transport = transport
        asyncio.ensure_future(self.send())
        print("Reader connection created")

    def connection_lost(self, exc: Union[Exception, None]) -> None:
        print("Writer closed")

    async def send(self):
        """Send four newline-terminated messages, one byte at a time.
        """
        message = b'foo\nbar\nbaz\nqux\n'
        for b in message:
            await asyncio.sleep(0.5)
            self.transport.serial.write(bytes([b]))
            print(f'Writer sent: {bytes([b])}')
        self.transport.close()