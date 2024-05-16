from myrepo import DataPipeline

from myrepo.a import B


def test_data_pipeline():
    dp = DataPipeline("exe")
    assert dp.best_trees_to_plant() == ["fern", "apple"]


def test_another_one():
    dp = DataPipeline("exe")
    assert dp.best_trees_to_plant() == ["fern", "apple"]
