from os import defpath
# from attr import fields
from rest_framework import serializers
from validator import Validator
from ..models import *


class PermissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class SessionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Session
        fields = '__all__'


class RequestsSerializer(serializers.ModelSerializer):
    # requester = serializers.StringRelatedField()

    class Meta:
        model = Request
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    #  staff = StaffSerializer(many=True, read_only=True)
    # StaffRoles = StaffSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = '__all__'


class ClassroomSerializer(serializers.ModelSerializer):
    # RequestClassroom = RequestsSerializer(many=True, read_only=True)

    class Meta:
        model = Classroom
        fields = "__all__"
        depth = 1

    # def validate(self, data):
    #     acceptedvalues = ['tp', 'td', 'amphi']
    #     if data['type'].lower not in acceptedvalues:
    #         raise serializers.ValidationError(
    #             "Invalid value for classroom type")


class ActivitytypeSerializer(serializers.ModelSerializer):
    # Req_ActivityType = RequestsSerializer(many=True, read_only=True)

    class Meta:
        model = Activity_type
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    # StaffSubjects = serializers.StringRelatedField(many=True)

    class Meta:
        model = Subject
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):

    # RequesterFromStaff = RequestsSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        # fields = "__all__"
        fields = ('id', 'uname', 'email', 'role',
                  'ppic', 'lastonline', 'Subjects')


class RequestsListingSerializer(serializers.ModelSerializer):
    # requester = serializers.StringRelatedField()
    requester = serializers.StringRelatedField()
    Classrooms = serializers.StringRelatedField()
    ReqActivityType = serializers.StringRelatedField()

    class Meta:
        model = Request
        fields = '__all__'


class StaffListingSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()
    Subjects = serializers.StringRelatedField(many=True)
    # RequesterFromStaff = RequestsSerializer(many=True, read_only=True)

    class Meta:
        model = Staff
        # fields = "__all__"
        fields = ('id', 'uname', 'email', 'role',
                  'ppic', 'lastonline', 'Subjects')
