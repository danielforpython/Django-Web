from django.urls import path

from books import views

urlpatterns = [
    path('shirley',views.shirley,name='Shirley'),
    path('',views.homepage,name='homepage'),
    path('base/',views.base,name='base'),
    path('book_list/',views.book_list,name='book_list'),
    path('person_list/',views.person_list,name='person_list'),
    path('q_duixiang/',views.q_duixiang,name='q_duixiang'),
    path('f_duixiang/',views.f_duixiang,name='f_duixiang'),
    path('query_mutitable/',views.query_mutitable,name='query_mutitable'),
    path('raw_sql/',views.raw_sql,name='raw_sql'),
    path('raw_sql_m_m/',views.raw_sql_m_m,name='raw_sql_m_m'),
    path('self_table/',views.self_table,name='self_table'),
    path('cud_c/',views.cud_c,name='cud_c'),
    path('cud_u/',views.cud_u,name='cud_u'),
    path('area_list/',views.area_list,name='area_list'),
    path('view_request/',views.view_request,name='view_request'),
    path('RegisterForms/',views.IndexForms.as_view(),name='RegisterForms'),
    path('login/',views.login,name='login'),
    path('cookie/',views.cookie,name='cookie'),
    path('session/',views.sessionrequest,name='session'),
    path('Glowing/',views.glowing,name='Glowing'),
    path('Responsive/',views.responsive,name='Responsive'),
    path('gallery/',views.galley,name='gallery'),
]
