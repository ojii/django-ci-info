from django.test.simple import DjangoTestSuiteRunner
try:
    from xmlrunner import XMLTestRunner
except ImportError:
    XMLTestRunner = None


class JenkinsDjangoTestSuiteRunner(DjangoTestSuiteRunner):
    def run_suite(self, suite, **kwargs):
        if XMLTestRunner:
            return XMLTestRunner(output='.').run(suite)
        else:
            return super(JenkinsDjangoTestSuiteRunner, self).run_suite(suite, **kwargs)
