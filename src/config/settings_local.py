ALLOWED_HOSTS = [
    '*',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pushes_db',
        'USER': 'pushes_user',
        'PASSWORD': 'pushes_test',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
