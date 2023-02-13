from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class SimplePagination(PageNumberPagination):
    page_size = 50
    page_query_param = "page"
    max_page_size = 2000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'pages': (self.page.paginator.count // self.page_size) + 1,
            'results': data
        })