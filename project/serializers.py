from rest_framework import serializers

from .models import Project, ProjectCategory, ProjectPicture


class ProjectPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPicture
        fields = ('name', 'image', 'project')


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectPictureSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('name','target_area', 'theme_description', 'goals',
                  'specific_goals', 'activities', 'results', 'schedule',
                  'target_audience', 'project_totals', 'taxes',
                  'community_tour', 'future_vision', 'category', 'images')


class ProjectCategorySerializer(serializers.ModelSerializer):
    project_categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='project-detail')

    class Meta:
        model = ProjectCategory
        fields = ('name', 'project_categories')

