from rest_framework import routers

# import quiz.urls
# import games.urls
import users.urls
import resume.urls
import jobs.urls
import interviews.urls
import companies.urls
import meetings.urls
import files.urls

router = routers.DefaultRouter()
# router.registry.extend(quiz.urls.router.registry)
# router.registry.extend(games.urls.router.registry)
router.registry.extend(users.urls.router.registry)
router.registry.extend(resume.urls.router.registry)
router.registry.extend(jobs.urls.router.registry)
router.registry.extend(interviews.urls.router.registry)
router.registry.extend(companies.urls.router.registry)
router.registry.extend(meetings.urls.router.registry)
router.registry.extend(files.urls.router.registry)

urlpatterns = router.urls