from rest_framework import serializers
from .models import Assignment, AssignmentSubmission


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = '__all__'
        read_only_fields = ['created_by', 'created_at']


class SubmissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssignmentSubmission
        fields = '__all__'

        read_only_fields = [
            'intern',
            'status',
            'submitted_at'
        ]