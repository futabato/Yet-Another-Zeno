# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import federated_pb2 as federated__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in federated_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class FederatedLearningStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendLocalUpdate = channel.unary_unary(
                '/FederatedLearning/SendLocalUpdate',
                request_serializer=federated__pb2.LocalUpdate.SerializeToString,
                response_deserializer=federated__pb2.ServerResponse.FromString,
                _registered_method=True)
        self.GetGlobalModel = channel.unary_unary(
                '/FederatedLearning/GetGlobalModel',
                request_serializer=federated__pb2.Empty.SerializeToString,
                response_deserializer=federated__pb2.GlobalModel.FromString,
                _registered_method=True)


class FederatedLearningServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendLocalUpdate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetGlobalModel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FederatedLearningServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendLocalUpdate': grpc.unary_unary_rpc_method_handler(
                    servicer.SendLocalUpdate,
                    request_deserializer=federated__pb2.LocalUpdate.FromString,
                    response_serializer=federated__pb2.ServerResponse.SerializeToString,
            ),
            'GetGlobalModel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGlobalModel,
                    request_deserializer=federated__pb2.Empty.FromString,
                    response_serializer=federated__pb2.GlobalModel.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'FederatedLearning', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('FederatedLearning', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FederatedLearning(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendLocalUpdate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/FederatedLearning/SendLocalUpdate',
            federated__pb2.LocalUpdate.SerializeToString,
            federated__pb2.ServerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetGlobalModel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/FederatedLearning/GetGlobalModel',
            federated__pb2.Empty.SerializeToString,
            federated__pb2.GlobalModel.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
