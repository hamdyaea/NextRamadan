# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
from datetime import date
from pathlib import Path
import tempfile
import unittest
from app import create_app, next_ramadan


class CalendarTests(unittest.TestCase):
    def test_same_day(self):
        self.assertEqual(next_ramadan("2030-01-01", date(2030, 1, 1))[1], 0)

    def test_tomorrow(self):
        self.assertEqual(next_ramadan("2030-01-02", date(2030, 1, 1))[1], 1)

    def test_unsorted_and_expired(self):
        self.assertEqual(next_ramadan("2031-01-01\n2020-01-01\n2030-01-02",
                                     date(2030, 1, 1))[0], date(2030, 1, 2))

    def test_exhausted_or_invalid(self):
        for text in ("", "2020-01-01", "invalid"):
            with self.assertRaises(ValueError):
                next_ramadan(text, date(2030, 1, 1))

    def test_unavailable_calendar_returns_503(self):
        with tempfile.TemporaryDirectory() as directory:
            client = create_app(Path(directory) / "missing.txt").test_client()
            self.assertEqual(client.get("/").status_code, 503)


if __name__ == "__main__":
    unittest.main()
