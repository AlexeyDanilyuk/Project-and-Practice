import views
import courses

routes = {
    '/': views.IndexView(),
    '/about/': views.AboutView(),
    '/contacts/': views.ContactPageView(),
    '/courses/': views.CoursePageView(),
    '/courses/create/': courses.Course.create_course(data='new_course.html'),
}
