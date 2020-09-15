from app import views

rule = {
    '/': views.IndexView(),
    '/about/': views.AboutView(),
    '/contacts/': views.ContactPageView(),
    '/courses/': views.CoursePageView(),
    '/register/': views.RegisterUserView(),
    '/showuser/': views.RegisterUserView.create_user,
}


def secret_controller(request):
    request['secret'] = 'secret'


front_controllers = [
    secret_controller
]
