import graphene
import graphql_jwt
from graphql_jwt.decorators import login_required
from graphene_django import DjangoObjectType
from uuid import uuid4

from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from apps.users.models import User


class UserType(DjangoObjectType):
    """ User type object """

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'username',
            'full_name',
            'registered_at',
        ]


class Query:
    profile = graphene.Field(UserType)

    @staticmethod
    @login_required
    def resolve_profile(cls, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user


class Register(graphene.Mutation):
    """ Mutation to register a user """

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        full_name = graphene.String(required=True)

    def mutate(self, info, username, email, password, full_name):
        if User.objects.filter(email__iexact=email).exists():
            errors = ['emailAlreadyExists']
            return Register(success=False, errors=errors)

        if User.objects.filter(username__iexact=username).exists():
            errors = ['usernameAlreadyExists']
            return Register(success=False, errors=errors)

        # create user
        user = User.objects.create(username=username, email=email, full_name=full_name)
        user.set_password(password)
        user.save()
        return Register(success=True)


class UpdateProfile(graphene.Mutation):
    """ Mutation to update a user's profile information """

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        full_name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, full_name, username, email):
        user = info.context.user

        if User.objects.filter(email__iexact=email).exclude(pk=user.pk).exists():
            errors = ['emailAlreadyExists']
            return UpdateProfile(success=False, errors=errors)
        if User.objects.filter(username__iexact=username).exclude(pk=user.pk).exists():
            errors = ['usernameAlreadyExists']
            return UpdateProfile(success=False, errors=errors)

        user.full_name = full_name
        user.email = email
        user.username = username
        user.save()
        return UpdateProfile(success=True)


class Logout(graphene.Mutation):
    """ Mutation to logout a user """

    success = graphene.Boolean()

    def mutate(self, info):
        logout(info.context)
        return Logout(success=True)


class ResetPassword(graphene.Mutation):
    """ Mutation for requesting a password reset email """

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        email = graphene.String(required=True)

    def mutate(self, info, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            errors = ['emailDoesNotExists']
            return ResetPassword(success=False, errors=errors)

        params = {
            'user': user,
            'WEBSITE_URL': settings.WEBSITE_URL,
        }
        send_mail(
            subject='Password reset',
            message=render_to_string('mail/password_reset.txt', params),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )
        return ResetPassword(success=True)


class ResetPasswordConfirm(graphene.Mutation):
    """ Mutation for requesting a password reset email """

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    class Arguments:
        token = graphene.String(required=True)
        password = graphene.String(required=True)

    def mutate(self, info, token, password):
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            errors = ['wrongToken']
            return ResetPasswordConfirm(success=False, errors=errors)

        user.set_password(password)
        user.token = uuid4()
        user.save()
        return ResetPasswordConfirm(success=True)


class Mutation:
    login = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    update_profile = UpdateProfile.Field()
    register = Register.Field()
    logout = Logout.Field()
    reset_password = ResetPassword.Field()
    reset_password_confirm = ResetPasswordConfirm.Field()
