import grpc
from concurrent import futures
import fibonacci_pb2
import fibonacci_pb2_grpc

class FibonacciSequence(fibonacci_pb2_grpc.FibonacciSequence):
    def Fibonacci(self, request, context):
        result = []
        a, b = 0, 1
        while a < request.number:
            result.append(a)
            a, b = b, a+b
        return fibonacci_pb2.FibonacciResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    fibonacci_pb2_grpc.add_FibonacciSequenceServicer_to_server(FibonacciSequence(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()