from django.urls import path
import itemsapp.views as itemsapp

app_name = "itemsapp"

urlpatterns = [
    path('monitors/', itemsapp.MonitorList.as_view(), name='monitors'),
    path('monitors/create/', itemsapp.MonitorCreate.as_view(), name='monitor_create'),
    path('monitors/update/<int:pk>/', itemsapp.MonitorUpdate.as_view(), name='monitor_update'),
    path('monitors/delete/<int:pk>/', itemsapp.MonitorDelete.as_view(), name='monitor_delete'),

    path('printers/', itemsapp.PrinterList.as_view(), name='printers'),
    path('printers/create/', itemsapp.PrinterCreate.as_view(), name='printer_create'),
    path('printers/update/<int:pk>/', itemsapp.PrinterUpdate.as_view(), name='printer_update'),
    path('printers/delete/<int:pk>/', itemsapp.PrinterDelete.as_view(), name='printer_delete'),

    path('scanners/', itemsapp.ScannerList.as_view(), name='scanners'),
    path('scanners/create/', itemsapp.ScannerCreate.as_view(), name='scanner_create'),
    path('scanners/update/<int:pk>/', itemsapp.ScannerUpdate.as_view(), name='scanner_update'),
    path('scanners/delete/<int:pk>/', itemsapp.ScannerDelete.as_view(), name='scanner_delete'),

    path('sysblocks/', itemsapp.SysBlockList.as_view(), name='sysblocks'),
    path('sysblocks/create/', itemsapp.SysBlockCreate.as_view(), name='sysblock_create'),
    path('sysblocks/update/<int:pk>/', itemsapp.SysBlockUpdate.as_view(), name='sysblock_update'),
    path('sysblocks/delete/<int:pk>/', itemsapp.SysBlockDelete.as_view(), name='sysblock_delete'),

    path('ups/', itemsapp.UpsList.as_view(), name='ups'),
    path('ups/create/', itemsapp.UpsCreate.as_view(), name='ups_create'),
    path('ups/update/<int:pk>/', itemsapp.UpsUpdate.as_view(), name='ups_update'),
    path('ups/delete/<int:pk>/', itemsapp.UpsDelete.as_view(), name='ups_delete'),
]
