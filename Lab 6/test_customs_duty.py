
from hypothesis import given, strategies as st
from customs_duty import parse_declaration, duty_amount, hs_chapter


@given(st.text() | st.none())
def test_parse_declaration_no_crash(s):
    result = parse_declaration(s)
    assert result is None or (
        isinstance(result, tuple)
        and len(result) == 2
        and isinstance(result[0], str)
        and isinstance(result[1], float)
    )


@given(st.text() | st.none())
def test_duty_amount_no_crash(s):
    result = duty_amount(s)
    assert result is None or isinstance(result, float)


@given(st.text() | st.none())
def test_hs_chapter_no_crash(s):
    result = hs_chapter(s)
    assert result is None or isinstance(result, int)
