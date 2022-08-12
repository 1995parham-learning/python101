import thriftpy2
from thriftpy2.rpc import make_client

watraft_thrift = thriftpy2.load("WatRaft.thrift", module_name="watraft_thrift")

client = make_client(watraft_thrift.WatRaft, "127.0.0.1", 6000)
print(client.get("parham"))
