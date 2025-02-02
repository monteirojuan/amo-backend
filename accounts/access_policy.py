"""Este módulo contem as definições de aplicativo 'accounts'."""
from rest_access_policy import AccessPolicy


class UserViewAccessPolicy(AccessPolicy):
    """Define o controle de acesso para UserViewSet"""

    statements = [
        {
            "action": ["registrar"],
            "principal": ["anonymous"],
            "effect": "allow",
        },
        {
            "action": ["<method:patch>"],
            "principal": "authenticated",
            "condition": ["is_owner"],
            "effect": "allow",
        },
        {
            "action": ["ativar", "list", "retrieve"],
            "principal": "authenticated",
            "effect": "allow",
        },
    ]

    def is_owner(self, request, view, *args):
        """Verifica que o usuário da requisição e do objeto são o mesmo.

        Esta verificação impede que um usuário edite os dados de outro.
        """
        return request.user == view.get_object()
