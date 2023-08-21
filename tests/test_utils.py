from utils import mask_account_number
from utils import input_to
from utils import data_time
from utils import sorting_from_empty
from utils import sorting_from_data
from utils import print_to_sum
from utils import print_from_to
from utils import print_date_description


def test_mask_account_number():
    assert mask_account_number({"to": "Счет 64686473678894779589"}) == "Счет **9589"
    assert mask_account_number({"to": "Visa Platinum 8990922113665229"}) == "Visa Platinum 8990 09** **** 5229"


def test_input_to():
    assert input_to({"from": "Visa Classic 6831982476737658"}) == "Visa Classic 6831 19** **** 7658"
    assert input_to({"from": "Счет 48894435694657014368"}) == "Счет **4368"
    assert input_to({}) == "Выполнен перевод на счет вклада"


def test_datatime():
    assert data_time("2019-03-23T01:09:46.296404") == "23.3.2019"


def test_sorting_from_empty():
    assert sorting_from_empty([]) == []
    assert sorting_from_empty([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]


def test_sorting_from_data():
    assert sorting_from_data([{"date": "2019-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"}]) == [
        {'date': '2019-08-26T10:50:58.294041'}, {'date': '2019-07-03T18:35:29.512364'}]
    assert sorting_from_data([{"date": "2019-07-26T10:50:58.294041"}, {"date": "2019-08-03T18:35:29.512364"}]) == [
        {'date': '2019-08-03T18:35:29.512364'}, {'date': '2019-07-26T10:50:58.294041'}]


def test_print_to_sum():
    assert print_to_sum(
        {'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}}) == "21344.35 руб."


def test_print_from_to():
    assert print_from_to({'from': 'Maestro 1596837868705199',
                          'to': 'Счет 64686473678894779589'}) == "Maestro 1596 68** **** 5199 -> Счет **9589"


def test_print_date_description():
    assert print_date_description(
        {'date': '2019-08-26T10:50:58.294041', 'description': 'Перевод организации'}) == "26.8.2019 Перевод организации"