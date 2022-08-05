from .settings import password_requirements

def isauth_context_processor(request):
    return {
        'isAuthenticated': request.COOKIES.get('isAuthenticated'),
        'pass_policy': password_requirements,
        'userName': request.COOKIES.get('userName'),
    }
