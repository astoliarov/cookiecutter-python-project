from {{cookiecutter.project_slug}}.logic import some_logic_stuff


def test__some_logic_stuff__expected_result():
    a = 2
    b = 3

    assert some_logic_stuff(a=a, b=b) == 5
