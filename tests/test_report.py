
import datetime

from unittest import TestCase, main
from unittest.mock import patch
from io import StringIO
from report_racing_app import abbreviations_to_dict, string_to_time, build_report, print_report


class TestReportRacingApp(TestCase):

    def test_abbreviations_to_dict(self):
        text = "SVF_Sebastian Vettel_FERRARI"
        result = abbreviations_to_dict(text)
        self.assertEqual(result, {'SVF': 'Sebastian Vettel | FERRARI'})

    def test_string_to_time(self):
        string = "SVF2018-05-24_12:02:58.917"
        result = string_to_time(string)
        self.assertEqual(result, {'SVF': datetime.datetime(1900, 1, 1, 12, 2, 58, 917000)})

    @patch('builtins.open', side_effect=[
        StringIO("SVF_Sebastian Vettel_FERRARI\n"),
        StringIO("SVF2018-05-24_12:02:58.917\n"),
        StringIO("SVF2018-05-24_12:04:03.332\n")
    ])
    def test_build_report(self, mock_open):
        path = 'mock_path'
        result_abbreviations, sorted_time_result = build_report(path)
        expected_abbreviations = {'SVF': 'Sebastian Vettel | FERRARI'}
        expected_time_result = {'SVF': datetime.timedelta(seconds=64, microseconds=415000)}

        self.assertEqual(result_abbreviations, expected_abbreviations)
        self.assertEqual(sorted_time_result, expected_time_result)

    def test_invalid_input(self):
        result = abbreviations_to_dict("invalid_text")
        self.assertIsNone(result)

    def test_print_report_with_driver(self):
        path = "/data_files"
        driver = "SVF"
        with patch('report_racing_app.build_report',
                   return_value=({'SVF': 'Sebastian Vettel | FERRARI'},
                                 {'SVF': datetime.timedelta(seconds=64, microseconds=415000)})):
            result = print_report(path, driver=driver)
        expected_output = ['Sebastian Vettel | FERRARI | 0:01:04.415000']
        self.assertEqual(result, expected_output)


if __name__ == '__main__':
    main()
