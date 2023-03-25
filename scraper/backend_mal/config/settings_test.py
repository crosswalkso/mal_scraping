# settings.py의 설정을 가져온 후 test_runner.py가 테스트임을 알려준다.
# python manage.py test [app_name] --settings='config.settings_test'
from config.settings import *

# test_runner.py에서 정의한 TestRunner 클래스를 테스트 러너로 지정
TEST_RUNNER = "config.test_runner.TestRunner"
