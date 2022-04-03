import asyncio
from typing import Union


class Reader(asyncio.Protocol):

    def __init__(self, *args, **kargs) -> None:
        self.message = None
        self.task = None
        super().__init__(*args, **kargs)

    def connection_made(self, transport: asyncio.transports.BaseTransport) -> None:
        self.transport = transport
        self.buf = bytes()
        self.msgs_recvd = 0
        print("Reader connection created")

    def connection_lost(self, exc: Union[Exception, None]) -> None:
        print("Reader closed")

    def set_message(self, message):
        self.message = message

    def set_task(self, task):
        self.task = task

    def data_received(self, data: bytes) -> None:
        if self.message == None:
            self.transport.close()
            raise Exception("Message was not set")
        if self.task == None:
            self.transport.close()
            raise Exception("Task was not set")

        self.buf += data
        if b'\n' in self.buf:
            lines = self.buf.split(b'\n')
            self.buf = lines[-1]
            for line in lines[:-1]:
                if line.decode() == self.message:
                    task_success = self.task
                    if not task_success:
                        pass
                print(line.decode())
                self.msgs_recvd += 1
