import cyberjake


def test_remove_bom_inplace():
    cyberjake.file_utils.remove_bom_inplace("README.md")
