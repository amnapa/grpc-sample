import grpc
import fibonacci_pb2
import fibonacci_pb2_grpc

def run(number):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = fibonacci_pb2_grpc.FibonacciSequenceStub(channel)
        response = stub.Fibonacci(fibonacci_pb2.FibonacciRequest(number = number))
    print(f"Result: {response.result}")

if __name__ == '__main__':
    # Get user Input 
    number = int(input("Please input a number to calculate the fibonacci sequence: "))
    run(number)