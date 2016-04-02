from django.core.urlresolvers import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase

from .views import UKPostcodeValidateView
from .serializers import UKPostcodeSerializer

class PostcodeValidationURLTest(APITestCase):

    def test_url_name_reverses_to_url(self):
        url = reverse('validate_uk_postcode')
        self.assertEqual(url, '/uk_postcode/validate/')

    def test_url_resoloves_to_view(self):
        resolver = resolve('/uk_postcode/validate/')
        self.assertEqual(resolver.func.__name__, UKPostcodeValidateView.as_view().__name__)

class PostcodeValidationViewTest(APITestCase):

    def test_valid_postcode_returns_success(self):
        data = {'postcode': 'B33 8TH'}
        response = self.client.post(reverse('validate_uk_postcode'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_postcode_returns_error_code(self):
        data = {'postcode': 'incorrect postcode'}
        response = self.client.post(reverse('validate_uk_postcode'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_postcode_returns_error_message(self):
        data = {'postcode': 'incorrect postcode'}
        error_msg = {'postcode': ['Postcode is not a valid UK postcode']}
        response = self.client.post(reverse('validate_uk_postcode'), data)
        self.assertEqual(response.data, error_msg)

class UKPostcodeSerializerTest(APITestCase):

    def test_valid_uk_postcode(self):
        valid_postcodes = ['M1 1AA', 'M11AA', 'M60 1NW', 'M601NW',
                           'DN55 1PT', 'DN551PT', 'W1A 1HQ', 'W1A1HQ',
                           'EC1A 1BB', 'EC1A1BB', 'WC1N 2PL', 'WC1N2PL',
                           'SE5 8LG', 'SE58LG', 'BR3 5DE', 'BR35DE',
                           'SE8 4QH', 'SE84QH', 'YO31 5DE', 'YO315DE',
                           'W1G 8LZ', 'W1G8LZ', 'SW1A 0AA', 'SW1A0AA',
                           'W1G 9XT', 'W1G9XT', 'W1K 5DL', 'W1K5DL',
                           'N4 5RT', 'N45RT']

        for postcode in valid_postcodes:
            serializer = UKPostcodeSerializer(data={'postcode': postcode})
            self.assertTrue(serializer.is_valid())

    def test_invalid_uk_postcode(self):
        invalid_postcodes = [
            'W12A 3PT', 'W12A3PT', 'Q1 1AA', 'Q11AA', 'V12 1AA', 'V121AA', 'X11 1AA', 'X111AA',
            'WJ12 1AA', 'WJ121AA', 'WZ12 1AA', 'WZ121AA', 'ECI 1AA', 'ECI1AA', 'SANTA1', 'A99A9AA',
            'ECL 1AA', 'ECL1AA', 'ECM 1AA', 'ECM1AA', 'ECN 1AA', 'ECN1AA', 'ECM 1AA', 'ECM1AA',
            'ECO 1AA', 'ECO1AA', 'ECP 1AA', 'ECP1AA', 'ECQ 1AA', 'ECQ1AA', 'ECR 1AA', 'ECR1AA',
            'ECV 1AA', 'ECV1AA', 'ECX 1AA', 'ECX1AA', 'ECY 1AA', 'ECY1AA', 'ECZ 1AA', 'ECZ1AA',
            'EC1C 1AA', 'EC1C1AA', 'EC1D 1AA', 'EC1D1AA', 'EC1F 1AA', 'EC1F1AA', 'EC1G 1AA', 'EC1G1AA',
            'EC1I 1AA', 'EC1I1AA', 'EC1J 1AA', 'EC1J1AA', 'EC1K 1AA', 'EC1K1AA', 'EC1L 1AA', 'EC1L1AA',
            'EC1O 1AA', 'EC1O1AA', 'EC1S 1AA', 'EC1S1AA', 'EC1T 1AA', 'EC1T1AA', 'EC1U 1AA', 'EC1U1AA',
            'W1 XYZ', 'W1XYZ', 'W1 3CB', 'W13CB', 'W1 3IB', 'W13IB', 'W1 3KB', 'W13KB', 'W1 3MB', 'W13MB',
            'W1 3OB', 'W13OB', 'W1 3VB', 'W13VB', 'W1 3AC', 'W13AC', 'W1 3AI', 'W13AI', 'W1 3AK', 'W13AK',
            'W1 3AM', 'W13AM', 'W1 3AO', 'W13AO', 'W1 3AV', 'W13AV', 'W! 5DE', 'W!5DE', 'A99A 9AA',
            '1G 8LZ', '1G8LZ', 'SWAA 0AA', 'SWAA0AA', 'WW 3EG', 'WW3EG', '11 1AA', '111AA', 'SAN TA1',
            'EC1Z 1AA', 'EC1Z1AA'
        ]

        for postcode in invalid_postcodes:
            serializer = UKPostcodeSerializer(data={'postcode': postcode})
            self.assertFalse(serializer.is_valid())
