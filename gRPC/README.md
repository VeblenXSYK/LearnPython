## Python gRPC 入门

#### 1、gRPC是什么？

	定义一个服务，指定其能够被远程调用的方法（包含参数和返回类型）。在服务端实现这个接口，并运行一个 gRPC 服务器来处理客户端调用。在客户端应用可以像调用本地对象一样直接调用另一台不同的机器上服务端的方法，使得我们能够更容易地创建分布式应用和服务。
	
	gRPC 默认使用 *protocol buffers*，这是 Google 开源的一种轻便高效的结构化数据存储格式，可以用于结构化数据串行化，或者说序列化。它很适合做数据存储或 RPC 数据交换格式。

![163db03c6fb2e200](.\image\163db03c6fb2e200.jpg)

#### 2、grpc安装

```
pip install grpcio				# 安装 gRPC
pip install grpcio-tools		# 安装 gRPC tools(包含 protocol buffer 编译器和用于从 .proto 文件生成服务端和客户端代码的插件)
```

#### 3、gRPC 示例

- 编译
```
python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. hello.proto

生成了两个文件：
	hello_pb2.py 此文件包含生成的request(HelloRequest)和response(HelloReply)的类。
	hello_pb2_grpc.py 此文件包含生成的客户端(GreeterStub)和服务端(GreeterServicer)的类。
```

- 创建服务端代码
```
见greeter_server.py
```
- 创建客户端代码

```
见greeter_client.py
```

- 运行
```
首先运行服务端代码:
	python greeter_server.py
然后运行客户端代码:
	python greeter_client.py
```