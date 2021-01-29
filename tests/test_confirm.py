from click.testing import CliRunner

from confirm.__main__ import main


def test_confirm():
    # type: () -> None
    runner = CliRunner()

    inputs_yes = ["y", "yes", "Y", "YES", "Yes"]

    inputs_no = ["n", "no", "N", "NO", "No"]

    for s in inputs_yes:
        result = runner.invoke(main, ["Are you sure?"], input=s + "\n")
        assert result.exit_code == 0

    for s in inputs_no:
        result = runner.invoke(main, ["Are you sure?"], input=s + "\n")
        assert result.exit_code != 0
