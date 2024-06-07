# -*- coding: utf-8 -*-
from rest_framework import serializers

class ScrapeTaskSerializer(serializers.Serializer):
    coin = serializers.CharField(max_length=10)
