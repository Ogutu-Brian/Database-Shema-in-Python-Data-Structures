# import sys
# sys.path.append('/home/Ogutu/Desktop/Training Flask/venv')
from instance.config import secret_key
from app.api.v1.views.question import question_view
from app.api.v1.views.user import user_view
from app.api.v1.views.answer import answer_view
