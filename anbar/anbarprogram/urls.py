from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required,user_passes_test

def is_superuser(user):
    return user.is_superuser

def is_staff(user):
    return user.is_staff

urlpatterns = [
    path('menu',user_passes_test(is_superuser, login_url='menu')(login_required(views.menu)),name='menu'),
    path('brands/', login_required(views.brands), name='brands'),
    path('brands/<int:check>/<int:user_id>/', login_required(views.brands), name='brands'),
    path('delete/<int:id>/', login_required(views.delete), name='delete'),
    path('delete/<int:check>/<int:id>/', login_required(views.delete), name='delete'),
    path('udalit/<int:id>/', login_required(views.udalit), name='udalit'),
    path('udalit/<int:check>/<int:id>/', login_required(views.udalit), name='udalit'),
    path('edit/<int:id>/', login_required(views.edit), name='edit'),
    path('edit/<int:check>/<int:id>', login_required(views.edit), name='edit'),
    path('update/<int:id>/', login_required(views.update), name='update'),
    path('update/<int:check>/<int:id>/', login_required(views.update), name='update'),

    path('clients/', login_required(views.clients), name='clients'),
    path('clients/<int:check>/<int:user_id>/', login_required(views.clients), name='clients'),
    path('delete1/<int:id>/', login_required(views.delete1), name='delete1'),
    path('delete1/<int:check>/<int:id>/', login_required(views.delete1), name='delete1'),
    path('udalit1/<int:id>/', login_required(views.udalit1), name='udalit1'),
    path('udalit1/<int:check>/<int:id>/', login_required(views.udalit1), name='udalit1'),
    path('edit1/<int:id>/', login_required(views.edit1), name='edit1'),
    path('edit1/<int:check>/<int:id>', login_required(views.edit1), name='edit1'),
    path('update1/<int:id>/', login_required(views.update1), name='update1'),
    path('update1/<int:check>/<int:id>/', login_required(views.update1), name='update1'),


    path('departments/', login_required(views.departments), name='departments'),
    path('departments/<int:check>/<int:user_id>/', login_required(views.departments), name='departments'),
    path('delete2/<int:id>/', login_required(views.delete2), name='delete2'),
    path('delete2/<int:check>/<int:id>/', login_required(views.delete2), name='delete2'),
    path('udalit2/<int:id>/', login_required(views.udalit2), name='udalit2'),
    path('udalit2/<int:check>/<int:id>/', login_required(views.udalit2), name='udalit2'),
    path('edit2/<int:id>/', login_required(views.edit2), name='edit2'),
    path('edit2/<int:check>/<int:id>/', login_required(views.edit2), name='edit2'),
    path('update2/<int:id>/', login_required(views.update2), name='update2'),
    path('update2/<int:check>/<int:id>/', login_required(views.update2), name='update2'),

    path('expense/', login_required(views.expense), name='expense'),
    path('expense/<int:check>/<int:user_id>/', login_required(views.expense), name='expense'),
    path('delete3/<int:id>/', login_required(views.delete3), name='delete3'),
    path('delete3/<int:check>/<int:id>/', login_required(views.delete3), name='delete3'),
    path('udalit3/<int:id>/', login_required(views.udalit3), name='udalit3'),
    path('udalit3/<int:check>/<int:id>/', login_required(views.udalit3), name='udalit3'),
    path('edit3/<int:id>/', login_required(views.edit3), name='edit3'),
    path('edit3/<int:check>/<int:id>/', login_required(views.edit3), name='edit3'),
    path('update3/<int:id>/', login_required(views.update3), name='update3'),
    path('update3/<int:check>/<int:id>/', login_required(views.update3), name='update3'),

    path('permissions',login_required(views.permissions),name='permissions'),

    path('orders/', login_required(views.orders), name='orders'),
    path('orders/<int:check>/<int:user_id>/', login_required(views.orders), name='orders'),
    path('delete4/<int:id>/', login_required(views.delete4), name='delete4'),
    path('delete4/<int:check>/<int:id>/', login_required(views.delete4), name='delete4'),
    path('udalit4/<int:id>/', login_required(views.udalit4), name='udalit4'),
    path('udalit4/<int:check>/<int:id>/', login_required(views.udalit4), name='udalit4'),
    path('edit4/<int:id>/', login_required(views.edit4), name='edit4'),
    path('edit4/<int:check>/<int:id>/', login_required(views.edit4), name='edit4'),
    path('update4/<int:id>/', login_required(views.update4), name='update4'),
    path('update4/<int:check>/<int:id>/', login_required(views.update4), name='update4'),


    path('planner/', login_required(views.planner), name='planner'),
    path('planner/<int:check>/<int:user_id>/', login_required(views.planner), name='planner'),
    path('delete5/<int:id>/', login_required(views.delete5), name='delete5'),
    path('delete5/<int:check>/<int:id>/', login_required(views.delete5), name='delete5'),
    path('udalit5/<int:id>/', login_required(views.udalit5), name='udalit5'),
    path('udalit5/<int:check>/<int:id>/', login_required(views.udalit5), name='udalit5'),
    path('edit5/<int:id>/', login_required(views.edit5), name='edit5'),
    path('edit5/<int:check>/<int:id>/', login_required(views.edit5), name='edit5'),
    path('update5/<int:id>/', login_required(views.update5), name='update5'),
    path('update5/<int:check>/<int:id>/', login_required(views.update5), name='update5'),


    path('positions/', login_required(views.positions), name='positions'),
    path('positions/<int:check>/<int:user_id>/', login_required(views.positions), name='positions'),
    path('delete6/<int:id>/', login_required(views.delete6), name='delete6'),
    path('delete6/<int:check>/<int:id>/', login_required(views.delete6), name='delete6'),
    path('udalit6/<int:id>/', login_required(views.udalit6), name='udalit6'),
    path('udalit6/<int:check>/<int:id>/', login_required(views.udalit6), name='udalit6'),
    path('edit6/<int:id>/', login_required(views.edit6), name='edit6'),
    path('edit6/<int:check>/<int:id>/', login_required(views.edit6), name='edit6'),
    path('update6/<int:id>/', login_required(views.update6), name='update6'),
    path('update6/<int:check>/<int:id>/', login_required(views.update6), name='update6'),

    path('products/', login_required(views.products), name='products'),
    path('products/<int:check>/<int:user_id>/', login_required(views.products), name='products'),
    path('delete7/<int:id>/', login_required(views.delete7), name='delete7'),
    path('delete7/<int:check>/<int:id>/', login_required(views.delete7), name='delete7'),
    path('udalit7/<int:id>/', login_required(views.udalit7), name='udalit7'),
    path('udalit7/<int:check>/<int:id>/', login_required(views.udalit7), name='udalit7'),
    path('edit7/<int:id>/', login_required(views.edit7), name='edit7'),
    path('edit7/<int:check>/<int:id>/', login_required(views.edit7), name='edit7'),
    path('update7/<int:id>/', login_required(views.update7), name='update7'),
    path('update7/<int:check>/<int:id>/', login_required(views.update7), name='update7'),

    path('staff/', login_required(views.staff), name='staff'),
    path('staff/<int:check>/<int:user_id>/', login_required(views.staff), name='staff'),
    path('delete8/<int:id>/', login_required(views.delete8), name='delete8'),
    path('delete8/<int:check>/<int:id>/', login_required(views.delete8), name='delete8'),
    path('udalit8/<int:id>/', login_required(views.udalit8), name='udalit8'),
    path('udalit8/<int:check>/<int:id>/', login_required(views.udalit8), name='udalit8'),
    path('edit8/<int:id>/', login_required(views.edit8), name='edit8'),
    path('edit8/<int:check>/<int:id>/', login_required(views.edit8), name='edit8'),
    path('update8/<int:id>/', login_required(views.update8), name='update8'),
    path('update8/<int:check>/<int:id>/', login_required(views.update8), name='update8'),

    path('suppliers/', login_required(views.suppliers), name='suppliers'),
    path('suppliers/<int:check>/<int:user_id>/', login_required(views.suppliers), name='suppliers'),
    path('delete9/<int:id>/', login_required(views.delete9), name='delete9'),
    path('delete9/<int:check>/<int:id>/', login_required(views.delete9), name='delete9'),
    path('udalit9/<int:id>/', login_required(views.udalit9), name='udalit9'),
    path('udalit9/<int:check>/<int:id>/', login_required(views.udalit9), name='udalit9'),
    path('edit9/<int:id>/', login_required(views.edit9), name='edit9'),
    path('edit9/<int:check>/<int:id>/', login_required(views.edit9), name='edit9'),
    path('update9/<int:id>/', login_required(views.update9), name='update9'),
    path('update9/<int:check>/<int:id>/', login_required(views.update9), name='update9'),

    path('accept_order/<int:order_id>/', login_required(views.accept_order), name='accept_order'),
    path('cancel_order/<int:order_id>/', login_required(views.cancel_order), name='cancel_order'),

    path('accept_order/<int:order_id>/<int:check>/', login_required(views.accept_order), name='accept_order'),
    path('cancel_order/<int:order_id>/<int:check>/', login_required(views.cancel_order), name='cancel_order'),

    path('accept_task/<int:planner_id>/', login_required(views.accept_task), name='accept_task'),
    path('cancel_task/<int:planner_id>/', login_required(views.cancel_task), name='cancel_task'),

    path('accept_task/<int:planner_id>/<int:check>/', login_required(views.accept_task), name='accept_task'),
    path('cancel_task/<int:planner_id>/<int:check>/', login_required(views.cancel_task), name='cancel_task'),

    path('planner/<str:filter_status>/', login_required(views.planner), name='planner_with_filter'),
    path('orders/<str:filter_status>/', login_required(views.orders), name='orders_with_filter'),

    path('planner/<int:check>/<int:user_id>/<str:filter_status>/', login_required(views.planner), name='planner_with_filter'),
    path('orders/<int:check>/<int:user_id>/<str:filter_status>/', login_required(views.orders), name='orders_with_filter'),


    path('register/',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('export_brands_to_excel/', login_required(views.export_brands_to_excel), name='export_brands_to_excel'),
    path('export_clients_to_excel/', login_required(views.export_clients_to_excel), name='export_clients_to_excel'),
    path('export_departments_to_excel/', login_required(views.export_departments_to_excel), name='export_departments_to_excel'),
    path('export_expense_to_excel/', login_required(views.export_expense_to_excel), name='export_expense_to_excel'),
    path('export_orders_to_excel/', login_required(views.export_orders_to_excel), name='export_orders_to_excel'),
    path('export_planner_to_excel/', login_required(views.export_planner_to_excel), name='export_planner_to_excel'),
    path('export_positions_to_excel/', login_required(views.export_positions_to_excel), name='export_positions_to_excel'),
    path('export_products_to_excel/', login_required(views.export_products_to_excel), name='export_products_to_excel'),
    path('export_staff_to_excel/', login_required(views.export_staff_to_excel), name='export_staff_to_excel'),
    path('export_suppliers_to_excel/', login_required(views.export_suppliers_to_excel), name='export_suppliers_to_excel'),

    path('delete_selected_brands/', login_required(views.delete_selected_brands), name='delete_selected_brands'),
    path('delete_selected_brands/<int:check>/<int:user_id>/', login_required(views.delete_selected_brands), name='delete_selected_brands'),
    path('delete_selected_clients/', login_required(views.delete_selected_clients), name='delete_selected_clients'),
    path('delete_selected_clients/<int:check>/<int:user_id>/', login_required(views.delete_selected_clients), name='delete_selected_clients'),

    path('delete_selected_departments/', login_required(views.delete_selected_departments), name='delete_selected_departments'),
    path('delete_selected_departments/<int:check>/<int:user_id>/', login_required(views.delete_selected_departments), name='delete_selected_departments'),
    path('delete_selected_expense/', login_required(views.delete_selected_expense), name='delete_selected_expense'),
    path('delete_selected_expense/<int:check>/<int:user_id>/', login_required(views.delete_selected_expense), name='delete_selected_expense'),
    path('delete_selected_orders/', login_required(views.delete_selected_orders), name='delete_selected_orders'),
    path('delete_selected_orders/<int:check>/<int:user_id>/', login_required(views.delete_selected_orders), name='delete_selected_orders'),
    path('delete_selected_planner/', login_required(views.delete_selected_planner), name='delete_selected_planner'),
    path('delete_selected_planner/<int:check>/<int:user_id>/', login_required(views.delete_selected_planner), name='delete_selected_planner'),
    path('delete_selected_positions/', login_required(views.delete_selected_positions), name='delete_selected_positions'),
    path('delete_selected_positions/<int:check>/<int:user_id>/', login_required(views.delete_selected_positions), name='delete_selected_positions'),
    path('delete_selected_products/', login_required(views.delete_selected_products), name='delete_selected_products'),
    path('delete_selected_products/<int:check>/<int:user_id>/', login_required(views.delete_selected_products), name='delete_selected_products'),
    path('delete_selected_staff/', login_required(views.delete_selected_staff), name='delete_selected_staff'),
    path('delete_selected_staff/<int:check>/<int:user_id>/', login_required(views.delete_selected_staff), name='delete_selected_staff'),
    path('delete_selected_suppliers/', login_required(views.delete_selected_suppliers), name='delete_selected_suppliers'),
    path('delete_selected_suppliers/<int:check>/<int:user_id>/', login_required(views.delete_selected_suppliers), name='delete_selected_suppliers'),

    path('', login_required(views.profile), name='profile'),
    path('update_profile/<int:user_id>', login_required(views.update_profile), name='update_profile'),
    path('update_profile/<int:user_id>/<int:check>/', views.update_profile, name='update_profile'),


    path('stats/<int:check>/', login_required(views.stats), name='stats'),
    path('stats', login_required(views.stats), name='stats'),

    

    path('settings', user_passes_test(is_staff, login_url='profile')(views.settings), name='settings'),
    path('update_settings', user_passes_test(is_superuser, login_url='profile')(login_required(views.update_settings)), name='update_settings'),


    path('sadmin/',user_passes_test(is_staff, login_url='profile')(login_required(views.sadmin)),name='sadmin'),
    path('delete_user/<int:user_id>',user_passes_test(is_staff, login_url='profile')(login_required(views.delete_user)),name='delete_user'),
    path('block_user/<int:user_id>/', user_passes_test(is_superuser, login_url='profile')(login_required(views.block_user)), name='block_user'),
    path('update_user/<int:user_id>/', user_passes_test(is_staff, login_url='profile')(login_required(views.update_user)), name='update_user'),
    path('set_admin_user/<int:user_id>/', user_passes_test(is_superuser,login_url='profile')(login_required(views.set_admin_user)), name='set_admin_user'),
    

    path('manage',user_passes_test(is_superuser, login_url='profile')(login_required(views.manage)),name='manage'),
    path('permissions',user_passes_test(is_superuser, login_url='profile')(login_required(views.permissions)),name='permissions'),

    path('contact',views.contact,name='contact'),
    path('look_messages',user_passes_test(is_staff, login_url='profile')(login_required(views.look_messages)),name='look_messages'),
    path('delete_messages/<int:id>',user_passes_test(is_staff, login_url='profile')(login_required(views.delete_messages)),name='delete_messages'),
    path('clean_messages/<int:id>',user_passes_test(is_staff,login_url='profile')(login_required(views.clean_messages)),name='clean_messages'),

    path('accept_messages/<int:id>/', user_passes_test(is_staff, login_url='profile')(login_required(views.accept_messages)), name='accept_messages'),
    path('cancel_messages/<int:id>/', user_passes_test(is_staff, login_url='profile')(login_required(views.cancel_messages)), name='cancel_messages'),


    path('mesaj',views.mesaj,name='mesaj'),
    path('chat',views.chat,name='chat'),
    path('chat/<int:id>/',views.chat,name='chat')
 ]