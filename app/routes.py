from app import views

rule = {
    '/': views.IndexView(),
    '/about/': views.AboutView(),
    '/contacts/': views.ContactPageView(),
    '/courses/': views.CoursePageView(),
}


def secret_controller(request):
    request['secret'] = 'secret'


front_controllers = [
    secret_controller
]
