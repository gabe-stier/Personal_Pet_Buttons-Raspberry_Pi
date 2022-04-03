import asyncio
from typing import Union

class Reader(asyncio.Protocol):
    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.transport = transport
        self.buf = bytes()
        self.msgs_recvd = 0
        print("Reader connection created")

    def connection_lost(self, exc: Union[Exception, None]) -> None:
        print("Reader closed")

    def data_received(self, data: bytes) -> None:
        self.buf += data
        if b'\n'in self.buf:
            lines = self.buf.split(b'\n')
            self.buf = lines[-1]
            for line in lines[:-1]:
                print(line.decode())
                self.msgs_recvd += 1
                
