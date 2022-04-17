from django.urls import path
from produto import views as v

app_name = 'produto'

urlpatterns =[
    path('', v.produto_list, name='produto_list'),    
    path('<int:pk>/', v.produto_detail, name='produto_detail'),
    path('add/', v.ProdutoCreate.as_view(), name='produto_add'),
    path('update/<int:pk>/', v.ProdutoUpdate.as_view(), name='produto_update'),
    path('replace_number/', v.replace_number, name='replace_number'),
    path('<int:pk>/json/', v.produto_json, name='produto_json'),
]