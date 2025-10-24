# Python entende arquivos com final _test.py e funções 
# que começem com test_ sendo testes do projeto
import pytest
from .db_connection_handler import DbConnectionHandler

@pytest.mark.skip(reason="Integration with DB")
def test_db_connection_handler():
    db_conn_handler = DbConnectionHandler()

    # validador de testes unitarios (assert)
    assert db_conn_handler.session is None

    with db_conn_handler:
        assert db_conn_handler.session is not None

