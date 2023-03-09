import graphene
from rx import Observable
from graphene_subscriptions.events import CREATED
from graphene_django.types import DjangoObjectType
from chat.models import Chat

# from your_app.graphql.subscriptions import YourSubscription


class ChatType(DjangoObjectType):
    class Meta:
        model = Chat
        fields = ("id", "text", "sent_at")


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")
    all_chats = graphene.List(ChatType)

    def resolve_all_chats(root, info):
        # We can easily optimize query count in the resolve method
        return Chat.objects.all()


class Subscription(graphene.ObjectType):
    hello = graphene.String()

    chat_created = graphene.Field(ChatType)

    def resolve_chat_created(root, info):
        return root.filter(
            lambda event: event.operation == CREATED
            and isinstance(event.instance, Chat)
        ).map(lambda event: event.instance)

    def resolve_hello(root, info):
        return Observable.interval(1000).map(lambda i: f"hello world {i}!")


#

schema = graphene.Schema(query=Query, subscription=Subscription)
#
# import graphene
#
#
# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")
#
#
# schema = graphene.Schema(query=Query)
