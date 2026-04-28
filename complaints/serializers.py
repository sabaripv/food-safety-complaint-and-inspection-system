# from rest_framework import serializers
# from .models import Complaint

# class ComplaintSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Complaint
#         fields = ["id", "title", "description", "status", "created_at", "image"]
#         read_only_fields = ["id", "status", "created_at"]

# from rest_framework import serializers
# from .models import Complaint
# from inspections.serializers import InspectionSerializer  # 👈 add this

# class ComplaintSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(read_only=True)  # 👈 shows username
#     inspections = InspectionSerializer(many=True, read_only=True)  # 👈 nested inspections

#     class Meta:
#         model = Complaint
#         fields = [
#             "id",
#             "title",
#             "description",
#             "status",
#             "created_at",
#             "image",
#             "user",          # 👈 add this
#             "inspections",   # 👈 add this
#         ]
#         read_only_fields = ["id", "status", "created_at"]



from rest_framework import serializers
from .models import Complaint

class ComplaintSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Complaint
        fields = [
            "id",
            "title",
            "description",
            "status",
            "created_at",
            "image",
            "user",
        ]