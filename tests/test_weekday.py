import when_exactly as we

def test_week_day_next_edge_cases():
    sunday = we.WeekDay(2025,20,7)
    assert sunday.next == we.WeekDay(2025, 21, 1)

    last_week_day_of_year = we.WeekDay(2024, 52,7)
    assert last_week_day_of_year.next == we.WeekDay(
        2025,1,1
    )

def test_week_day_week():
    week_day = we.WeekDay(2025, 5,3)
    assert week_day.week == we.Week(2025, 5)

    # we.WeekDay(2025,1,1) is 2024-12-30
    assert we.WeekDay(2025,1,1).week == we.Week(2025,1) # day with different month-day

def test_weed_day_to_day():
    week_day = we.WeekDay(2025,1,1)
    assert week_day.to_day() == we.Day(2024,12,30)