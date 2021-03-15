def sort_by(names, first_letter=False):
    if first_letter:
        names.sort()

    return names


class TestSort:
    def test_sort(self):
        # given
        names = ['Alina','Ewa','Paulina','Maciej']

        # when
        sorted_names = sort_by(names, first_letter=True)

        # then
        assert sorted_names == ['Alina','Ewa','Maciej','Paulina']