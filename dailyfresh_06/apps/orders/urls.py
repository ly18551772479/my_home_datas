
import haystack
from django.conf.urls import include, url
from django.contrib import admin

from orders import views

urlpatterns = [
    url(r'^place$', views.PlaceOrdereView.as_view(),name='place'),
    url(r'^commit$', views.CommitOrderView.as_view(),name='commit'),
    # 我的订单
    url('^(?P<page>\d+)$', views.UserOrdersView.as_view(), name="info"),
    url('^pay$', views.PayView.as_view(), name="pay"), #支付
    url('^check_pay$', views.CheckPayStatusView.as_view(), name="check_pay"),#查询支付结果
    url('^comment/(?P<order_id>\d+)$', views.CommentView.as_view(), name="comment"),#评论
]
