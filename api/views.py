from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response

from core.utils.get_api_key import GetApiKey
from core.utils.get_api_data import GetRequestData

from drf_yasg.utils import swagger_auto_schema


class DataRequestView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(responses={200: 'Success', 500: 'Fail'})
    def get(self, request):
        keys, err = GetApiKey.get_api_key_n_check_error()
        if err:
            return Response({'detail': err}, status=500)

        result, err = GetRequestData.get_request_data_n_check_error(keys)
        if err:
            return Response({'detail': err}, status=500)

        return Response(result, status=200)
