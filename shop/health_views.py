from django.http import JsonResponse
from django.db import connection


def health_check(request):
    return JsonResponse({
        "status": "healthy",
        "service": "hvac_master"
    })


def readiness_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()

        return JsonResponse({
            "status": "ready",
            "database": "connected"
        })
    except Exception as e:
        return JsonResponse({
            "status": "not_ready",
            "error": str(e)
        }, status=503)


def liveness_check(request):
    return JsonResponse({
        "status": "alive"
    })
