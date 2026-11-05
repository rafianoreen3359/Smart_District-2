from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied

from .models import Assignment, AssignmentSubmission
from .serializers import (
    AssignmentSerializer,
    SubmissionSerializer
)


class AssignmentViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubmissionViewSet(viewsets.ModelViewSet):

    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        user = self.request.user

        if user.is_staff:
            return AssignmentSubmission.objects.all()

        return AssignmentSubmission.objects.filter(
            intern=user
        )

    def perform_create(self, serializer):

        if self.request.user.is_staff:
            raise PermissionDenied(
                "Admins cannot submit intern assignments."
            )

        serializer.save(intern=self.request.user)

    def perform_update(self, serializer):

        if not self.request.user.is_staff:
            raise PermissionDenied(
                "Only admins can update submissions."
            )

        serializer.save()