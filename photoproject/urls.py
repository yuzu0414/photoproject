"""photoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# auth.viewをインポートしてauth_viewという名前で利用する
from django.contrib.auth import views as auth_views
# settingsを追加
from django.conf import settings
# staticを追加
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # photo.urlsへのURLパターン
    path('',include('photo.urls')),

    # accounts.urlsへのURLパターン
    path('',include('accounts.urls')),

    # パスワードリセットのためのURLパターン
    # PasswordResetConfirmViewがプロジェクトのurls.pyを参照するのでここに記載
    # パスワードリセット申し込みページ
    path('password_reset/',
         auth_views.PasswordResetView.as_view(
            template_name = "password_reset.html"),
         name = 'password_reset'),

    # メール送信完了ページ
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name = "password_reset_sent.html"),
         name = 'password_reset_done'),

    # パスワードリセットページ
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(
            template_name = "password_reset_form.html"),
         name = 'password_reset_confirm'),

    # パスワードリセット完了ページ
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
            template_name = "password_reset_done.html"),
         name = 'password_reset_complete'),
]

# urlpatternsにmediaフォルダーのURLパターンを追加
urlpatterns += static(
    # MEDIA_URL = 'media/'
    settings.MEDIA_URL,
    # MEDIA_ROOTにリダイレクト
    document_root=settings.MEDIA_ROOT
    )