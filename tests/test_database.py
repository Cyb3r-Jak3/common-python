import cyberjake
import os
import pytest


def _clear_environ():
    for x in [
        "DATABASE_USER",
        "DATABASE_PASSWORD",
        "DATABASE_HOST",
        "DATABASE_PORT",
        "DATABASE_DATABASE",
        "DATABASE_URL"
    ]:
        try:
            del os.environ[x]
        except KeyError:
            pass


def test_database_URL():
    os.environ["DATABASE_URL"] = "test"
    url = cyberjake.build_database_url("postgres")
    assert url == "test"
    _clear_environ()


def test_unsupported_protocol():
    with pytest.raises(ValueError):
        cyberjake.build_database_url("fake")


def test_database_postgres_defaults():
    url = cyberjake.build_database_url("postgres")
    assert url == "postgres://postgres:@localhost:5432/postgres"


def test_database_mysql_defaults():
    url = cyberjake.build_database_url("mysql")
    assert url == "mysql://root:@localhost:3306/"


def test_database_postgres_build():
    os.environ["DATABASE_USER"] = "test_user"
    os.environ["DATABASE_PASSWORD"] = "weakpassword"
    os.environ["DATABASE_HOST"] = "127.0.0.2"
    os.environ["DATABASE_PORT"] = "5435"
    os.environ["DATABASE_DATABASE"] = "testing"
    url = cyberjake.build_database_url("postgres")
    assert url == "postgres://test_user:weakpassword@127.0.0.2:5435/testing"
    _clear_environ()
