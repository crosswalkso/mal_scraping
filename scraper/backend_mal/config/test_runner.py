# 내가 설정한 DB로 테스트할 수 있도록 한다.
# 테스트 DB 생성 없이 테스트 가능
from django.test.runner import DiscoverRunner

# DiscoverRunner - test DB 생성을 담당


class TestRunner(DiscoverRunner):
    def setup_databases(self, **kwargs):
        pass

    def teardown_databases(self, old_config, **kwargs):
        pass
