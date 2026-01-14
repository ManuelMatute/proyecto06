from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from datetime import datetime

def format_timestamp_es(dt: datetime) -> str:
    s = dt.strftime("%d/%m/%Y, %I:%M:%S %p")
    return s.replace("AM", "a. m.").replace("PM", "p. m.")

class LandingAPI(APIView):
    name = "Landing API"
    collection_name = "leads"

    def get(self, request):
        ref = db.reference(self.collection_name)
        data = ref.get()

        if not data:
            return Response([], status=status.HTTP_200_OK)

        result = []
        for key, value in data.items():
            item = value
            item["id"] = key
            result.append(item)

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        payload = request.data

        if "name" not in payload or "email" not in payload:
            return Response(
                {"message": "Faltan campos obligatorios: name y email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        payload["timestamp"] = format_timestamp_es(datetime.now())

        ref = db.reference(self.collection_name)
        new_ref = ref.push(payload)

        return Response(
            {"message": "Creado", "id": new_ref.key},
            status=status.HTTP_201_CREATED,
        )
