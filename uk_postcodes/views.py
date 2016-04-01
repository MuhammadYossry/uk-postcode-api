from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UKPostcodeSerializer


class UKPostcodeValidateView(APIView):
    """
    View to validate UK postcodes.
    """

    def post(self, request, *args, **kwargs):
        """
        Validates if submitted postcode is a valid UK postcode
        and returns formatted postcode if valid
        ---
        parameters:
          - name: postcode
            description: The postcode that needed to be checked
            type: string

        responseMessages:
          - code: 400
            message: Not a valid UK postcode
        serializer: uk_postcodes.serializers.UKPostcodeSerializer
        """
        serializer = UKPostcodeSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
