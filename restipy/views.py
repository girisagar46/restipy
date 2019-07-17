import logging
import os
import random
import time

from django.conf import settings as s
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class Environment(APIView):
    def get(self, request, *args, **kwargs):
        server = self.request.META.get('HTTP_HOST')
        client = self.request.META.get('REMOTE_ADDR')
        try:
            logging.info(f"/env {server} has been invoked from {client}")
            data = {
                "version": s.VERSION,
                "env": str(os.environ),
            }
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data, status=status.HTTP_200_OK)


class Endpoint0(APIView):

    def get(self, request, *args, **kwargs):
        server = self.request.META.get('HTTP_HOST')
        client = self.request.META.get('REMOTE_ADDR')
        try:
            logging.info(f"/env {server} has been invoked from {client}")
            data = {
                "version": s.VERSION,
                "host": server,
                "result": "Everything is well"
            }
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data, status=status.HTTP_200_OK)


class Health(APIView):
    def get(self, request, *args, **kwargs):
        server = self.request.META.get('HTTP_HOST')
        client = self.request.META.get('REMOTE_ADDR')
        try:
            logging.info(f"/env {server} has been invoked from {client}")
            data = {
                "healthy": True
            }
            if s.HEALTH_MAX > s.HEALTH_MIN >= 0:
                delay_response = random.randrange(float(s.HEALTH_MIN),
                                                  float(s.HEALTH_MAX))
                time.sleep(delay_response / 1000.0)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data, status=status.HTTP_200_OK)


class Info(APIView):
    def get(self, request, *args, **kwargs):
        server = self.request.META.get('HTTP_HOST')
        client = self.request.META.get('REMOTE_ADDR')
        try:
            logging.info(f"/env {server} has been invoked from {client}")
            data = {
                "version": s.VERSION,
                "host": server,
                "from": client
            }
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(data, status=status.HTTP_200_OK)
