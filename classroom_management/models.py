from django.db import models
from django.forms import BooleanField, CharField, IntegerField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# for choices field still in development
ClassroomType = (
    ("TP", "TP"),
    ("TD", "TD"),
    ("Amphi", "Amphi"),
    ("Other", "Other")
)

RequestStatus = (
    ("Approved", "Approved"),
    ("On Waiting", "On Waiting"),
    ("Desapproved", "Desapproved")
)


class Activity_type(models.Model):
    activity_type_name = models.CharField(max_length=30)

    def __str__(self):
        return self.activity_type_name


class Permission(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Classroom(models.Model):
    cycle = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(2)])
    classroom_name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=10,
        choices=ClassroomType,
        default='Other'
    )
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.classroom_name + " | " + self.type


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    roleName = models.CharField(max_length=30)
    ActivityTypes = models.ManyToManyField(
        Activity_type, related_name="ActivityType", blank=True)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.roleName


class Staff(models.Model):
    uname = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="StaffRoles")
    ppic = models.CharField(max_length=100, blank=True)
    lastonline = models.DateTimeField()
    Subjects = models.ManyToManyField(
        Subject, blank=True, default=None, related_name="StaffSubjects")

    def __str__(self):
        return self.uname + " | " + self.role.Rolename


class Request(models.Model):
    requester = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="RequesterFromStaff")
    is_approved = models.CharField(
        max_length=16,
        choices=RequestStatus,
        default='On Waiting'
    )
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    # frequency = models.CharField(max_length=5)
    is_finished = models.BooleanField()
    group = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=100)
    # repetition = models.IntegerField()
    request_time = models.DateField(auto_now_add=True)
    Classrooms = models.ForeignKey(
        Classroom, default=None, on_delete=models.CASCADE, related_name="RequestClassroom")
    ReqActivityType = models.ForeignKey(
        Activity_type, default=None, on_delete=models.CASCADE, related_name="Req_ActivityType")

    def __str__(self):
        return self.requester.uname + " | " + str(self.group) + " | " + str(self.Classrooms) + " |"


class Session(models.Model):
    SessionSubject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="SessionSubjects")
    session_type = models.CharField(max_length=100)
    SessionLead = models.ForeignKey(
        Staff,  on_delete=models.CASCADE, related_name="Staffs"
    )
    classroom_id = models.ForeignKey(
        Classroom,  on_delete=models.CASCADE, related_name="SessionClassrooms"
    )
    period_start = models.DateTimeField()
    period_end = models.TimeField()
    ActivityType = models.ForeignKey(
        Activity_type, on_delete=models.CASCADE, related_name="SessionActivityTypes"
    )
    group = models.IntegerField()
