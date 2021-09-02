import unittest

try:
    from .test_task_use_cases import TestTaskUseCases
    from .test_client_use_cases import TestClientUseCases
    from .test_auth_use_case import TestAuthUseCase
    from .test_cache import TestSingletonCache
except ImportError:
    from test_task_use_cases import TestTaskUseCases
    from test_client_use_cases import TestClientUseCases
    from test_auth_use_case import TestAuthUseCase
    from test_cache import TestSingletonCache

if __name__ == '__main__':
    unittest.main()
