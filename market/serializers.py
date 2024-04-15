from django.core.serializers.json import Serializer as JSONSerializer


class CustomBookSerializer(JSONSerializer):
    def get_dump_object(self, obj):
        data = self._current or {}
        data.update({'name': obj.name, 'category': obj.category, 'page_count': obj.page_count, 'price': obj.price})
        if hasattr(obj, 'author'):
            data['author'] = f"{obj.author.first_name} {obj.author.last_name}"
        return data
