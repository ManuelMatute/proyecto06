import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

data_list = [
    {"id": str(uuid.uuid4()), "name": "User01", "email": "user01@example.com", "is_active": True},
    {"id": str(uuid.uuid4()), "name": "User02", "email": "user02@example.com", "is_active": True},
    {"id": str(uuid.uuid4()), "name": "User03", "email": "user03@example.com", "is_active": False},
]

def find_item(item_id: str):
    for item in data_list:
        if item["id"] == item_id:
            return item
    return None

class DemoRestApi(APIView):
    name = "Demo REST API"

    def get(self, request):
        return Response(data_list, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data

        if "name" not in data or "email" not in data:
            return Response(
                {"message": "Faltan campos obligatorios: name y email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        new_item = {
            "id": str(uuid.uuid4()),
            "name": data["name"],
            "email": data["email"],
            "is_active": True,
        }
        data_list.append(new_item)

        return Response(
            {"message": "Elemento creado exitosamente", "data": new_item},
            status=status.HTTP_201_CREATED,
        )

class DemoRestApiItem(APIView):
    def put(self, request, item_id):
        item = find_item(item_id)
        if not item:
            return Response({"message": "No existe el item"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if "name" not in data or "email" not in data:
            return Response(
                {"message": "Para PUT debes enviar name y email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        item["name"] = data["name"]
        item["email"] = data["email"]
        if "is_active" in data:
            item["is_active"] = bool(data["is_active"])

        return Response({"message": "Item reemplazado (PUT)", "data": item}, status=status.HTTP_200_OK)

    def patch(self, request, item_id):
        item = find_item(item_id)
        if not item:
            return Response({"message": "No existe el item"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if "name" in data:
            item["name"] = data["name"]
        if "email" in data:
            item["email"] = data["email"]
        if "is_active" in data:
            item["is_active"] = bool(data["is_active"])

        return Response({"message": "Item actualizado (PATCH)", "data": item}, status=status.HTTP_200_OK)

    def delete(self, request, item_id):
        item = find_item(item_id)
        if not item:
            return Response({"message": "No existe el item"}, status=status.HTTP_404_NOT_FOUND)

        item["is_active"] = False
        return Response({"message": "Item eliminado lógicamente (DELETE)", "data": item}, status=status.HTTP_200_OK)
