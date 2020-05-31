from PyQt5 import QtCore, QtGui, QtWidgets
from .NotificationWidget import Ui_NotificationWidget
from .NotificationWidgetBad import Ui_NotificationWidgetBad

def show_notification(ctx, notif_ctx):
    ctx.__notif_window = QtWidgets.QMainWindow()
    ctx.__notif_widget = Ui_NotificationWidgetBad()
    ctx.__notif_widget.setupUi(ctx.__notif_window)
    ctx.__notif_window.show()

def get_sample_notification_tile(ctx):
    notif_ctx = {
        'title': 'Sample Notification',
        'timestamp': 'H/M/S',
        'type': 'Check In'
    }

    return Ui_NotificationWidget(notif_ctx, add_buttons=False)

def sample_notification(ctx):
    notif_ctx = {
        'title': 'Sample Notification',
        'timestamp': 'Now',
        'type': 'Check In'
    }

    show_notification(ctx, notif_ctx)