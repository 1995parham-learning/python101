import thriftpy2
from thriftpy2.rpc import make_server

watraft_thrift = thriftpy2.load("WatRaft.thrift", module_name="watraft_thrift")


class Dispatcher:
    def get(self, key: str):
        return f"Amusse you get the value of {key}"

    def put(self, key: str, val: str):
        return f"Ammuse {val} is put into {key}"

    def append_entries(
        self,
        term: int,
        leader_id: int,
        prev_log_index: int,
        prev_log_temr: int,
        entries: list,
        leader_commit_index: int,
    ):
        return "you take this shit seriously"


server = make_server(watraft_thrift.WatRaft, Dispatcher(), "127.0.0.1", 6000)
server.serve()
