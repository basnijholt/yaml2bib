"""Nox sessions."""

import nox


@nox.session(python=["3.8", "3.9", "3.10", "3.11"])
def pytest(session: nox.Session) -> None:
    """Run the test suite."""
    session.install(".[test,]")
    session.run("coverage", "erase")
    session.run("pytest")
