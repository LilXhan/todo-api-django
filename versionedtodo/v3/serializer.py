from tasks.models import Todo 

from rest_framework.serializers import ModelSerializer

class TodoSerializer(ModelSerializer):
    class Meta:
        db_table = Todo
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'done_at', 'delete_at', )
