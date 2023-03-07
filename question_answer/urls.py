from rest_framework.routers import DefaultRouter
from question_answer.views import QuestionViewSet, AnswerViewSet, UsersViewSet

router = DefaultRouter()

router.register(r'question', QuestionViewSet)
router.register(r'answer', AnswerViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = router.urls
