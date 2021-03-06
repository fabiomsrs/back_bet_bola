from core.paginations import PageNumberPagination
from rest_framework.response import Response
from decimal import Decimal
from user.models import CustomUser as User

class EntryPagination(PageNumberPagination):
    page_size = 30

    def get_paginated_response(self, data):        
        entry = 0
        out = 0        
        total = 0
        if self.request.user.user_type == 3:
            users = [{"id":user.pk,"username":user.username} for user in self.request.user.manager.manager_assoc.all()]
        else:
            users = [{"id":user.pk,"username":user.username} for user in User.objects.filter(user_type__in=[2], is_active=True, my_store=self.request.user.my_store)] 

        for release in data:            
            if float(release['value']) > 0:
                entry += float(release['value'])                
            else:
                out += float(release['value'])
            total += float(release['value'])  

        page = int(self.request.GET.get('page',1)) 

        if page == 1:
            data = data[0:self.page_size]
        data = data[self.page_size * (page - 1) : (page * self.page_size)] 

        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,            
            'entry': entry,
            'out': out,            
            'total': total,
            'users': users,
            'results': data
        })
