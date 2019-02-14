from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    # this is custom permission to only allow owners of an
    # object to edit it

    def has_object_permission(self, request, view, obj):
        # read perm's are allowed to any request
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # write perm's are only allowed to the owner of the snippet
        return obj.owner == request.user
