from django.contrib.auth.models import Permission

MODELS_PERMISSIONS = [
    'account.manage_customer',
    'account.manage_staff',
    'sitesetting.manage_sitesettings',
    'blog.manage_category',
    'blog.manage_tag',
    'blog.manage_post',
    'service.manage_service',
    'portfolio.manage_category',
    'portfolio.manage_project',
]


def split_permission_codename(permissions):
    return [permission.split('.')[1] for permission in permissions]


def get_permissions(permissions=None):
    if permissions is None:
        permissions = MODELS_PERMISSIONS
    codenames = split_permission_codename(permissions)
    return (
        Permission.objects.filter(codename__in=codenames)
        .prefetch_related('content_type')
        .order_by('id')
    )
