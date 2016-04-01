import re

from rest_framework import serializers


class UKPostcodeSerializer(serializers.Serializer):
    postcode = serializers.CharField(max_length=100, required=True)

    def validate_postcode(self, value):
        """
        Check that the postcode is valid UK postcode.
        """
        outcode_regex = '[A-PR-UWYZ]([0-9]{1,2}|([A-HIK-Y][0-9](|[0-9]|[ABEHMNPRVWXY]))|[0-9][A-HJKSTUW])'
        incode_regex = '[0-9][ABD-HJLNP-UW-Z]{2}'
        postcode_regex = re.compile(r'^(GIR 0AA|%s %s)$' % (outcode_regex, incode_regex))
        space_regex = re.compile(r' *(%s)$' % incode_regex)

        postcode = value.upper().strip()

        postcode = space_regex.sub(r' \1', postcode)
        if not postcode_regex.search(postcode):
            raise serializers.ValidationError("Postcode is not a valid UK postcode")
        return postcode
