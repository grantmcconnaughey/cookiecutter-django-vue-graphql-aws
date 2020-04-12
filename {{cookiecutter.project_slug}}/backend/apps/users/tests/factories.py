import factory


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'users.User'

    username = 'user'
    email = '{{cookiecutter.email}}'
    full_name = '{{cookiecutter.author_name}}'
